package com.fourthyear.nocturneapp.ui.group;

import android.annotation.SuppressLint;
import android.os.Build;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.PopupWindow;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import com.fourthyear.nocturneapp.R;
import com.fourthyear.nocturneapp.databinding.FragmentGroupBinding;


public class GroupFragment extends Fragment {

    private FragmentGroupBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        GroupViewModel groupViewModel =
                new ViewModelProvider(this).get(GroupViewModel.class);

        binding = FragmentGroupBinding.inflate(inflater, container, false);
        Button creategroupbutton=binding.getRoot().findViewById(R.id.creategroup);

        creategroupbutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Handle the click event to show the popup window
                onButtonShowPopupWindowClick(view);
            }
        });
        View root = binding.getRoot();
        return root;
    }

    //onclicking the @+id/creategroup button the should open group_create_group_popup.xml popup
    @SuppressLint("ClickableViewAccessibility")
    public void onButtonShowPopupWindowClick(View view) {
        // Inflate the popup window layout
        View popupView = getLayoutInflater().inflate(R.layout.group_create_group_popup, null);

        // Create a PopupWindow
        PopupWindow popupWindow = new PopupWindow(
                popupView,
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        );

        // Set focusable and outside touchable to make it behave like a dropdown menu
        popupWindow.setFocusable(true);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.CUPCAKE) {
            popupWindow.setOutsideTouchable(false);
        }

        popupWindow.showAtLocation(view, Gravity.CENTER, 0, 0);

        // Example: Close the popup window when clicking outside
        popupView.setOnTouchListener((v, event) -> {
            popupWindow.dismiss();
            return true;
        });
    }



    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}