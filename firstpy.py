from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
import cv2 as cv

chrome_driver = 'chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

def capture_start():
    seat1_frame = driver.find_element_by_name("ifrmSeat")
    driver.switch_to_frame(seat1_frame)
    image = driver.find_element_by_id('imgCaptcha')
    for i in range(0, 1):
        image2 = image.screenshot_as_png
        with open("%d.png" % i, "wb") as file:
            file.write(image2)
            return image2
        # driver.find_element_by_class_name('refreshBtn').click()

driver.set_window_size(1400, 1200)
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')
driver.implicitly_wait(3)

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('bin2716') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('gksqls0823!') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)



#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21002720')
#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21004910')
driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21005689')
#driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=' + '21005562')


pag.click(979, 929)
time.sleep(0.2)
pag.click(1225, 430) #8월
time.sleep(0.2)
pag.click(1160, 491) #4일
time.sleep(0.2)
MB = True
while MB:
    resbutton = driver.find_element_by_xpath('//*[@id="productSide"]/div/div[2]/a[1]')
    if(resbutton.text=='예매하기'):
        print('예매')
        resbutton.click()
        MB = False
        break
    else:
        print('새로고침')
        driver.refresh()


time.sleep(1)
# 예매하기 눌러서 새창이 뜨면 포커스를 새창으로 변경
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

##########################################################
pag.click(441, 535)                                #catcha
capture_start()
img = cv.imread('0.png', cv.IMREAD_GRAYSCALE)
cv.imshow('original', img)


cv.waitKey(0)
cv.destroyAllWindows()
##########################################################

# while(True):
#     if keyboard.is_pressed('1'):
#        break
#    else:
#        pass

def color(RGB):  # RGB 값을 색깔 문자열로 반환하는 함수
    c_p = (124, 104, 238)
    c_g = (28, 168, 20)
    c_c = (23, 179, 255)
    c_o = (251, 126, 79)
    c_r = (255, 68, 15)
    test = (0,0,0)
    if RGB == c_p: return "purple"
    elif RGB == c_g: return "green"
    elif RGB == c_c: return "cyan"
    elif RGB == c_o: return "orange"
    elif RGB == c_r: return "red"
    elif RGB == test: return "test"
    else: return "other"
SB=0


print("here!!!!!!!!!!")
while SB==0:
    if keyboard.is_pressed('2'):
        break
    else:
        pag.click(849, 704)
        time.sleep(0.5)
        screen = ImageGrab.grab() # 화면 캡쳐
        for j in range(219, 753):
        #for j in range(0, 992):
            for i in range(145, 564):
        #    for i in range(0, 900): 
                # if i%30==0 and j % 30==0 : pag.click((i,j))
                A = color(screen.getpixel((i,j))) # 가장왼쪽자리
                if (A == "test"): # 5색깔 중 하나 + 두 자리
                    print(A)
                    pag.click((i,j))
                    pag.click((i+3,j+3))
                    pag.click(871, 669) #좌석선택완료
                    SB=1
                    break
                if SB==1:
                    break
            if SB==1:
                break
input()