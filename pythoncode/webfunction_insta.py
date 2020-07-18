import errno
from selenium import webdriver
import os
from urllib.request import urlopen
import threading
import time
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

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

    baseurl = "https://www.instagram.com/explore/tags/"#+searchterm
    url = baseurl + quote_plus(searchterm)

    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html)

    insta = soup.select('.v1Nh3.kIKUG._bz0w')

    n = 1
    for i in insta:
        try:
            print('https://www.instagram.com' + i.a['href'])
            imgUrl = i.select_one('.KL4Bh').img['src']
            with urlopen(imgUrl) as f:
                with open(forfile + searchterm + 'INSTA_' + str(n) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
            n += 1
            print(imgUrl)
            print()
        except Exception:
            continue

    driver.close()
