#𝐅𝐞𝐢𝐭𝐨 𝐩𝐨𝐫 𝐕𝐢𝐧𝐢𝐜𝐢𝐮𝐬 𝐒𝐚𝐧𝐭𝐨𝐬-𝐓𝐞𝐜𝐡
#𝙋𝙧𝙞𝙢𝙚𝙞𝙧𝙖 𝘼𝙥𝙡𝙞𝙘𝙖𝙘̧𝙖𝙤 𝙙𝙤 𝙎𝙀𝙇𝙀𝙉𝙄𝙐𝙈

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
produtos = [
    {"nome": "Iphone 15", "url": "https://www.magazineluiza.com.br/apple-iphone-15-128gb-preto-61-48mp-ios-5g/p/238035600/te/ip15/?&seller_id=magazineluiza&utm_source=google&utm_medium=cpc&utm_term=79684&utm_campaign=google_eco_per_ven_pla_mob_apo_1p_te-csp&utm_content=&partner_id=79684&gclsrc=aw.ds&gad_source=1&gad_campaignid=22578732921&gbraid=0AAAAAD4zZmT5uXVsHRh2cIloeqD8qpOHq&gclid=Cj0KCQjwmYzIBhC6ARIsAHA3IkTnqK3NnfhhKP-gG9UiCLFNsXjycOL-VqS4iNW8MzPEGm-V0b7YqicaAshiEALw_wcB"},
    {"nome": "Iphone 16e", "url": "https://www.magazineluiza.com.br/apple-iphone-16e-128gb-preto-61-48mp-ios-5g/p/240060000/te/i16e/?&seller_id=magazineluiza&utm_source=google&utm_medium=cpc&utm_term=79684&utm_campaign=google_eco_per_ven_pla_mob_apo_1p_te-csp&utm_content=&partner_id=79684&gclsrc=aw.ds&gad_source=1&gad_campaignid=22578732921&gbraid=0AAAAAD4zZmT5uXVsHRh2cIloeqD8qpOHq&gclid=Cj0KCQjwmYzIBhC6ARIsAHA3IkTycC-_8Iexk-xl0i0OrW1zWyEqQr0EA8oBzJ17-SFcH2OLtpFwhd8aAin4EALw_wcB"},
    {"nome": "Iphone 16", "url": "https://www.magazineluiza.com.br/apple-iphone-16-128gb-ultramarino-61-48mp-ios-5g/p/238804300/te/ip16/?&seller_id=magazineluiza&utm_source=google&utm_medium=cpc&utm_term=79684&utm_campaign=google_eco_per_ven_pla_mob_apo_1p_te-csp&utm_content=&partner_id=79684&gclsrc=aw.ds&gad_source=1&gad_campaignid=22578732921&gbraid=0AAAAAD4zZmT5uXVsHRh2cIloeqD8qpOHq&gclid=Cj0KCQjwmYzIBhC6ARIsAHA3IkQfDpqV8QpCJgRP22lxzQwvt_LvOnwzUs5oDu2QCKlj5x8CKGKAF2caAlzDEALw_wcB"}
]

for produto in produtos:
    driver.get(produto["url"])
    time.sleep(2)
    Nome = produto["nome"]
    preco = driver.find_element(By.CSS_SELECTOR,".leading-none.text-on-surface-1.font-3xlg-medium")
    print(f"O {Nome} esta custando: R$ {preco.text} ")

driver.quit()
