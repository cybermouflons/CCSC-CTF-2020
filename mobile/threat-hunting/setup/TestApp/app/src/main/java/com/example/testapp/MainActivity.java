package com.example.testapp;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.navigation.NavigationView;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Collections;
import java.util.concurrent.ExecutionException;

@SuppressWarnings("all")

public class MainActivity extends AppCompatActivity {

    private AppBarConfiguration mAppBarConfiguration;
    String hex_final = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                //Url endpoint
                String myUrl = "http://134.209.189.120:5000/test_valid?string=" + hex_final;

                //String to place the response
                String result = null;

                //Instantiate new instance of our class
                HTTPReq getRequest = new HTTPReq();

                //Perform the doInBackground method, passing in our url
                try {
                    result = getRequest.execute(myUrl).get();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                // globally
                TextView myAwesomeTextView = (TextView) findViewById(R.id.myAwesomeTextView);

                //in your OnCreate() method
                myAwesomeTextView.setText(result);
            }
        });
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        mAppBarConfiguration = new AppBarConfiguration.Builder(
                R.id.nav_home)
                .setDrawerLayout(drawer)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment);
        NavigationUI.setupActionBarWithNavController(this, navController, mAppBarConfiguration);
        NavigationUI.setupWithNavController(navigationView, navController);


        // globally
        TextView myAwesomeTextView = (TextView) findViewById(R.id.myAwesomeTextView);

        if (checkForBinary("su") == false && checkForBinary("busybox") == false) {

            if (checkForBinary2("su") == true || checkForBinary2("busybox") == true) {

                String u = "e86c1268-08e4-4529-8758-4589bde0e854";

                String myUrl = null;

                SharedPreferences a; // 0 - for private mode
                a = getApplicationContext().getSharedPreferences("MyPref", 0);
                SharedPreferences.Editor b = a.edit();
                b.clear();

                b.putBoolean("key_name", true); // Storing boolean - true/false
                b.putString("secret", u); // Storing string
                int a_1 = 124;
                b.putInt("num", a_1);
                float b_1 = 2;
                b.putStringSet("set2", Collections.singleton("കൊങകൊങ് ♺ ☼ ☂ ☺ ☹ കണി ്കas΅ρ;214128pu7y21ൊങ്കണി കണ"));
                b.putFloat("num2", b_1);
                b.putFloat("num2", a_1);
                b.putStringSet("set1", Collections.singleton(" ♐ ♑τ ♐ ♑e ♐ ♑st1 ♐ ♑"));
                b.putStringSet("⌸", Collections.singleton("കൊങകൊങ്കണി ്കas΅▇ ✈ρ;214128pu7y21ൊങ്കണി കണ"));
                b.putStringSet("set3", Collections.singleton(" ♐ ♑tesτ1 ♐ ♑"));
                b.putStringSet("⌹", Collections.singleton("കൊങകൊങ്കണി ്കas΅ρ;214128pu7y21ൊങ്കണി കണ"));
                b.putStringSet("⌷ ⌸ ⌹ ", Collections.singleton(" ɍ Ɍ Ʀ  ȋ Ⓜ ⓜ ⒨ M m Ḿ ḿ Ṁ ṁ Ṃ ṃ ꟿ ꟽ Ɱ Ʃ Ɯ"));

                b.commit(); // commit changes

                MessageDigest md = null; //SHA, MD2, MD5, SHA-256, SHA-384...
                try {
                    md = MessageDigest.getInstance("SHA-256");
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                }
                hex_final = null;
                try {
                    hex_final = checksum("/data/data/com.example.testapp/shared_prefs/MyPref.xml", md);

                } catch (IOException e) {
                    e.printStackTrace();
                }

            }

        } else {
            SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", 0); // 0 - for private mode
            SharedPreferences.Editor editor = pref.edit();
            editor.clear();

            editor.putBoolean("key_name", true); // Storing boolean - true/false
            editor.putString("secret", "Your_device_is_rooted!! You ain't getting any secrets :)"); // Storing string

            editor.commit(); // commit changes

            MessageDigest md1 = null; //SHA, MD2, MD5, SHA-256, SHA-384...
            try {
                md1 = MessageDigest.getInstance("SHA-256");
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
            }
            hex_final = null;
            try {
                hex_final = checksum("/data/data/com.example.testapp/shared_prefs/MyPref.xml", md1);

            } catch (IOException e) {
                e.printStackTrace();
            }

        }

    }

    private static String checksum(String filepath, MessageDigest md) throws IOException {

        try (DigestInputStream dis = new DigestInputStream(new FileInputStream(filepath), md)) {
            while (dis.read() != -1) ;
            md = dis.getMessageDigest();
        }

        StringBuilder result = new StringBuilder();
        for (byte b : md.digest()) {
            result.append(String.format("%02x", b));
        }
        return result.toString();

    }


    public static String getFileChecksum(MessageDigest digest, File file) throws IOException {
        FileInputStream fis = new FileInputStream(file);

        byte[] byteArray = new byte[1024];
        int bytesCount = 0;

        while ((bytesCount = fis.read(byteArray)) != -1) {
            digest.update(byteArray, 0, bytesCount);
        }
        ;

        fis.close();

        byte[] bytes = digest.digest();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bytes.length; i++) {
            sb.append(Integer.toString((bytes[i] & 0xff) + 0x100, 16).substring(1));
        }

        return sb.toString();
    }

    public void onClick(View v) {
        //Url endpoint
        String myUrl = "http://134.209.189.120:5000/test_valid?string=" + hex_final;

        //String to place the response
        String result = null;

        //Instantiate new instance of our class
        HTTPReq getRequest = new HTTPReq();

        //Perform the doInBackground method, passing in our url
        try {
            result = getRequest.execute(myUrl).get();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // globally
        TextView myAwesomeTextView = (TextView) findViewById(R.id.myAwesomeTextView);

        //in your OnCreate() method
        myAwesomeTextView.setText(result);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    public static String getMD5EncryptedString(String encTarget) {
        MessageDigest mdEnc = null;
        try {
            mdEnc = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            System.out.println("Exception while encrypting to md5");
            e.printStackTrace();
        } // Encryption algorithm
        mdEnc.update(encTarget.getBytes(), 0, encTarget.length());
        String md5 = new BigInteger(1, mdEnc.digest()).toString(16);
        while (md5.length() < 32) {
            md5 = "0" + md5;
        }
        return md5;
    }

    private boolean checkSuExists() {
        Process a = null;
        try {
            a = Runtime.getRuntime().exec(new String[]
                    {"/system /xbin/which", "su"});
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(a.getInputStream()));
            String line = in.readLine();
            a.destroy();
            return line != null;
        } catch (Exception e) {
            if (a != null) {
                a.destroy();
            }
            return false;
        }
    }

    private String[] binaryPaths = {
            "/data/local/",
            "/data/local/bin/",
            "/data/local/xbin/",
            "/sbin/",
            "/su/bin/",
            "/system/bin/",
            "/system/bin/.ext/",
            "/system/bin/failsafe/",
            "/system/sd/xbin/",
            "/system/usr/we-need-root/",
            "/system/xbin/",
            "/system/app/Superuser.apk",
            "/cache",
            "/data",
            "/dev"
    };

    private boolean checkForBinary(String filename) {
        for (String path : binaryPaths) {
            File f = new File(path, filename);
            boolean fileExists = f.exists();
            if (fileExists) {
                return true;
            }
        }
        return false;
    }

    private boolean checkForBinary2(String filename) {
        for (String path : binaryPaths) {
            File f = new File(path, filename);
            boolean fileExists = f.exists();
            if (fileExists) {
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean onSupportNavigateUp() {
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment);
        return NavigationUI.navigateUp(navController, mAppBarConfiguration)
                || super.onSupportNavigateUp();
    }
}
