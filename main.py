import sys

from selenium import webdriver
from settings import WEB_SITE, WEB_DRIVER
from service import make_login, get_readable_data, download_bankslip_not_payed, prepare_setup
from send_email import send_email


def main():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(WEB_DRIVER, options=chrome_options)  # Could be Firefox as well

    driver.get(WEB_SITE)

    try:
        if prepare_setup():
            make_login(driver)
            df = get_readable_data(driver)

            download_bankslip_not_payed(driver, df)
            send_email()

    except:
        print('Something Went Wrong')
        driver.quit()
        sys.exit()

    driver.quit()
    sys.exit()


main()
