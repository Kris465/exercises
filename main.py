from selenium import webdriver
import time

url = "https://cabinfourtranslations.wordpress.com/"
url1 = "https://cabinfourtranslations.wordpress.com/2022/07/15/sss-grade-cafe-in-front-of-the-dungeon-chapter-1/"
url2 = "https://cabinfourtranslations.wordpress.com/2022/07/15/sss-grade-cafe-in-front-of-the-dungeon-chapter-2/"
driver = webdriver.Chrome(executable_path="C:\\Users\\Nata\\Prog\\Parser\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(10)
    driver.get(url=url1)
    time.sleep(10)
    driver.get(url=url2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
