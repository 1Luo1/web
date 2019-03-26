#coding:utf-8
from selenium import webdriver
from common.base import Base
import time

login_url="http://10.10.10.23/zentao/user-login-L3plbnRhby9idWctYnJvd3NlLmh0bWw=.html"
class LoginPage(Base):#继承Base里面的方法
    #定位登录
    loc_user = ("id", "account")
    loc_pswd = ("css selector", "[name='password']")
    loc_button= ("xpath", "//*[@id='submit']")
    loc_keep_login=("id","keepLoginon")
    loc_forget_pswd=("xpath",".//*[@id='login-form']/form/table/tbody/tr[4]/td/a")
    loc_get_user=("xpath"," .//*[@id='userMenu']/a")
    loc_forget_pswd_page=("xpath","html/body/div[1]/div/div[2]/p/a")

    def input_user(self,text):
        self.sendKeys(self.loc_user,text)

    def input_pswd(self,text):
        self.sendKeys(self.loc_pswd,text)

    def click_keep_login(self):
        self.clk(self.loc_keep_login)

    def click_login_button(self):
        self.clk(self.loc_button)

    def click_forget_pswd(self):
        self.clk(self.loc_forget_pswd)
        time.sleep(3)


    def get_login_name(self):
        user=self.get_text(self.loc_get_user)
        return user

    def get_login_result(self,user):
        result=self.is_value_in_element(self.loc_get_user,user)
        return result

    def is_alert_exits(self):
        '''判断alert是不是存在'''
        a=self.is_alert()
        if  a:
            print(a)
            a.accept()

    def login(self,user="luomiao",pswd="nuanguang123456"):
        '''登录流程'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_pswd(pswd)
        self.click_login_button()


    def is_forget_pages_rerfesh_exit(self):
        '''判断忘记密码页面元素是否存在'''
        r=self.isElementExit1(self.loc_forget_pswd_page)
        return r







if __name__=="__main__":
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.login()
    # driver.get(login_url)
    # login_page.input_user("luomiao")
    # login_page.input_pswd("nuanguang123456")
    # login_page.click_keep_login()
    # login_page.click_login_button()

