#!/usr/bin/python3


def isElementExist(self, element):
    flag = True
    driver = self.driver
    try:
        driver.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag


class aliPayClass(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        # desired_caps['platformVersion']='8.0.0'
        # desired_caps['deviceName']='73EBB18730214045'
        # desired_caps['platfromVersion']='7.1.2'#红米5A
        # desired_caps['deviceName']='79bad8ec7d94'
        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element_by_xpath(
            "//android.widget.TextView[@text='朋友']").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        time.sleep(1)
        # f0 = open('D:\\zxtest\\cpay.txt', 'r')#备注
        # z = len(open('D:\\zxtest\\cpay.txt', 'r').readlines())
        # f1=open('D:\\zxtest\\zhifubao.txt', 'r')#二维码
        f1 = open('D:\\zxtest\\cpayzhifubao.txt', 'r')  # 二维码
        while True:
            # beizhu = f0.readline()
            erweima = f1.readline()
            print "erweima:%s" % erweima
            if erweima == '':
                break
            time.sleep(2)
            driver.find_element_by_xpath(
                "//android.widget.EditText[@index='0']").send_keys(erweima)
            time.sleep(2)
            driver.find_element_by_xpath(
                "//android.widget.TextView[@text='发送']").click()
            time.sleep(2)
            lianjies = driver.find_elements_by_id(
                "com.alipay.mobile.chatapp:id/chat_msg_text")
            time.sleep(2)
            lianjies[-1].click()
            time.sleep(2)
            element01 = "//android.widget.Button[@text='确认转账']"
            if isElementExist(self, element01):
                pass
            else:
                time.sleep(1)
                lianjies[-1].click()
                time.sleep(2)
            time.sleep(2)
            driver.find_element_by_xpath(
                "//android.widget.Button[@text='确认转账']").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//android.widget.TextView[@text='立即付款']").click()
            time.sleep(1)
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            driver.tap([(140*x/1080, 1500*y/1920)], 0)
            driver.tap([(200*x/1080, 1500*y/1920)], 0)
            driver.tap([(800*x/1080, 1500*y/1920)], 0)
            driver.tap([(800*x/1080, 1500*y/1920)], 0)
            driver.tap([(500*x/1080, 1680*y/1920)], 0)
            driver.tap([(500*x/1080, 1680*y/1920)], 0)
            time.sleep(2)

            element = "//android.widget.TextView[@text='开通指纹支付']"
            if isElementExist(self, element):
                driver.find_element_by_xpath(
                    "//android.widget.TextView[@text='取消']").click()
                time.sleep(3)
            else:
                pass
            time.sleep(2)
            driver.find_element_by_xpath(
                "//android.widget.TextView[@text='完成']").click()
            time.sleep(1)

        f1.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
