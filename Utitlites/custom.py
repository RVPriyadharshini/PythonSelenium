import time
import traceback
from TestData import data
from TestLocators import locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_Clipping


class CustomMethod:

    def __init__(self, driver):
        self.driver = driver

    def TakeScreenshot(self, ImageName):
        self.driver.get_screenshot_as_file("Screenshot/Screenshot_Clipping/" + ImageName + ".png")
