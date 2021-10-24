import random
import time
from selenium import webdriver

with webdriver.Chrome() as driver:
    b = random.randint(-180, 180)
    driver.get('https://www.baidu.com/')
    print(b)
    # 随机填写内容
    date = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input'
    ).send_keys(b)
    time.sleep(1)

    # 触发点击事件
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[2]/input').click(
        )
    print(driver.title)
    time.sleep(5)
    print("递交分支到main1tef")
    print("递交")
    driver.close()