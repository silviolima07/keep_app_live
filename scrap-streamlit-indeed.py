#%%
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import os

#from checar_parametros import buscar_campos

#%%
#Acesso ao site do app streamlit

options = webdriver.ChromeOptions()
options.add_argument("--headless")
print("\nCriando driver chrome\n")
driver  = webdriver.Chrome(r"/usr/bin/chromedriver", options=options)
time.sleep(10)


url_app = 'https://silviolima07-app-indeed-app-d4yfit.streamlitapp.com/'
#%%
print("\nAcessando app do streamlit\n")
driver.get(url_app)
driver.implicitly_wait(60)
time.sleep(60)
print("Encerrando browse aberto")
driver.close()
