#coding:utf-8
from selenium import webdriver
from common.base import Base
import time
from pages.login_page import LoginPage


class ZentaoBug(Base):#继承Base里面的方法

    #定位添加bug
    loc4=("link text","测试")#测试目录按钮
    loc5=("link text","Bug")#bug目录按钮
    loc6=("xpath",".//*[@id='createActionMenu']/a") #添加Bug按钮

    loc13=("xpath",".//*[@id='module_chosen']/a") #选择所属模块
    loc12 = ("xpath", ".//*[@id='module_chosen']/div/ul/li[1]")  # 所属模块

    loc7=("xpath",".//*[@id='openedBuild_chosen']/ul")#影响版本输入框
    loc8=("xpath",".//*[@id='openedBuild_chosen']/div/ul/li[1]")#选择一个影响版本号
    loc9=("id","title")#输入标题框


    #需要先切换iframe
    loc10=("class name","article-content")#定位富文本，用定位到body就行
    loc11=("id","submit")#保存按钮

    #新增的列表
    loc_newbug=("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def add_bg(self,title="测试提交Bug"):
        self.clk(self.loc4)
        self.clk(self.loc5)
        self.clk(self.loc6)
        self.clk(self.loc13)
        self.clk(self.loc12)
        self.clk(self.loc7)
        self.clk(self.loc8)
        self.sendKeys(self.loc9,title)

        #输入body正文
        frame=self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)

        body='''[测试步骤]XXXX
        [测试结果]XXXXX
        [期望结果]XXXXX'''

        self.sendKeys(self.loc10,body)
        self.driver.switch_to.default_content()# 返回最上层
        self.clk(self.loc11)

    def is_add_bug_sucess(self,_text):
        return self.is_text_in_element(self.loc_newbug,_text)


if __name__=="__main__":
    driver=webdriver.Firefox()
    bug = ZentaoBug(driver)
    
    ad=LoginPage(driver)
    ad.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title="测试提交Bug"+timestr

    bug.add_bg(title)
    result=bug.is_add_bug_sucess(title)
    print(result)













