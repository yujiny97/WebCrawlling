import errno
import signal
from selenium import webdriver
import os
import urllib.request
import threading
import time
from functools import wraps


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

    url = "https://www.google.com/search?q="+searchterm+"&source=lnms&tbm=isch"
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

    # 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서)

    for _ in range(500):
        # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
        browser.execute_script("window.scrollBy(0,10000)")

    # div태그에서 class name이 rg_meta인 것을 찾아온다
    # div태그에서 class name이 rg_meta인 것을 찾아온다
    for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
        alarm = Alarm(10)
        try:
            counter = counter + 1
            print("Total Count:", counter)
            print("Succsessful Count:", succounter)
            # 이미지 url
            img = (x.get_attribute('src'))
            print("URL:", img)

            if img is None:
                continue
                # 이미지 확장자
                imgtype = 'jpg'

                # 구글 이미지를 읽고 저장한다, 저장될 위치
            urllib.request.urlretrieve(img, forfile + searchterm + '3_' + str(counter) + '.jpg')
        except Exception:
            continue
        finally:
            del alarm
            succounter = succounter + 1
            if succounter >= cnt:
                break;

    #print(succounter, "succesfully downloaded")
    browser.close()
