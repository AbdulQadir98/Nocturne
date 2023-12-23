const admin = require('firebase-admin');
const logger = require('../logger');
const { io, geoFirestore } = require('../app'); // Import the io and geoFirestore instances

let previousLocation = null;

exports.logLocation = async (req, res) => {
  const { latitude, longitude } = req.body;

  try {
    // Use GeoFirestore to set the location
    await geoFirestore.collection('locations').doc().set({
      coordinates: new admin.firestore.GeoPoint(latitude, longitude),
      timestamp: admin.firestore.FieldValue.serverTimestamp(),
    });

    logger.info('Location logged successfully:', { latitude, longitude });

    // Check if there is a significant change in location
    if (!previousLocation || distance(previousLocation, { latitude, longitude }) > 0.01) {
      // Emit an update to all connected clients
      io.emit('locationUpdate', { latitude, longitude });

      // Update the previousLocation for the next comparison
      previousLocation = { latitude, longitude };
    }

    res.status(200).send('Location logged successfully');
  } catch (error) {
    logger.error('Error logging location:', error);
    res.status(500).send('Internal Server Error');
  }
};

exports.getNearbyLocations = async (req, res) => {
  const { latitude, longitude } = req.body;
  const radiusInKm = 0.02; // Assuming 0.02 degrees is approximately 20 meters

  try {
    // Use GeoFirestore to query nearby locations
    const query = geoFirestore.collection('locations').near({
      center: new admin.firestore.GeoPoint(latitude, longitude),
      radius: radiusInKm,
    });

    const snapshot = await query.get();
    const nearbyLocations = [];

    snapshot.forEach((doc) => {
      const data = doc.data();
      nearbyLocations.push({
        id: doc.id,
        latitude: data.coordinates.latitude,
        longitude: data.coordinates.longitude,
      });
    });

    logger.info('Nearby locations fetched successfully:', { latitude, longitude, nearbyLocations });
    res.status(200).json({ nearbyLocations });
  } catch (error) {
    logger.error('Error fetching nearby locations:', error);
    res.status(500).send('Internal Server Error');
  }
};

// Helper function to calculate distance between two points (Haversine formula)
function distance(point1, point2) {
  const toRadians = (angle) => (angle * Math.PI) / 180;
  const earthRadius = 6371; // Earth radius in kilometers

  const lat1 = toRadians(point1.latitude);
  const lon1 = toRadians(point1.longitude);
  const lat2 = toRadians(point2.latitude);
  const lon2 = toRadians(point2.longitude);

  const dLat = lat2 - lat1;
  const dLon = lon2 - lon1;

  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) * Math.sin(dLon / 2);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return earthRadius * c;
}


// const admin = require('firebase-admin');
// const logger = require('../logger');
// const { io, geoFirestore } = require('../app'); // Import the io and geoFirestore instances

// let previousLocation = null;

// exports.logLocation = async (req, res) => {
//   const { latitude, longitude } = req.body;

//   try {
//     // Use GeoFirestore to set the location
//     await geoFirestore.collection('locations').doc().set({
//       coordinates: new admin.firestore.GeoPoint(latitude, longitude),
//       timestamp: admin.firestore.FieldValue.serverTimestamp(),
//     });

//     logger.info('Location logged successfully:', { latitude, longitude });

//     // Check if there is a significant change in location
//     if (!previousLocation || distance(previousLocation, { latitude, longitude }) > 0.01) {
//       // Emit an update to all connected clients
//       io.emit('locationUpdate', { latitude, longitude });

//       // Update the previousLocation for the next comparison
//       previousLocation = { latitude, longitude };
//     }

//     res.status(200).send('Location logged successfully');
//   } catch (error) {
//     logger.error('Error logging location:', error);
//     res.status(500).send('Internal Server Error');
//   }
// };

// exports.getNearbyLocations = async (req, res) => {
//   const { latitude, longitude } = req.body;
//   const radiusInKm = 0.02; // Assuming 0.02 degrees is approximately 20 meters

//   try {
//     // Use GeoFirestore to query nearby locations
//     const query = geoFirestore.collection('locations').near({
//       center: new admin.firestore.GeoPoint(latitude, longitude),
//       radius: radiusInKm,
//     });

//     const snapshot = await query.get();
//     const nearbyLocations = [];

//     snapshot.forEach((doc) => {
//       const data = doc.data();
//       nearbyLocations.push({
//         id: doc.id,
//         latitude: data.coordinates.latitude,
//         longitude: data.coordinates.longitude,
//       });
//     });

//     logger.info('Nearby locations fetched successfully:', { latitude, longitude, nearbyLocations });
//     res.status(200).json({ nearbyLocations });
//   } catch (error) {
//     logger.error('Error fetching nearby locations:', error);
//     res.status(500).send('Internal Server Error');
//   }
// };

// // Helper function to calculate distance between two points (Haversine formula)
// function distance(point1, point2) {
//   const toRadians = (angle) => (angle * Math.PI) / 180;
//   const earthRadius = 6371; // Earth radius in kilometers

//   const lat1 = toRadians(point1.latitude);
//   const lon1 = toRadians(point1.longitude);
//   const lat2 = toRadians(point2.latitude);
//   const lon2 = toRadians(point2.longitude);

//   const dLat = lat2 - lat1;
//   const dLon = lon2 - lon1;

//   const a =
//     Math.sin(dLat / 2) * Math.sin(dLat / 2) +
//     Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) * Math.sin(dLon / 2);

//   const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

//   return earthRadius * c;
// }