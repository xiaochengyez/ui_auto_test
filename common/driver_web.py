# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2019/10/14  10:19 
# 文件  driver_configure
from selenium import webdriver



class DriverWeb:
    def get_chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--args --disable-web-security --user-data-dir")#跨域
        self._driver = webdriver.Chrome(options=chrome_options)
        #self.driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)
        self._driver.get("https://www.baidu.com")
        return self._driver
