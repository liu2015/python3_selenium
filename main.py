import random
import time
from selenium import webdriver

# with webdriver.Chrome() as driver:
# win10 环境需要配置指向driver
with webdriver.Chrome("C://chromedriver.exe") as driver:

    b = random.randint(-180, 180)
    driver.get('http://47.114.139.188/')
    print(b)
    # 随机填写内容
    date = driver.find_element_by_xpath(
        '/html/body/div/div/form/div/div[3]/input').send_keys("18111111111")
    time.sleep(1)

    # 触发点击事件
    driver.find_element_by_xpath(
        '/html/body/div/div/form/div/div[4]/input').send_keys("123456")
    print(driver.title)

    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/form/div/button").click()
    time.sleep(5)
    print("递交分支到main1tef")
    print("递交")
    driver.close()