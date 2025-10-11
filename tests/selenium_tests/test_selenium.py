import threading
import unittest

from flask_app import app
from selenium import webdriver


class TestFlaskSelenium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = threading.Thread(target=app.run, kwargs={'port': 5001})
        cls.server.daemon = True
        cls.server.start()
        cls.driver = webdriver.Chrome()  # Or use Firefox, Edge, etc.

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_homepage(self):
        self.driver.get('http://localhost:5001/')
        self.assertIn("Home", self.driver.page_source)


if __name__ == "__main__":
    unittest.main()
