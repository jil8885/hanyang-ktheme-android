package com.kakao.talk.theme.hanyang.bibi

import android.app.Activity
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.view.WindowManager
import android.widget.Button

open class MainActivity : Activity() {

    companion object {
        private const val KAKAOTALK_SETTINGS_THEME_URI = "kakaotalk://settings/theme/"
        private const val MARKET_URI = "market://details?id="
        const val KAKAOTALK_PACKAGE_NAME = "com.kakao.talk"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_activity)

        window?.apply {
            try {
                addFlags(WindowManager.LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
                statusBarColor = this@MainActivity.resources.getColor(R.color.statusBarColor, null)
            } catch (ignored: Throwable) {
            }
        }

        val applyButton = findViewById<Button>(R.id.apply)
        applyButton.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW)
            intent.data = Uri.parse(KAKAOTALK_SETTINGS_THEME_URI + packageName)
            startActivity(intent)
            finish()
        }

        val marketButton = findViewById<Button>(R.id.market)
        marketButton.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse(MARKET_URI + KAKAOTALK_PACKAGE_NAME))
            startActivity(intent)
            finish()
        }

        if (isKakaoTalkInstalled()) {
            applyButton.visibility = View.VISIBLE
            marketButton.visibility = View.GONE
        } else {
            applyButton.visibility = View.GONE
            marketButton.visibility = View.VISIBLE
        }
    }

    open fun isKakaoTalkInstalled(): Boolean {
        return try {
            packageManager.getPackageInfo(KAKAOTALK_PACKAGE_NAME, 0)
            true
        } catch (e: PackageManager.NameNotFoundException) {
            false
        }
    }
}
