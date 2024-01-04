package com.nocturne.nocturne.controller;

import java.util.List;
import java.util.concurrent.ExecutionException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.nocturne.nocturne.model.Location;
import com.nocturne.nocturne.service.LocationService;

@RestController
@RequestMapping("/location")
public class LocationController {

    @Autowired
    private LocationService locationService;

    public LocationController(LocationService locationService) {
        this.locationService = locationService;
    }

    @PostMapping
    public ResponseEntity<String> saveLocation(@RequestBody Location location) {
        try {
            locationService.saveLocation(location);
            return new ResponseEntity<>("Location saved successfully", HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>("Failed to save location. Error: " + e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping
    public ResponseEntity<List<Location>> getAllLocations() {
        try {
            List<Location> locations = locationService.getAllLocations();
            return new ResponseEntity<>(locations, HttpStatus.OK);
        } catch (InterruptedException | ExecutionException e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    // @GetMapping
    // public void getAllLocations() {
    // try {
    // FirebaseDatabase database = FirebaseDatabase.getInstance();
    // GeoFire geoFire = new GeoFire(database.getReference("locations"));

    // // Perform a geo query
    // GeoLocation center = new GeoLocation(37.7749, -122.4194);
    // double radius = 10.0; // in kilometers

    // geoFire.query().setCenter(center).setRadius(radius).addGeoQueryEventListener(new
    // MyGeoQueryEventListener());
    // } catch (Exception e) {
    // e.printStackTrace();
    // }
    // }

}