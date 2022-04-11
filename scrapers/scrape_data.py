from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import os

CHROME_DRIVER_PATH = 'C:/Users/Eito Miyamura/Documents/My Programs/chromedriver.exe'

def get_data(pair, save=False, chromedriver_path=os.environ.get('CHROME_DRIVER_PATH')):
    driver = webdriver.Chrome(
        executable_path=chromedriver_path
    )

    driver.get(f'https://www.dextools.io/app/uniswap/pair-explorer/{pair}')


    all_results = []  # list for all rows
    
    for page in tqdm(range(35)):

        # print('--- page:', page, '---')
        
        # get table
        tableElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ngx-datatable'))
        )
        # scroll into table view
        driver.execute_script("arguments[0].scrollIntoView();", tableElement)
    
        # scrolling through the table body to the bottom
        tableBodyelement = tableElement.find_element_by_tag_name('datatable-body-cell')
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", tableBodyelement)
    
        rowWrapper = tableElement.find_elements_by_tag_name('datatable-row-wrapper')
        rowNum = 0
        for row in rowWrapper:
            cells = row.find_elements_by_tag_name('datatable-body-cell')
            date = cells[0].text
            type = cells[1].text
            price_usd = cells[2].text
            price_eth = cells[3].text
            amount_cuminu = cells[4].text
            total_eth = cells[5].text
            maker = cells[6].find_element_by_tag_name('a').get_attribute('href')
            # print(f"page {page} row {rowNum}",date, type, price_usd, price_eth, amount_cuminu, total_eth, maker)
            # print('----')
            rowNum += 1
            # add row to list
            all_results.append( [date, type, price_usd, price_eth, amount_cuminu, total_eth, maker] )
    
        try:
            next_page = driver.find_element(by=By.XPATH, value='//a[@aria-label="go to next page"]')
            next_page.click()
            time.sleep(1)
        except Exception as ex:
            print("Finished.")
            break
    
    # after loop convert to DataFrame and write it to excel
    if save:
        import pandas as pd        
        df = pd.DataFrame(all_results, columns=['date', 'type', 'price_usd', 'price_eth', 'amount_cuminu', 'total_eth', 'maker'])
        df.to_excel(f'{save}.xlsx')

def get_wallet_analytics(pair, wallet, save=False, chromedriver_path=os.environ.get('CHROME_DRIVER_PATH')):
    driver = webdriver.Chrome(
        executable_path=chromedriver_path
    )

    driver.get(f'https://www.dextools.io/app/uniswap/pair-explorer/')


    all_results = []  # list for all rows
    
    for page in range(35):

        # print('--- page:', page, '---')
        
        # get table
        tableElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ngx-datatable'))
        )
        # scroll into table view
        driver.execute_script("arguments[0].scrollIntoView();", tableElement)
    
        # scrolling through the table body to the bottom
        tableBodyelement = tableElement.find_element_by_tag_name('datatable-body-cell')
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", tableBodyelement)
    
        rowWrapper = tableElement.find_elements_by_tag_name('datatable-row-wrapper')
        rowNum = 0
        for row in rowWrapper:
            cells = row.find_elements_by_tag_name('datatable-body-cell')
            date = cells[0].text
            type = cells[1].text
            price_usd = cells[2].text
            price_eth = cells[3].text
            amount_cuminu = cells[4].text
            total_eth = cells[5].text
            maker = cells[6].find_element_by_tag_name('a').get_attribute('href')
            print(f"page {page} row {rowNum}",date, type, price_usd, price_eth, amount_cuminu, total_eth, maker)
            print('----')
            rowNum += 1
            # add row to list
            all_results.append( [date, type, price_usd, price_eth, amount_cuminu, total_eth, maker] )
    
        try:
            next_page = driver.find_element(by=By.XPATH, value='//a[@aria-label="go to next page"]')
            next_page.click()
            time.sleep(1)
        except Exception as ex:
            print("Finished.")
            break
    
    # after loop convert to DataFrame and write it to excel
    if save:
        import pandas as pd        
        df = pd.DataFrame(all_results, columns=['date', 'type', 'price_usd', 'price_eth', 'amount_cuminu', 'total_eth', 'maker'])
        df.to_excel(f'{save}.xlsx')

if __name__=="__main__": 
    # get_wallet_analytics
    get_data(None)
