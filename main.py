import time
import sys

from selenium import webdriver
from settings import WEB_SITE, WEB_DRIVER
from service import make_login, get_readable_data, download_bankslip_not_payed


def main():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(WEB_DRIVER, options=chrome_options)  # Could be Firefox as well

    driver.get(WEB_SITE)
    time.sleep(0.5)
    try:
        make_login(driver)
        df = get_readable_data(driver)
        download_bankslip_not_payed(driver, df)
    except:
        print('Something Went Wrong')
        driver.quit()
        sys.exit()

    time.sleep(3)
    driver.quit()
    sys.exit()


main()
