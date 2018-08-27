#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'P7C0218105009504'
desired_caps['appPackage'] = 'com.netease.blockchain'
desired_caps['appActivity'] = 'com.netease.blockchain.business.main.MainActivity'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(10)

driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[1]').click()
sleep(2)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View').click()
sleep(2)
#点击挖矿
bb = driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.widget.Button")
#aa = driver.find_element_by_xpath('//android.widget.Button[@content-desc="自动挖宝中 点击加暴击率"]')

a =1
while a==1:
    bb.click()

