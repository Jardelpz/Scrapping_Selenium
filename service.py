import pandas
import shutil
import os
import time

from datetime import datetime, date
from settings import USER_NAME, USER_PASSWORD, DOWNLOAD_PATH


def make_login(driver) -> None:
    time.sleep(0.5)
    user_name = driver.find_element_by_xpath('//*[@id="quadroTransparente"]/form/table/tbody/tr[1]/td[2]/input')
    user_name.send_keys(USER_NAME)
    user_password = driver.find_element_by_xpath('//*[@id="quadroTransparente"]/form/table/tbody/tr[2]/td[2]/input')
    user_password.send_keys(USER_PASSWORD)
    button_login = driver.find_element_by_xpath('//*[@id="quadroTransparente"]/form/table/tbody/tr[4]/td/p/input')
    button_login.click()
    go_to_payment_page(driver)


def go_to_payment_page(driver):
    driver.find_element_by_xpath('//*[@id="quadroTransparente"]/table/tbody/tr[3]/td/center/form/input[5]').click()
    return


def get_readable_data(driver):
    table = driver.find_element_by_xpath('//*[@id="quadroTransparente"]/table[2]')
    table_html = table.get_attribute('outerHTML')
    return pandas.read_html(table_html)[0]


def download_bankslip_not_payed(driver, df):
    index = get_index_not_paymed(df)
    boleto = driver.find_element_by_xpath(
        '//*[@id="quadroTransparente"]/table[2]/tbody/tr[{}]/td[10]/a[2]'.format(index + 2))
    boleto.click()
    move_pdf(df, driver)
    time.sleep(2)


def get_index_not_paymed(df):
    list_of_values = list(df['Valor Pago'])

    for value in list_of_values:
        if not value:
            return list_of_values.index(value)


def move_pdf(df, driver) -> None:
    docs_path = os.getcwd() + '/docs'
    bankslip_path = docs_path + '/boletos'
    image_path = docs_path + '/images'
    if not os.path.exists(bankslip_path) and not os.path.exists(image_path):
        os.mkdir(docs_path)
        os.mkdir(bankslip_path)
        os.mkdir(image_path)

    take_screenshot(image_path, driver)

    os.chdir(DOWNLOAD_PATH)
    try:
        for arq in os.listdir():
            if 'boleto' in arq and arq.split('.')[1] == 'pdf':
                if verify_existence(arq, bankslip_path):
                    rename = str(arq.split('.')[0]).replace(' ', '') + str(date.today()) + '.' + str(arq.split('.')[1])
                    shutil.move(DOWNLOAD_PATH + '/' + arq, bankslip_path + '/' + rename)

    except:
        print("Destination Path already exists")
    finally:
        build_csv(df, docs_path)


def take_screenshot(path, driver) -> None:
    os.chdir(path)
    table = driver.find_element_by_xpath('//*[@id="quadroTransparente"]/table[2]')
    table.screenshot('payment{}.png'.format(str(date.today())))


def build_csv(df, path) -> None:
    os.chdir(path)
    dictionary = {}
    for data in df:
        dictionary.update({str(data): list(df[data])})

    payment_csv = str(datetime.today()).replace(' ', 'T').replace(':', '-').split('.')[0] + '.csv'

    dt = build_data_frame(dictionary)
    dt.to_csv(payment_csv, index=False)


def build_data_frame(dictionary: dict):
    return pandas.DataFrame(dictionary)


def verify_existence(arq, path):
    os.chdir(path)
    return False if arq in os.listdir() else True
