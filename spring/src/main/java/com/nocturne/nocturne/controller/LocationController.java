package com.nocturne.nocturne.controller;

import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.nocturne.nocturne.entity.Location;
import com.nocturne.nocturne.service.LocationService;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/location")
public class LocationController {

    @Autowired
    LocationService locationService;

    @PostMapping
    @RequestMapping("/")
    public void saveLocation(@RequestBody Location location) {
        locationService.saveLocation(location);
    }

    // private final LocationService locationService;

    // public LocationController(LocationService locationService) {
    // this.locationService = locationService;
    // }

    // @PostMapping
    // @RequestMapping("/")
    // public void saveLocation(@RequestBody Location location) {
    // return locationService.saveLocation(location);
    // }

    // @GetMapping
    // public Flux<Location> getAllLocations() {
    // return locationService.getAllLocations();
    // }

}