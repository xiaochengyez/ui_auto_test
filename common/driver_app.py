# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/5/8  13:28 
# 文件  driver_app
from appium import webdriver


class DriverApp:
    _package = ""
    _activity = ""
    def app_start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "aa"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(self._package, self._activity)

        return self._driver