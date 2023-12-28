package com.nocturne.nocturne.config;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Configuration;
import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;

@Configuration
public class FirebaseConfig {

    private static final Logger logger = LoggerFactory.getLogger(FirebaseConfig.class);

    // @PostConstruct
    public void configureFirebaseConnection() throws IOException {

        logger.info("Configuring Firebase connection...");
        // File file = ResourceUtils.getFile("./service_account_pk.json");
        // FileInputStream serviceAccount = new FileInputStream(file);
        InputStream serviceAccount = new FileInputStream("classpath:config/service_account_pk.json");
        GoogleCredentials credentials = GoogleCredentials.fromStream(serviceAccount);
        FirebaseOptions options = new FirebaseOptions.Builder()
                .setCredentials(credentials)
                .build();

        FirebaseApp.initializeApp(options);
        logger.info("Firebase connection configured successfully.");
    }

}
