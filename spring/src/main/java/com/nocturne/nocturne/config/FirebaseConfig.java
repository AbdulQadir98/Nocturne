package com.nocturne.nocturne.config;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import javax.annotation.PostConstruct;

import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;

@Service
public class FirebaseConfig {

    // private static final Logger logger =
    // LoggerFactory.getLogger(FirebaseConfig.class);

    @PostConstruct
    public void configureFirebaseConnection() throws IOException {

        // logger.info("Configuring Firebase connection...");
        try {
            File file = ResourceUtils.getFile("classpath:config/service_account_pk.json");
            FileInputStream serviceAccount = new FileInputStream(file);

            // GoogleCredentials credentials = GoogleCredentials.fromStream(serviceAccount);
            FirebaseOptions options = FirebaseOptions.builder()
                    .setCredentials(GoogleCredentials.fromStream(serviceAccount))
                    .build();
            FirebaseApp.initializeApp(options);
            // logger.info("Firebase connection configured successfully.");

        } catch (Exception e) {
            // e.printStackTrace();
            System.out.println(e);
        }
    }

}