package com.nocturne.nocturne.service;

import com.nocturne.nocturne.model.Location;

import java.util.List;
import java.util.concurrent.ExecutionException;
import org.springframework.http.ResponseEntity;

public interface LocationService {
    ResponseEntity<String> saveLocation(Location location);

    List<Location> getAllLocations() throws InterruptedException, ExecutionException;
}
