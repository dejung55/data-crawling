from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import os


driver = webdriver.Chrome('/Users/../Chrome/chromedriver')
driver.get('http://short.krx.co.kr/contents/SRT/02/02010100/SRT02010100.jsp')

dataLists = []
data_date,data_code,data_comp,data_volu,data_intv,data_pric,data_intp = [],[],[],[],[],[],[]


for years in range(18,18):
    
    driver.find_element_by_xpath('//*[@id="strt_dda87ff679a2f3e71d9181a67b7542122c"]').clear()
    try :
        sleep(0.1) 
        driver.switch_to_alert().accept()
    except NoAlertPresentException: sleep(0.1)
    except UnexpectedAlertPresentException: sleep(0.1)
    driver.find_element_by_xpath('//*[@id="end_dda87ff679a2f3e71d9181a67b7542122c"]').clear()
    driver.find_element_by_xpath('//*[@id="strt_dda87ff679a2f3e71d9181a67b7542122c"]').send_keys('20'+str(years)+'0101')
    driver.find_element_by_xpath('//*[@id="end_dda87ff679a2f3e71d9181a67b7542122c"]').send_keys('20'+str(years+1)+'0101')

    sleep(1.5)

    elem=driver.find_element_by_xpath('//*[@id="btnidc4ca4238a0b923820dcc509a6f75849b"]')
    sleep(0.2)
    actions = ActionChains(driver)
    actions.click(elem).perform()

    elem=driver.find_element_by_xpath('//*[@id="e4da3b7fbbce2345d7772b0674a318d5"]/button')
    sleep(0.2)
    actions = ActionChains(driver)
    actions.click(elem).perform()

    sleep(3)
    data = pd.read_excel('/Users/../Downloads/data.xls')


    for idx in range(len(data)) : 
        data_date.append(data['일자'][len(data)-idx-1])
        data_code.append(data['종목코드'][len(data)-idx-1])
        data_comp.append(data['종목명'][len(data)-idx-1])
        data_volu.append(data['공매도거래량'][len(data)-idx-1])
        data_intv.append(data['공매도잔고수량'][len(data)-idx-1])
        data_pric.append(data['공매도거래대금'][len(data)-idx-1])
        data_intp.append(data['공매도잔고금액'][len(data)-idx-1])

    os.remove('/Users/../Downloads/data.xls')

df = pd.DataFrame({'일자':data_date,
                   '종목코드':data_code,
                   '종목명':data_comp,
                   '공매도거래량':data_volu,
                   '공매도잔고수량':data_intv,
                   '공매도거래대금':data_pric,
                   '공매도잔고금액':data_intp})
writer = pd.ExcelWriter('Short.xlsx',engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

# driver.quit()


# '''
# dataLists = []
# for idx in range(len(data)) :
#     data_date = data['일자'][idx]
#     data_code = data['종목코드'][idx]
#     data_comp = data['종목명'][idx]
#     data_volu = data['공매도거래량'][idx]
#     data_intv = data['공매도잔고수량'][idx]
#     data_pric = data['공매도거래대금'][idx]
#     data_intp = data['공매도잔고금액'][idx]

#     data_col = [data_date,data_code,data_comp,data_volu,data_intv,data_pric,data_intp]
#     dataLists.append(data_col)

# for dataList in dataLists :
#     print(dataList)
# '''
