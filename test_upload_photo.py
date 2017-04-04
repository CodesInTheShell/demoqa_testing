import unittest
from selenium import webdriver
import os



class UploadPhotoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_upload(self):
        driver = self.driver
        driver.get("http://demoqa.com/registration/")

        elem_profile_pic = driver.find_element_by_xpath('//*[@id="profile_pic_10"]')
        elem_profile_pic.send_keys(os.path.abspath('D:\\tooth.png'))

    def tearDown(self):
        self.driver.close()




