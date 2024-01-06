const locationServiceImplementation = require('./impl/location.service.impl');

const locationService = {
  getAllLocations: async () => {
    return locationServiceImplementation.getAllLocations();
  },

  addLocation: async (lat, lng) => {
    return locationServiceImplementation.addLocation(lat, lng);
  },

  getNearbyLocations: async (lat, lng, radius) => {
    return locationServiceImplementation.getNearbyLocations(lat, lng, radius);
  },
};

module.exports = locationService;
