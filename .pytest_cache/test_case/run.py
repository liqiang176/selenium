from time import sleep
import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver')

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip
    def test_click(self):
        # 点击事件
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        e_click = self.driver.find_element(By.XPATH,'/html/body/form/input[3]')
        e_doubleclick = self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        e_rightclick = self.driver.find_element(By.XPATH,'/html/body/form/input[4]')
        # 创建action对象
        actions = ActionChains(self.driver)
        # 添加点击事件
        actions.click(e_click)
        # 添加双击事件
        actions.double_click(e_doubleclick)
        # 添加右键点击事件
        actions.context_click(e_rightclick)
        # 执行已添加的事件
        actions.perform()

    # @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com/")
        e_move = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        actions = ActionChains(self.driver)
        # 鼠标光标移动到某个元素上
        actions.move_to_element(e_move)
        actions.perform()
        sleep(2)

    # @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        e_drag = self.driver.find_element(By.XPATH,'//*[@id="dragger"]')
        e_drop = self.driver.find_element(By.XPATH,'/html/body/div[2]')
        actions = ActionChains(self.driver)
        # 将A元素拖拽到B元素上
        actions.drag_and_drop(e_drag, e_drop)
        # actions.click_and_hold(e_drag).release(e_drop).perform()  等同于拖拽操作
        # actions.click_and_hold(e_drag).move_to_element(e_drop).release().perform()  同上
        actions.perform()
        sleep(2)

    def test_keys(self):
        self.driver.get('https://sahitest.com/demo/label.htm')
        e_keys = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        e_keys.click()
        actions = ActionChains(self.driver)
        # pause 暂停1秒看操作
        actions.send_keys('username1').pause(1)
        actions.send_keys(Keys.SPACE).pause(1)  # 键盘上的空格
        actions.send_keys('tom').pause(1)
        actions.send_keys(Keys.BACK_SPACE).pause(1)  # 键盘上的退格操作
        actions.perform()
        sleep(2)


if __name__ == '__main__':
    pytest.main(['--clean-alluredir', "run.py", "-s",'--alluredir','../report/tmp'])
    os.system("allure serve ../report/tmp")