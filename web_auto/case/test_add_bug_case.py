from selenium import webdriver
import unittest
from pages.login_page import LoginPage
import time
from  pages.add_bug_page import ZentaoBug

my="http://10.10.10.23/zentao/my/"
class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bug = ZentaoBug(cls.driver)
        ad = LoginPage(cls.driver)
        ad.login()

    def setUp(self):
        self.driver.get(my)

    def test_add_bug_01(self):

        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交Bug" + timestr
        self.bug.add_bg(title)
        result = self.bug.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()