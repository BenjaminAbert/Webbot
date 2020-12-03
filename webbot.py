import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Åpner nettsiden rett i handlekurv
browser.get('https://www.komplett.no/cart')

# krysser ut popout-vindu
browser.find_element_by_xpath('//*[@id="caas-header"]/div[1]/div/div/div[2]/form/div/div[1]/button').click();

# klikker for å logge inn
browser.find_element_by_xpath('//*[@id="caas-header"]/header/section/div[1]/div/nav/div/div[1]/div').click();


#login info
brukernavn = ""
passord = ""

#skriver inn login info
browser.find_element_by_id('Username').send_keys(brukernavn)
browser.find_element_by_id('Password').send_keys(passord)

#logger inn
browser.find_element_by_xpath('/html/body/div/main/div/div[2]/section/div/div/div/form/button').click();
time.sleep(1)

#går til checkout og velger betaling
browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/form/div/div[2]/div[2]/div/button').click();
time.sleep(2)


kortinfo = ""


#
browser.find_element_by_id('').send_keys(kortinfo)
