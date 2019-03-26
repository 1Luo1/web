from  selenium.webdriver.support.wait import WebDriverWait
from  selenium import  webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout=5
        self.t=1

    def findElementNew(self,locator):
        '''定位元素，返回元素对象，没定位到，返回Timeout异常'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型：loc=('id','value')")
        else:
            print("正在定位元素信息：定位方式——>%s,value值——>%s")
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))#driver此处不用传
            return ele



    def findElement(self,locator):#传入参数,loctor=("by","value"),一个是定位方式，是通过id还是name之类的，一个是id变量名称
        ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))#*是将元组或list分开传入
        return ele

    def sendKeys(self,locator,text):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def clk(self,locator):
        ele=self.findElement(locator)
        ele.click()

    def clr(self,locator):
        ele=self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):#判断元素是否被选中，返回Bool值
        ele=self.findElement(locator)
        r=ele.is_selected()
        return r


    def isElementExit1(self,locator):#判断元素是否存在
        try:
            ele=self.findElement(locator)
            return True
        except:
            return False

    def isElementsExit2(self,locator):#判断元素是否存在,如果没有定位到就会返回空的，不会抛异常
        eles=self.findElement(locator)#定位到的元素会通过列表
        n=len(eles)
        if n==0:
            return False
        elif n==1:
            return True
        else:
            print("定位到元素的个数：%S"%n)
            return True


    def is_title(self,_title):
        '''返回bool值'''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''返回bool值'''
        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        try:
             result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
             return result
        except:
            return False

    def get_text(self,locator):
        '''获取文本'''
        try:
            t=self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回‘’ ")
            return ""

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele=self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引的第几个，从0开始，默认选第一个'''
        element=self.findElement(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element=self.findElement(locator)
        Select(element).select_by_index(value)

    def select_by_text(self,locator,text):
        '''通过文本值定位'''
        element=self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target = driver.find_element(locator)
        js = "arguments[0].scrollIntoView();"  # 聚焦这个元素，就是光标放到这个位置的意思
        self.driver.execute_script(js, target)


    def js_scroll_top(self, locator):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"  # 0,0:顶部
        driver.execute_script(js)

    def js_scroll_end(self, locator):
        '''滚动到底部'''
        js="window.scrollTo(0,document.body.scrollHeight)"#0：横坐标，在最左边；document。body。scrollHeight：js里面的函数，计算高度
        driver.execute_script(js)


if __name__=="__main__":
    driver = webdriver.Firefox()
    driver.get("http://10.10.10.23/zentao/user-login-L3plbnRhby9idWctYnJvd3NlLmh0bWw=.html")
    zentao=Base(driver)#先实例化

    # loc1=(By.ID,"account")#然后定位   # By.ID = "id"
    loc1=("id","account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")

    zentao.move_to_element()
    
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"


    # zentao.sendKeys(loc1,"luomiao")
    # zentao.sendKeys(loc2,"nuanguang123456")
    # zentao.clk(loc3)
    # zentao.clr()
