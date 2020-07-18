import errno
from selenium import webdriver
import os
import urllib.request
import threading
import time
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys

#출처:https://github.com/jun7867/Web_Image_Crawling/blob/master/naver_crawling.py
class Alarm(threading.Thread):
    def __init__(self, timeout):
        threading.Thread.__init__(self)
        self.timeout = timeout
        self.setDaemon(True)

    def run(self):
        time.sleep(self.timeout)
        raise Exception("end of time")

def getpicture(searchterm,poi,cnt):
    forfile='C:/Python/사진/'+poi+'_'+searchterm+'/'
    DIR='C:/Python/사진/'+poi+'_'+searchterm
    try:
        if not (os.path.isdir(DIR)):
            os.makedirs(os.path.join(DIR))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="+searchterm#+"&oquery="+searchterm
    # chrom webdriver 사용하여 브라우저를 가져온다.
    browser = webdriver.Chrome(r'C:\Python\chromedriver')
    browser.get(url)

    # User-Agent를 통해 봇이 아닌 유저정보라는 것을 위해 사용
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    # 이미지 카운트 (이미지 저장할 때 사용하기 위해서)
    counter = 0#os.walk(forfile).__next__().__sizeof__()
    print(counter)
    succounter = 0

    # 페이지 스크롤 다운
    body=browser.find_element_by_css_selector('body')
    for i in range(3):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1) #delay 주기

    #이미지 링크 수집
    imgs= browser.find_elements_by_css_selector("img._img")
    result=[]
    for img in tqdm(imgs):
        if 'http' in img.get_attribute('src'):
            result.append(img.get_attribute('src'))

    browser.close() # 크롬창 자동 종료
    print("수집 완료")

    #다운로드
    for index, link in tqdm(enumerate(result)): #tqdm은 작업현황을 알려줌.
        #alarm = Alarm(10)
        #alarm.run()
        try:
            start=link.rfind('.') #뒤쪽부터 검사
            end=link.rfind('&')
            filetype=link[start:end] # .jpg , .png 같은게 뽑힘
            #'C:/Python/사진/'+poi+'_'+searchterm+'/'
            urllib.request.urlretrieve(link,forfile + searchterm + 'Naver_' + str(index) + '.'+filetype)
        except Exception:
            continue
        #finally:
            #del alarm
