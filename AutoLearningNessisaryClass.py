from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulStoneSoup as bs
from time import sleep
import datetime

driver=webdriver.Chrome(ChromeDriverManager().install())
#페이지 이동
URL="https://sll.seoul.go.kr/"
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)
#로그인 및 강의 보기는 수동 입력
#로그인


driver.find_element(By.ID,"id").send_keys("goidokiato")
driver.find_element(By.ID,"pw").send_keys("dydtjs0911!")
driver.find_element(By.ID,"log.login").click()
#강의실 이동
lecture_url='https://www.safetyedu.net/safetyedu/efrt3000e'
driver.get(url=lecture_url)
in_butten_to_lecture=driver.find_elements(By.TAG_NAME,"button")
lecture_url_list=[]
for i in range(0,len(in_butten_to_lecture)):
    if(in_butten_to_lecture[i]=='강의실입장'):
        lecture_url_list.append(in_butten_to_lecture[i])


sleep(3)
lecture_list=driver.find_element(By.CLASS_NAME,'tbody').find_elements(By.TAG_NAME,'li')
for i in range(2,4):
    
    lecture_list=driver.find_element(By.CLASS_NAME,'tbody').find_elements(By.TAG_NAME,'li')
    lecture_list[i].find_elements(By.TAG_NAME,'dl')[-1].click()
    sleep(3)
    #탭이동
    driver.switch_to.window(driver.window_handles[-1])

    content=driver.find_element(By.TAG_NAME,'iframe')
    driver.switch_to.frame(content)
    while(driver.find_element(By.ID,"mobileLoading").get_attribute("style")!='display: none;'):
        sleep(1)
    content_time=driver.find_element(By.XPATH,'//*[@id="time"]')
    #현재 페이지, 라스트 페이지 불러오기
    # driver.find_element(By.ID,'nextBtn').click()
    now_page=driver.find_element(By.ID,'currentNum').text
    last_page=driver.find_element(By.ID,'totalNum').text
    #플레이 상태가 재생이 아니면 클릭
    while(driver.find_element(By.ID,'playBtn').get_attribute('class')!='controlSet controlBtn pause'):
        driver.find_element(By.ID,'playBtn').click()
        sleep(1)
    

    while(now_page<=last_page):
        print(now_page)
        sleep(4)
        #시간 체크해서 
        content_time=driver.find_element(By.XPATH,'//*[@id="time"]')
        now_page=driver.find_element(By.ID,'currentNum').text
        last_page=driver.find_element(By.ID,'totalNum').text
        while(content_time.text.find('/')==-1) :
            sleep(1)
        
        content_end_time=content_time.text.split('/')[1].replace(' ','')
        start_time_str=content_time.text.split('/')[0].replace(' ','')
        minute=int(content_end_time.split(':')[0].replace(' ',''))-int(start_time_str.split(':')[0].replace(' ',''))
        sec=int(content_end_time.split(':')[1].replace(' ',''))-int(start_time_str.split(':')[0].replace(' ',''))
        #종료 시간 체크
        end_time=datetime.datetime.now()+datetime.timedelta(minutes=minute)+datetime.timedelta(seconds=sec)
        print('first add time')
        print(minute*60+sec)
        #종료시간 까지 기다리기
        wait_time=minute*60+sec
        if(wait_time<0):
            wait_time=1
        sleep(wait_time)
        #지금이 종료시간보다 크면 클릭 수행
        while(end_time>datetime.datetime.now()):
            print("end time")
            print(end_time)
            #시간만큼 기다리기 추가
            sleep(1)
            pass
        #다음 버튼 클릭
        if(now_page !=last_page):
            driver.find_element(By.ID,'nextBtn').click()
        else:
            break
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

