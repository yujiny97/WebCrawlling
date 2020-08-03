# WebCrawlling

#데이터 전처리를 위한 코드들  

##경로별 파일들 설명  

```
/pythoncode/FileCount
```  

movefile.py: 이미지 개수가 100개가 되지 않아 폴더 자체를 옮겨주는 코드  

filecounter.py: 각 폴더 클래스들에 들어있는 파일들을 모두 카운트해서 데이터개수라는 엑셀에 적어주는 코드  

testandtrain.py: train 데이터와 test 데이터를 7:3 비율로 나눠서 저장해주는 코드  

classname.py: class들의 이름을 {"클래스이름","클래스이름2"} 형태로 출력함  


-> 코드의 경로는 /로 표시해주어야함  

```
/python
```
name: google, naver, insta  
excel_name.py : 엑셀에서 값을 읽어와서 name 사이트에서 이미지 웹크롤링 하는 코드 (엑셀에서 D#,E#,G# 값을 불러와서 크롤링 진행)  
D#: 검색할 이름 (예: 느타리버섯)  
E#: 현재까지 모았던 데이터의 개수 (500를 최대값으로 데이터를 모았음)  
G#: 식용인지 아닌지 여부를 폴더 앞에 붙여주기 위함  

webfunction_name.py: 웹크롤링 코드로 excel_name.py에서 호출하는 함수가 작성되어있음  
```
urllib.request.urlretrieve(img, forfile + searchterm + 'googlev1_' + str(counter) + '.jpg')  
```
이부분의 경로가 사진이 저장될 경로이고

```   
 forfile='C:/Python/사진/train/'+poi+'_'+searchterm+'/'
 DIR='C:/Python/사진/train/'+poi+'_'+searchterm
```
forfile은 저장될 사진의 파일경로, DIR이 사진을 저장할 디렉토리 경로이다.
