const express = require('express');
const router = express.Router();
const locationController = require('../controllers/location.controller');

// Define location routes
router.get('/location', locationController.getAllLocations);
router.get('/location/nearby', locationController.getNearbyLocations);
router.post('/location', locationController.addLocation);

module.exports = router;
