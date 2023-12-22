const express = require('express');
const router = express.Router();
const locationRoutes = require('./locations');

router.use('/', locationRoutes);

module.exports = router;
