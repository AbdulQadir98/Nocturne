package com.fourthyear.nocturneapp.ui.anomalies;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class AnomaliesViewModel extends ViewModel {

    private final MutableLiveData<String> mText;

    public AnomaliesViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("This is anomalies fragment of vili");
    }

    public LiveData<String> getText() {
        return mText;
    }
}