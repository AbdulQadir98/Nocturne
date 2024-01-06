const locationService = require('../services/location.service');

const GeoFire = require('geofire-common');
const db = require('../config/firebase-config');
// const location = require('../models/location.model');


const locationController = {
  getAllLocations: async (req, res) => {
    try {
      const locationSnapshot = await db.collection('location').get();
      locationSnapshot.forEach((doc) => {
        res.json(doc.data());
      });
      
    } catch (error) {
      console.error('Error getting location:', error);
      res.status(500).send('Internal Server Error');
    }
  },

  getNearbyLocations: async (req, res) => {
    
    try {
      const { lat, lng, radius } = req.query;
      if (lat === undefined || lng === undefined || radius === undefined) {
        return res.status(400).json({ error: 'Latitude, Longitude, and Radius are required.' });
      }

      const center = [parseFloat(lat), parseFloat(lng)];
      const radiusInM = parseFloat(radius) * 1000;
      // Each item in 'bounds' represents a startAt/endAt pair. We have to issue
      // a separate query for each pair. There can be up to 9 pairs of bounds
      // depending on overlap, but in most cases there are 4.
      const bounds = GeoFire.geohashQueryBounds(center, radiusInM);
      const promises = [];

      for (const b of bounds) {
        const q = db.collection('location') 
          .orderBy('geohash')
          .startAt(b[0])
          .endAt(b[1]);
      
        promises.push(q.get());
      }

      // Collect all the query results together into a single list
      const snapshots = await Promise.all(promises);
      const matchingDocs = [];

      for (const snap of snapshots) {
        for (const doc of snap.docs) {
          const lat = doc.get('latitude');
          const lng = doc.get('longitude');

          // We have to filter out a few false positives due to GeoHash
          // accuracy, but most will match
          const distanceInKm = GeoFire.distanceBetween([lat, lng], center);
          const distanceInM = distanceInKm * 1000;
          if (distanceInM <= radiusInM) {
            matchingDocs.push(doc.data());
          }
        }
      }
      res.json(matchingDocs);
      
    } catch (error) {
      console.error('Error getting Nearby locations:', error);
      res.status(500).send('Internal Server Error');
    }
  },

  addLocation: async (req, res) => {
    
    try {
      const { lat, lng } = req.body;
      const hash = GeoFire.geohashForLocation([lat, lng]);

      const locationRef = db.collection('location').doc();
      await locationRef.set({
        geohash: hash,
        latitude: lat,
        longitude: lng,
      });

      // console.log(hash);
      res.json({ message: 'Location added successfully'});
    } catch (error) {
      console.error('Error creating location:', error);
      res.status(500).send('Internal Server Error');
    }
  },
};

module.exports = locationController;
