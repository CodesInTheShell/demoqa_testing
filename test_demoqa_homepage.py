import unittest
from selenium import webdriver


###############################
#      CODES IN THE SHELL     #
###############################

class DemoqaHomeTest(unittest.TestCase):
    """ Test www.demoqa.com home page """
        
    def setUp(self):
        """ Use firefox browser"""
        self.driver = webdriver.Firefox()

    def test_home_page(self):
        """Testing www.demoqa.com homepage"""
        driver = self.driver
        driver.get("http://demoqa.com/")
        self.assertIn ("Demoqa", driver.title)

    def tearDown(self):
        """Close firefox browser"""
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
        
        

    
