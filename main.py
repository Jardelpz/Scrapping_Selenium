import sys
import os

from selenium import webdriver
from settings import WEB_SITE, WEB_DRIVER
from service import make_login, get_readable_data, download_bankslip_not_payed, prepare_setup
from send_email import send_email


def main():
    workdir = os.getcwd()
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": workdir,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    try:
        if prepare_setup():
            driver = webdriver.Chrome(WEB_DRIVER, options=chrome_options)
            driver.get(WEB_SITE)
            make_login(driver)
            df = get_readable_data(driver)

            download_bankslip_not_payed(driver, df, workdir)

            send_email(workdir)

    except:
        print('Something Went Wrong')
        driver.quit()
        sys.exit()

    driver.quit()
    sys.exit()


if __name__ == '__main__':
    main()
