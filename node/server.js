const express = require('express');
const bodyParser = require('body-parser');
const routes = require('./routes');
const logger = require('./logger');

const app = express();
const port = 3000;

// Middleware for logging requests
app.use((req, res, next) => {
  logger.info(`${req.method} ${req.url}`);
  next();
});

app.use(bodyParser.json());
app.use('/', routes);

app.listen(port, () => {
  logger.info(`Server is listening at http://localhost:${port}`);
});

module.exports = app;
