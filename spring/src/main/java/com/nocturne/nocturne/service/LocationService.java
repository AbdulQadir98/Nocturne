package com.nocturne.nocturne.service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;

import org.springframework.stereotype.Service;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.cloud.firestore.QuerySnapshot;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import com.nocturne.nocturne.entity.Location;

@Service
public class LocationService {

    // @Autowired
    // private Firestore firestore;

    // private CollectionReference getLocationCollection() {
    // return firestore.collection("location");
    // }

    // public ApiFuture<WriteResult> saveLocation(Location location) {
    // ApiFuture<WriteResult> apiFuture =
    // getLocationCollection().document(location.getId().toString()).set(location);
    // return apiFuture;
    // }

    public void saveLocation(Location location) {
        Firestore db = FirestoreClient.getFirestore();

        DocumentReference docRef = db.collection("location").document();

        location.setId(docRef.getId());
        ApiFuture<WriteResult> apiFuture = docRef.set(location);
    }

    public List<Location> getAllLocations() throws InterruptedException, ExecutionException {
        Firestore db = FirestoreClient.getFirestore();
        ApiFuture<QuerySnapshot> future = db.collection("location").get();
        List<QueryDocumentSnapshot> documents = future.get().getDocuments();

        List<Location> locations = new ArrayList<>();
        for (QueryDocumentSnapshot document : documents) {
            locations.add(document.toObject(Location.class));
        }

        return locations;
    }
}
