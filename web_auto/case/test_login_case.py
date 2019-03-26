from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url


'''
1.输入luomiao/nuanguang123456,点登陆
2.输入luomiao，不输入密码,点登陆
3.输入错误的用户名、nuanguang123456，点登陆
4、点击忘记密码
'''


class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        '''输入luomiao/nuanguang123456,点登陆'''
        self.loginp.input_user("luomiao")
        self.loginp.input_pswd("nuanguang123456")
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="罗苗")#断言

    def test_02(self):
        '''输入luomiao，不输入密码,点登陆'''
        self.loginp.input_user("luomiao")
        self.loginp.click_login_button()

        result=self.loginp.get_login_name()
        self.assertTrue(result=="")#断言

    def test_03(self):
        '''输入错误的用户名、nuanguang123456，点登陆'''
        self.loginp.input_user("luo")
        self.loginp.input_pswd("nuanguang123456")
        self.loginp.click_login_button()

        result=self.loginp.get_login_name()
        self.assertTrue(result=="")#断言

    def test_04(self):
        '''点击忘记密码'''
        self.loginp.click_forget_pswd()
        result=self.loginp.is_forget_pages_rerfesh_exit()
        self.assertTrue(result) # 断言

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()