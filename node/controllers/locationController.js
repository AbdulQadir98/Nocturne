const admin = require('firebase-admin');
const db = admin.firestore();
const logger = require('../logger');

exports.logLocation = (req, res) => {
  const { latitude, longitude } = req.body;
  const locationsRef = db.collection('locations');

  locationsRef
    .add({
      latitude,
      longitude,
      timestamp: admin.firestore.FieldValue.serverTimestamp(),
    })
    .then(() => {
      logger.info('Location logged successfully:', { latitude, longitude });
      res.status(200).send('Location logged successfully');
    })
    .catch((error) => {
      logger.error('Error logging location:', error);
      res.status(500).send('Internal Server Error');
    });
};

exports.getNearbyLocations = async (req, res) => {
  const { latitude, longitude } = req.body;
  const radius = 0.02; // Assuming 0.02 degrees is approximately 20 meters

  const locationsRef = db.collection('locations');
  const query = locationsRef.where('latitude', '>=', latitude - radius)
    .where('latitude', '<=', latitude + radius)
    .where('longitude', '>=', longitude - radius)
    .where('longitude', '<=', longitude + radius);

  try {
    const snapshot = await query.get();
    const nearbyLocations = [];

    snapshot.forEach((doc) => {
      const data = doc.data();
      nearbyLocations.push({
        id: doc.id,
        latitude: data.latitude,
        longitude: data.longitude,
      });
    });

    logger.info('Nearby locations fetched successfully:', { latitude, longitude, nearbyLocations });
    res.status(200).json({ nearbyLocations });
  } catch (error) {
    logger.error('Error fetching nearby locations:', error);
    res.status(500).send('Internal Server Error');
  }
};
