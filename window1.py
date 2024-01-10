import pyautogui
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


user_name = "440211100590"
user_password = "S1234567U"

start_time = datetime.now()


driver = webdriver.Chrome()
driver.get("https://student.fiin.uz/test/exams")
# driver.get("file:///C:/Users/idevice/AppData/Local/Temp/Rar$EXa18264.45568/test.html")
username = driver.find_element(By.ID, "formstudentlogin-login")
username.clear()
username.send_keys(user_name)

password = driver.find_element(By.ID, "formstudentlogin-password")
password.clear()
sleep(1)
password.send_keys(user_password)
sleep(2)

login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/form/div[2]/div/div[2]/button").click()

sleep(3)

# sleep(10)
start_btn = driver.find_element(By.XPATH, "/html/body/div/div[2]/section/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr/td[5]/a").click()

sleep(2)
try:  
    pyautogui.press('enter')
except:
    sleep(10000)

sleep(5)

# # Web ga kirib alert ga enter bosish ^

def test_solver():
    count = 0
    answers_of_test = []


    with open('eko.txt', 'r') as file:
        
        lines = file.readlines()

        
        for line in lines:
            
            if line.startswith('#'):
                
                cleaned_line = line.lstrip('#').strip()
                answers_of_test.append(cleaned_line)
    
    # driver.get("file:///C:/Users/sodiq/OneDrive/Ishchi%20stol/Moliyaviy%20hisob%203%20(60410100-Buxgalteriya%20hisobi%20va%20audit%20(Sirtqi%203-kurs))%20_%20HEMIS%20Student%20axborot%20tizimi.html")
    sleep(2)

    for i in range(1, 26):
        for j in range(1, 5):
            variant_element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div[1]/div[{i+1}]/div[2]/p[{j}]/label/span[2]")
            variant_text = variant_element.text

            cleaned_variant = "".join(char if ord(char) < 128 else '' for char in variant_text)

            if cleaned_variant in answers_of_test:
                count  += 1
                variant_element.click()
    print(count)
    sleep(1000)
try:
    test_solver()
except:
    print('Nimadir xato ketdi')
    sleep(3600)
print('Menimcha tugadi')
sleep(3600)




    # /html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/p[1]/label/span[2] 1 A
    # /html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/p[2]/label/span[2] 1 B

    # /html/body/div[1]/div/div/div/div[1]/div[6]/div[2]/p[4]/label/span[2] 5 D

    # /html/body/div[1]/div/div/div/div[1]/div[26]/div[2]/p[1]/label/span[2] 25 A

# !Diqqat ushbu belgilar: “ va ” va ' va " va ʻ va ? lar umuman kerak emas o'chirib tashlash kerak .txt dan  –