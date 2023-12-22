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
