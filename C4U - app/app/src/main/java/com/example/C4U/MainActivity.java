package com.example.C4U;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        Intent intent1 = new Intent(MainActivity.this, ButtonsActivity.class); //buttons
        Intent intent2 = new Intent(MainActivity.this, GestureActivity.class); //swipes and stuff
        Intent intent3 = new Intent(MainActivity.this, VoiceActivity.class); //voice

        String sharedPrefFile = "com.c4u.appsharedprefs";
        SharedPreferences mPreferences = getSharedPreferences(sharedPrefFile, MODE_PRIVATE);
        int layout = mPreferences.getInt("method", 1);
        super.onCreate(savedInstanceState);
        if (layout == 1)
        {
            startActivity(intent1);
        }
        else if (layout == 2)
        {
            startActivity(intent2);
        }
        else if (layout == 3)
        {
            startActivity(intent3);
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
    }
}