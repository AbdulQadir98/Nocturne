const admin = require('firebase-admin');
const db = admin.firestore();

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
      res.status(200).send('Location logged successfully');
    })
    .catch((error) => {
      console.error('Error logging location:', error);
      res.status(500).send('Internal Server Error');
    });
};
