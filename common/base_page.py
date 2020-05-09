# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/4/29  10:00
# 文件  base_page
from time import sleep

import yaml

from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.driver_app import DriverApp
from common.driver_web import DriverWeb


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [ ]
    _error_max = 10
    _error_count = 0
    _params={}

    def __init__(self, channel="web"):
        if channel == "app":
            self._driver = DriverApp().app_start()
        else:
            self._driver = DriverWeb().get_chrome_driver()

    #web
    def _find_by_css(self, by,locator):
        try:
            WebDriverWait(self._driver, 20).until(expected_conditions.visibility_of_element_located((by,locator)))
            return self._driver.find_element(by,locator)
        except Exception as e:
            raise e
    def page_source(self):
        self._driver.refresh()
        return self._driver.page_source

    def quit(self):
        self._driver.quit()

    def _find(self, locator, value: str = None):
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            self._error_count = 0
            return element
        except Exception as e:
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self._find(locator, value)
            raise e

    def _find_and_get_text(self, locator, value: str = None):
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            self._error_count = 0
            return element.text
        except Exception as e:
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self._find_and_get_text(locator, value)
            raise e

    def _get_toast(self):
        return self._find(By.XPATH, "//*[@class='android.widget.Toast']").text

    def _text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def _find_by_text(self, key):
        return self._find(self._text(key))

    def _steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    if step["by"] == "css":
                        element = self._find_by_css(By.CSS_SELECTOR,step["locator"])
                    elif step["by"] == "xpath":
                        element = self._find_by_text(step["locator"])
                    else:
                        element = self._find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str=step["value"]
                        for key in self._params.keys():
                            content=content.replace("{%s}" %key, self._params[key])
                        element.send_keys(content)