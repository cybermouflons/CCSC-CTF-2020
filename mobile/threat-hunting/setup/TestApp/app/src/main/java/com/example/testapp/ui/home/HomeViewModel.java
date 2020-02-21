package com.example.testapp.ui.home;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class HomeViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public HomeViewModel() {
        mText = new MutableLiveData<>();
//        mText.setValue("Guard: So, could you please send me your name? \nAgent 47: Names are for friends...so I don't need one.\nGuard: Okay send me your unique identifier then!");
    }

    public LiveData<String> getText() {
        return mText;
    }
}