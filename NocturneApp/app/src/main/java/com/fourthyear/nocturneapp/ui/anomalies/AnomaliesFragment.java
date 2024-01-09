package com.fourthyear.nocturneapp.ui.anomalies;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.fourthyear.nocturneapp.databinding.FragmentAnomaliesBinding;

public class AnomaliesFragment extends Fragment {

    private FragmentAnomaliesBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        AnomaliesViewModel anomaliesViewModel =
                new ViewModelProvider(this).get(AnomaliesViewModel.class);

        binding = FragmentAnomaliesBinding.inflate(inflater, container, false);
        View root = binding.getRoot();

        final TextView textView = binding.textAnomalies;
        anomaliesViewModel.getText().observe(getViewLifecycleOwner(), textView::setText);
        return root;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}