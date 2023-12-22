const express = require('express');
const router = express.Router();
const locationController = require('../controllers/locationController');

router.post('/api/locations', locationController.logLocation);

module.exports = router;
