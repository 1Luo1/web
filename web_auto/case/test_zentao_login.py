from  selenium import  webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#浏览器只打开一次
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://10.10.10.23/zentao/user-login-L3plbnRhby9idWctYnJvd3NlLmh0bWw=.html")

    def tearDown(self):#tearDown清空之后，截图就会为空，解决办法，可以把tearDown内容写在setUp里面
        self.is_alert_exist()
        self.driver.delete_all_cookies()#清空cookies，这样跑第二条登录的用例不会报错
        self.driver.refresh() #清空之后，刷新浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()#退出浏览器

    def get_username(self):#获取登录之后的页面用户名，如果登录失败则返回空值
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):#登录操作之后，判断下是否有弹窗，有alert的话，就点一下，把弹窗去掉
        try:
            time.sleep(3)
            a=self.driver.switch_to.alert
            at=a.text
            a.accept()
            return at
        except:
            pass


    def login(self,user,psw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()


    def testdenglu_01(self):#正确的用户名、密码，并且登录成功
        time.sleep(3)
        self.login("luomiao","nuanguang123456")
        time.sleep(3)
        #判断是否登录成功
        t=self.get_username()
        print("登录名称结果：%s"%t)
        self.assertTrue(t=="罗苗")

    def testdenglu_02(self):#错误的用户名、密码
        time.sleep(3)
        self.login("luomiao","")
        time.sleep(3)
        #判断是否登录成功
        t=self.get_username()
        print("登录失败，登录名称是空的：%s"%t)
        self.assertTrue(t=="")
        # self.assertTrue(1==3) #断言失败，添加截图


# if __name__=="__main__": #用脚本方式运行
#     unittest.main()
