import pandas as pd
from firestoreUploader import uploadFirestore, deleteDoc
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from datetime import date
'''
eventsTitle
eventsDetail
location
organizer
points
type
startTime
endTime
typeInt
'''

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(
    "/Users/Howard/documents/chromedriver/chromedriver", options=options)
# driver = webdriver.Chrome("chromedriver", options=options)
# driver.get('https://pass.pccu.edu.tw/bin/home.php')
driver.get('https://pass.pccu.edu.tw/files/11-1191-6113.php?Lang=zh-tw')
driver.find_element_by_partial_link_text(
    '可認證於「全人學習護照」喔！歡迎同學利用課餘時間踴躍參與').click()
#可認證於「全人學習護照」喔！歡迎同學利用課餘時間踴躍參與！！
get_URL = ''
get_URL = driver.current_url
print(f'current url base: {get_URL}')
time.sleep(1)


DOMAIN = 'https://pass.pccu.edu.tw/'
URL = requests.get(get_URL).text
file_type = '.xlsx'
soup = BeautifulSoup(URL, 'lxml')
file_area = soup.find('div', class_='module module-ptattach pt_style1')
file_tr = file_area.find('span').findNext('span')
# file_tr = file_area.find('tr').findNext('tr')
print(file_tr.getText)
file_href = file_tr.find('a').get('href')
if file_type in file_href:
    print(file_href)
    with open(f'passport{file_type}', 'wb') as file:
        response = requests.get(DOMAIN + file_href)
        file.write(response.content)

#活動清單為covid後更新
source = pd.read_excel('passport.xlsx', header=1,
                       dtype=str, sheet_name='活動清單')  # 本學期活動清單 本週活動清單 活動清單
source.fillna('', inplace=True)
source.drop(columns=['項目', '群組', '群組.1', '類別.1', '項目.1', '活動類型', '補登者', '對象(1)', '對象(2)', '備註', '點數.1'], inplace=True, axis=1)
#修改前有的axis，可能未來會加回來因為covid!?: 場地容量, 人次, 人次(非系統), 點數小記,參與人次, 支應點數, 活動類型2, Unnamed: 42
today = date.today()
now = today.strftime("%Y-%m-%d")
print(now)
source = source.sort_values(['ID'], ascending=False)
source = source.loc[(source['活動名稱'] != '') & (source['ID'] != '') & (source['結束日期/時間'] > now)]

for index, row in source.iterrows():
    if '德' in row['類別']:
        row['類別'] = '德'
    elif '智' in row['類別']:
        row['類別'] = '智'
    elif '體' in row['類別']:
        row['類別'] = '體'
    elif '群' in row['類別']:
        row['類別'] = '群'
    elif '美' in row['類別']:
        row['類別'] = '美'
    else:
        row['類別'] = '無'

source.to_csv('modified.csv', index=False, encoding='utf-8-sig')


csv_source = pd.read_csv('modified.csv', dtype=str)
deleteDoc()
for index, row in csv_source.iterrows():
    try:
        collection = str(row['類別'])
        eventsTitle = str(row['活動名稱'])
        print(f'eventsTitle: {eventsTitle} added')
        eventsDetail = str(row['活動說明'])
        location = str(row['活動地點'])
        organizer = str(row['主辦單位'])
        points = int(row['點數'])
        type = str(row['類別'])
        startTime = row['開始日期/時間']
        endTime = row['結束日期/時間']
        typeInt = row['類別']
        uploadFirestore(collection=collection, eventsTitle=eventsTitle, eventsDetail=eventsDetail, location=location,
                        organizer=organizer, points=points, type=type, startTime=startTime, endTime=endTime, typeInt=typeInt)
    except Exception:
        pass

