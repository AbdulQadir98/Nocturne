package com.nocturne.nocturne.service;

import com.nocturne.nocturne.model.Location;

import java.util.List;
import java.util.concurrent.ExecutionException;

public interface LocationService {
    void saveLocation(Location location);

    List<Location> getAllLocations() throws InterruptedException, ExecutionException;
}
