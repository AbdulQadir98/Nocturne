package com.nocturne.nocturne.service;

import org.springframework.stereotype.Service;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import com.nocturne.nocturne.entity.Location;

@Service
public class LocationService {

    public void saveLocation(Location location) {
        Firestore db = FirestoreClient.getFirestore();

        DocumentReference docRef = db.collection("location").document();

        location.setId(docRef.getId());
        ApiFuture<WriteResult> apiFuture = docRef.set(location);
    }
}
