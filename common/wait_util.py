from selenium.common.exceptions import NoSuchElementException, TimeoutException
from common.base_util import BaseUtil
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil:

    def element_wait_visible(self, driver, locationType, locationExpresstion):
        """
         判断某个元素是否被添加到了dom里并且可见,如果是则返回该元素
        """
        try:
            loc = (locationType, locationExpresstion)
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
            return element
        except TimeoutException:
            print("元素查找超时：%s" % locationExpresstion)
        except:
            print("未知异常！")

    def element_wait_clickable(self, driver, locationType, locationExpresstion):
        """
        判断某个元素是否可见并且可点击，如果是则返回该元素
        """
        try:
            loc = (locationType, locationExpresstion)
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc))
            return element
        except TimeoutException:
            print("元素查找超时：%s" % locationExpresstion)
        except:
            print("未知异常！")
