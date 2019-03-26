import unittest
from common import HTMLTestRunner #导入框架模块

casePath="F:\web_auto\\case" #用例路径
rule="test*.py" #匹配规则，任意test开头的文件

# 运行所有的用例，用discover方法，需要两个参数，用例路径和匹配规则
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
# print(discover)  #打印下看看，能不能找到要跑的用例

reportPath="F:\\web_auto\\report\\"+"report.html"#报告路径
fp=open(reportPath,"wb")#报告内容写入指定路径,wb为写入

runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="V2.1测试报告",description="描述**",retry=1)#retry=1是让失败的重新跑
runner.run(discover)
fp.close()
