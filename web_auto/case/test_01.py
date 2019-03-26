import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

    # def setUp(self):  # 会在每一条用例执行之前，先执行一次
    #     print("先打开浏览器")

    @classmethod
    def setUpClass(cls):
        print("用例前，只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("用例后，只执行一次")

    # def tearDown(self):  # 会在每一条用例执行之后，调用一次
    #     print("关闭浏览器")

    def test1(self):  ## test method names begin 'test*'
        '''用例的描述哈哈'''
        print("1111111")
        self.assertEqual((1 + 2), 3)  # 添加断言，判断用例是否通过
        self.assertEqual(0 + 1, 1)


    def test2(self):
        print("22222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':  #在当前脚本运行，使用unittest.main()的方法，这个可用可不用
    unittest.main()