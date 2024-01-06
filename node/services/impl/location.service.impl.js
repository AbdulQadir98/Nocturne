const Location = require('../../models/location.model');
const GeoFire = require('geofire-common');
const db = require('../../config/firebase-config');
// const location = require('../models/location.model');

const locationServiceImplementation = {
    getAllLocations: async () => {
      const locationSnapshot = await db.collection('location').get();
      const locations = [];
  
      locationSnapshot.forEach((doc) => {
        locations.push(doc.data());
      });
  
      return locations;
    },

    addLocation: async (lat, lng) => {
      const hash = GeoFire.geohashForLocation([lat, lng]);
      // console.log(hash);
  
      const locationRef = db.collection('location').doc();
      await locationRef.set({
        geohash: hash,
        latitude: lat,
        longitude: lng,
      });
    },

    getNearbyLocations: async (lat, lng, radius) => {
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
          const docData = doc.data();

          // We have to filter out a few false positives due to GeoHash
          // accuracy, but most will match
          const distanceInKm = GeoFire.distanceBetween([docData.latitude, docData.longitude], center);
          const distanceInM = distanceInKm * 1000;
  
          if (distanceInM <= radiusInM) {
            matchingDocs.push(docData);
          }
        }
      }
  
      return matchingDocs;
    },

  };
  
  module.exports = locationServiceImplementation;