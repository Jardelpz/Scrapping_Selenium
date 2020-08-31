import pandas

from settings import USER_NAME, USER_PASSWORD


def make_login(driver) -> None:
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
    boleto = driver.find_element_by_xpath('//*[@id="quadroTransparente"]/table[2]/tbody/tr[{}]/td[10]/a[2]'.format(index+2))
    boleto.click()


def get_index_not_paymed(df):
    list_of_values = list(df['Valor Pago'])
    # lis_of_payment = {list_due_date[i]: list_of_values[i] for i in range(0, len(list_due_date))} # Export to json, csv something like that

    for value in list_of_values:
        if not value:
            return list_of_values.index(value)

