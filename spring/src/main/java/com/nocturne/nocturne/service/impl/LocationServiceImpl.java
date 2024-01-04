package com.nocturne.nocturne.service.impl;

import com.nocturne.nocturne.model.Location;
import com.nocturne.nocturne.service.LocationService;
import com.nocturne.nocturne.util.LocationLogger;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;

import org.springframework.stereotype.Service;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.CollectionReference;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.cloud.firestore.QuerySnapshot;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;

@Service
public class LocationServiceImpl implements LocationService {

    private static final LocationLogger locationLogger = new LocationLogger();

    private static final String COLLECTION_NAME = "location";
    private final Firestore db;

    public LocationServiceImpl() {
        this.db = FirestoreClient.getFirestore();
    }

    private CollectionReference getLocationCollection() {
        return db.collection(COLLECTION_NAME);
    }

    @Override
    public void saveLocation(Location location) {
        try {
            DocumentReference docRef = getLocationCollection().document();

            location.setId(docRef.getId());
            ApiFuture<WriteResult> apiFuture = docRef.set(location);
            apiFuture.get(); // This will throw an exception if the write fails
            // locationLogger.logInfo("saved location:");
        } catch (Exception e) {
            locationLogger.logSevere("Failed to save location: " + e.getMessage());
        }
    }

    @Override
    public List<Location> getAllLocations() throws InterruptedException, ExecutionException {
        ApiFuture<QuerySnapshot> future = getLocationCollection().get();
        List<QueryDocumentSnapshot> documents = future.get().getDocuments();

        List<Location> locations = new ArrayList<>();
        for (QueryDocumentSnapshot document : documents) {
            locations.add(document.toObject(Location.class));
        }

        return locations;
    }
}
