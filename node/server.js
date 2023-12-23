const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const bodyParser = require('body-parser');
const admin = require('firebase-admin');
const GeoFirestore = require('geofirestore');
const routes = require('./routes');
const logger = require('./logger');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);
const port = 3000;

// Initialize Firebase Admin SDK
const serviceAccount = require('./path/to/your/serviceAccountKey.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://your-project-id.firebaseio.com',
});

// Initialize GeoFirestore with Firestore instance
const db = admin.firestore();
const geoFirestore = new GeoFirestore.GeoFirestore(db);

app.use(bodyParser.json());
app.use('/', routes);

// Middleware for logging requests
app.use((req, res, next) => {
  logger.info(`${req.method} ${req.url}`);
  next();
});

// WebSocket connection handling
io.on('connection', (socket) => {
  logger.info(`Client connected: ${socket.id}`);

  // Handle disconnection
  socket.on('disconnect', () => {
    logger.info(`Client disconnected: ${socket.id}`);
  });
});

// Start the server
server.listen(port, () => {
  logger.info(`Server is listening at http://localhost:${port}`);
});

module.exports = { app, io, geoFirestore };  // Export the app, io, and geoFirestore instances for testing purposes
