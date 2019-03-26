from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
from common.read_excel import ExcelUtil
import os


'''
1.输入luomiao/nuanguang123456,点登陆
2.输入luomiao，不输入密码,点登陆
3.输入错误的用户名、nuanguang123456，点登陆

'''

# testdates=[
#     {"user":"luomiao","pswd":"nuanguang123456","expect":"罗苗"},
#     {"user":"luomiao","pswd":"","expect":""},
#     {"user":"luo","pswd":"nuanguang123456","expect":""}
#
# ]

propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath=os.path.join(propath,"common","datas.xlsx")
print(filepath)


data=ExcelUtil(filepath)
testdates = data.dic_data()
print(testdates)

@ddt.ddt
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

    def login_case(self,user,pswd,expect):
        self.loginp.login(user,pswd)
        # self.loginp.input_user(user)
        # self.loginp.input_pswd(pswd)
        # self.loginp.click_login_button()
        # result=self.loginp.get_login_name()
        result = self.loginp.get_login_name()
        self.assertTrue(result==expect)#断言


    @ddt.data(*testdates)
    def test_01(self,data):
        print("----------测试开始---------")
        print("测试数据：%s" % data)
        self.login_case(data["user"],data["pswd"],data["expect"])
        print("----------测试结束----------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()