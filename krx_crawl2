## macro for reading excel file in KRX web

import pandas as pd # pandas for data frame work(handling)
import os # romove excel 
from selenium import webdriver # data chrolling
from time import sleep # time hold
# Bring function from selenium webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 데이터 스크랩
from bs4 import BeautifulSoup    

# workspace 폴더에 chromedriver다운받아 설치 -> driver에 넣기 
driver = webdriver.Chrome('/Users/daeunjung/Desktop/workspace/chrome/chromedriver')

# 매크로 돌리고자 하는 웹주소 가져오기
driver.get("http://short.krx.co.kr/contents/SRT/02/02010100/SRT02010100.jsp")
data_date = []
data_code = []
data_comp = []
data_volu = []
data_intv = []
data_pric = []
data_intp = []

    for years in range(15,17) :

    # 첫번째 날짜 칸 클리어 & 값 넣어주기 
    driver.find_element_by_xpath('//*[@id="strt_dda87ff679a2f3e71d9181a67b7542122c"]').clear()
    driver.find_element_by_xpath('//*[@id="strt_dda87ff679a2f3e71d9181a67b7542122c"]').send_keys('20'+str(years)+'0101') 
    # 두번째 날짜 칸 클리어 & 값 넣어주기 
    driver.find_element_by_xpath('//*[@id="end_dda87ff679a2f3e71d9181a67b7542122c"]').clear()
    driver.find_element_by_xpath('//*[@id="end_dda87ff679a2f3e71d9181a67b7542122c"]').send_keys('20'+str(years+1)+'0101')
    
    # 팝업 없어지게 확인 눌러줌 
    # driver.find_element_by_xpath("").click() 

    # 조회 클릭 (disabled 강제로 눌러주기)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btnidc4ca4238a0b923820dcc509a6f75849b"]'))
    )
    element.click()
    # 엑셀 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="e4da3b7fbbce2345d7772b0674a318d5"]/button'))
    )
    element.click()

    sleep(3)

    # download된 excel data 읽기 : pandas 통해서 읽고 -> data에 넣음
    data = pd.read_excel('/Users/daeunjung/Downloads/data.xls')

        for idx in range(len(data)) :
            data_date.append(data['일자'][len(data)-idx-1])
            data_code.append(data['종목코드'][len(data)-idx-1])
            data_comp.append(data['종목명'][len(data)-idx-1])
            data_volu.append(data['공매도거래량'][len(data)-idx-1])
            data_intv.append(data['공매도잔고수량'][len(data)-idx-1])
            data_pric.append(data['공매도거래대금'][len(data)-idx-1])
            data_intp.append(data['공매도잔고금액'][len(data)-idx-1])

    # 다운받은 data는 삭제 
    os.remove('/Users/daeunjung/Downloads/data.xls')

df = pd.DataFrame({
        '일자' : data_date,
        '종목코드' : data_code,
        '종목명' : data_comp,
        '공매도거래량' : data_volu,
        '공매도잔고수량' : data_intv,
        '공매도거래대금' : data_pric,
        '공매도잔고금액' : data_intp}) 

# short.xls로 데이터 저장
writer = pd.ExcelWriter('short.xls', engine='xlsxwriter') 
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

# 드라이버 끄기 
driver.quit()









