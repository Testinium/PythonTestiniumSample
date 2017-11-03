from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
  

TESTINIUM_USER="canberk"
TESTINIUM_PASS="dc21f489b133c5cc058450eeb195be34"
Key =TESTINIUM_USER+':'+TESTINIUM_PASS
desired_cap = {
    'platform': "WIN8_1",
    'browserName': "firefox",
    'version': "47",
    'takesScreenshot':True,
    'recordsVideo':True,
    'screenResolution':'XGA',
    'key':Key
}
driver = webdriver.Remote(
   command_executor='http://hub.testinium.io/wd/hub',
   desired_capabilities=desired_cap)
  
# This is your test logic. You can add multiple tests here.
driver.implicitly_wait(10)
driver.get("http://www.amazon.com")
if not "Amazon" in driver.title:
    raise Exception("Unable to load amazon page!")
elem = driver.find_element_by_id("twotabsearchtextbox")
elem.send_keys("Superman Comics")
elem.submit()
print driver.title
  
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()