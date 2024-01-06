const locatioinServiceInterface = require('./interfaces/location.service.impl');
const Location = require('../models/location.model');

class UserService extends UserServiceInterface {
  async getUserById(userId) {
    try {
      const user = await UserModel.findById(userId);
      return user;
    } catch (error) {
      throw new Error(`Error getting user by ID: ${error.message}`);
    }
  }

  async createUser(user) {
    try {
      const newUser = await UserModel.create(user);
      return newUser;
    } catch (error) {
      throw new Error(`Error creating user: ${error.message}`);
    }
  }
}

module.exports = new UserService();
