package com.nocturne.nocturne.util;

import java.util.logging.Logger;

public class LocationLogger {

    private static final Logger logger = Logger.getLogger(LocationLogger.class.getName());

    public void logInfo(String message) {
        logger.info(message);
    }

    public void logSevere(String message) {
        logger.severe(message);
    }
}
