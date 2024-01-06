const locationService = require('../services/location.service');

const locationController = {
  getAllLocations: async (req, res) => {
    try {
      const locations = await locationService.getAllLocations();
      res.json(locations);
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
      const nearbyLocations = await locationService.getNearbyLocations(lat, lng, radius);
      res.json(nearbyLocations);
      
    } catch (error) {
      console.error('Error getting Nearby locations:', error);
      res.status(500).send('Internal Server Error');
    }
  },

  addLocation: async (req, res) => {
    try {
      const { lat, lng } = req.body;
      await locationService.addLocation(lat, lng);
      res.json({ message: 'Location added successfully'});
    } catch (error) {
      console.error('Error creating location:', error);
      res.status(500).send('Internal Server Error');
    }
  },
};

module.exports = locationController;
