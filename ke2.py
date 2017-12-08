# coding:utf-8
from selenium import webdriver
import time
import unittest
class login(unittest.TestCase):
    @classmethod
    def setUp(self):
        print "打开博客园登录界面："
        self.driver = webdriver.Firefox()
        self.driver.get("https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
        self.driver.implicitly_wait(10)
    def tearDown(self):
        print "退出博客园"
        self.driver.quit()
    def test_login_successful(self):
        self.driver.find_element_by_id("input1").send_keys("ya")
        self.driver.find_element_by_id("input2").send_keys("111111@@")
        self.driver.find_element_by_id("signin").click()
        print "登录成功"
    def test_login_failed(self):
        self.driver.find_element_by_id("input1").send_keys("yangt")
        self.driver.find_element_by_id("input2").send_keys("123")
        self.driver.find_element_by_id("signin").click()
        print "登录失败"
if __name__ == "__main__":
    print main()
