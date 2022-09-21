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
driver  = webdriver.Chrome(r".\driver\chromedriver.exe", options=options)
time.sleep(10)

#%%
def buscar_campos(driver, url_cargo):

    print("Funcao buscar_campos")
    cargo=[]
    local=[]
    empresa=[]
    descricao=[]
    page=1
    
    # O numero de vagas por pagina é 10. Se o total de vagas for menor que 10, pelo 1 pagina é mostrada.
    # Se o numero for 13, vai mostrar 1 pagina com 10 e outra com 3, no total 2 paginas.
    #pagina_final = (int(total_vagas/10)+1)*10
    pagina_final = 10

    #url_page = url_page_BR+str('&start=')

    pagina_limite = 10 # Seria aqui o total de vagas se fosse pesquisar todas vagas
                        # Dessa forma as primeiras 5 paginas apenas.

    if (pagina_final < pagina_limite):
        pagina_limite = pagina_final
    
    #print("Pagina limite:", pagina_limite)  
    print("Serão pesquisadas ", int(pagina_limite/10), "paginas")
    print("Sleep de 50 e wait de 60")

    for n in range(0,pagina_limite,10):

        print("\nPage:",n,'\n')
        url_page_n = url_cargo+str(n)

        driver.get(url_page_n)

        driver.implicitly_wait(60)

    

        elem_mosaic = driver.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul')#'//*[@id="mosaic-provider-jobcards"]/ul')

        #print("elem_mosaic:\n", type(elem_mosaic))

        page_html = elem_mosaic.get_attribute('innerHTML')
        
        soup = bs(page_html, 'html.parser')
        result = soup.find_all('ul', {'class': 'jobsearch-ResultsList css-0'})
        print("Result type\n: ", type(result))
        
        print("inside result:\n",result)


        #print("TESTE innerHTML:\n",page_html)
        #try: 
            #soup = bs(page_html, 'html.parser')
            #result = soup.find_all('ul', {'class': 'jobsearch-ResultsList css-0'})
            #print("Result type: ", type(result))

            #print(result)
            #for ul_tag in result:
            #    print("ul:\n", ul_tag)  

                #for lit_tag in ul_tag.find_all('li'):
                #    print('LI:\n', li_tag.text)

            #lis = soup.find_all('li')
            #print("Size:\n", len(lis))
            #for i in lis:
            #    print("LI:\n",i.text)
        #except:
        #    print('Erro no soup')    

       

        #res = requests.get(url_page_n)
        #html_page = res.text

        #soup = bs(res.text, 'html.parser')

        #print("html page:\n", html_page)

        #print(soup.find('h1').getText())
        
        #data = soup.find('ul', class_="jobsearch-ResultsList css0")


        
        #print(url_page)
        #print("url_page_BR: ",url_page_BR)

        #driver.implicitly_wait(60)
        #elem_mosaic = driver.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]')
        #elem_mosaic = driver.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul')
        #elem_mosaic = driver.find_element(By.CLASS_NAME, '//*[@id="mosaic-provider-jobcards"]/ul')
        
        #print("result:", elem_mosaic)

        #page = bs(elem_mosaic.text, 'html.parser')
        #print("\nVagas:\n", page)


        #print("Tipo page:", type(page))

        #print("Prettify:",page.prettify)

        
        #url_page_n = url_cargo+str(n)
        #print("URL pesquisada:\n", url_page_n)
        #driver.get(url_page_n)
        #print("Sleep 50")
        #time.sleep(50)
        #driver.implicitly_wait(60)
        #url_page = driver.current_url
        #page = requests.get(url_page)
        #oup = BeautifulSoup(page.text, 'html.parser')
        #print("soup:", soup.text)
        #data = soup.find('ul', class_="jobsearch-ResultsList css0")
        #print('data:', type(data))
        #data = driver.find_element(By.CLASS_NAME, "jobsearch-ResultsList css-0")
        #elem_mosaic_zone = driver.find_element(By.CLASS_NAME, "mosaic-zone")
        #print("Tipo mosaic_zone:",type(elem_mosaic_zone))
        #elem_jobcards = elem_mosaic_zone.find_element(By.CLASS_NAME, "mosaic mosaic-provider-jobcards mosaic-provider-hydrated")
        #print("Tipo elem_jobcards:",type(elem_jobcards))
        #elem_result = driver.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]')
        #print("Tipo result:",type(elem_result))
        #elem_mosaic_providers_jobcards = elem_result.find_element(By.XPATH,'//*[@id="mosaic-provider-jobcards"]/ul')
        #print("Tipo elem_mosaic_providers_jobcards:",type(elem_mosaic_providers_jobcards))
        #for i in elem_mosaic_providers_jobcards:
        #    print(i)     
   


    #return

    # //*[@id="mosaic-provider-jobcards"]/ul

        #for i in data:
        #    print("Dentro do for")
        #    print(i.text)
        #print('\n\tSoup:', soup)
        #parent = soup.find('body').find('ul')
        #text = list(parent.descendants)
        #print(text)
        #for i range(2,len(text),2):
        #    print(text[i], end=" ")
        #all_jobs = soup.find('ul', {"class": "jobsearch-ResultsList css-0"})
        #print(type(all_jobs)) 
    #    for job in all_jobs:

    #        result_html = job.get_attribute('innerHTML')
    #        soup = BeautifulSoup(result_html, 'html.parser')
		
    #        try:
    #            title = soup.find("a", class_="jobtitle").text.replace('\n', '')
    #        except:
    #            title = 'None'
    #        cargo.append(title)   

    #        try:
    #            location = soup.find(class_="location").text
    #        except:
    #            location = 'None'
    #        local.append(location)        

    #        try:
    #            company = soup.find(class_="company").text.replace("\n", "").strip()
    #        except:
    #            company = 'None'
    #        empresa.append(company)        


    #        try:
    #            summary = soup.find(class_="summary").text.replace("\n", "").strip()
    #        except:
    #            summary = 'None'
    #        descricao.append(summary)

            
        #print("Page: {}".format(str(page)))
    #    page=page+1
       

    #return (cargo, local, empresa, descricao)


#%%
url_app = 'https://silviolima07-app-venda-imoveis-app-ukx6ci.streamlitapp.com/'
#%%
print("\nAcessando app do streamlit\n")
driver.get(url_app)
driver.implicitly_wait(50)
time.sleep(60)
print("Encerrando browse aberto")
driver.close()
#%%
# Advanced search
#advanced_search = driver.find_element_by_xpath("//a[contains(text(),'Achar vagas')]")
#advanced_search.click()

#%%
#print("\Enviar cargo\n")
# Enviar na pagina na linha as_ttl, para usar as palavras em CARGO na busca
#search_job = driver.find_element(By.NAME,'q')
#search_job.send_keys([CARGO])
#%%
# Localizacao
#print("\nLimpar e enviar localizacao Brasil\n")
#search_local = driver.find_element(By.NAME,'l')
#search_local.send_keys(Keys.CONTROL, 'a')
#search_local.send_keys(Keys.DELETE)
#search_local.clear()
#search_local.send_keys('Brasil')
#%%
#print("\nClicar em Achar vagas")
# Apos envio acionar botao para iniciar busca
#search_button = driver.find_element(By.XPATH,'//*[@id="jobsearch"]/button')
#search_button.click()
#driver.implicitly_wait(50)
#url_page = driver.current_url
#print(url_page)
#%%%
# Clicar se aparecer botao Close do google account
#try:
#    search_close =  driver.find_element(By.CSS_SELECTOR,'#google-Only-Modal > div > div.google-Only-Modal-Upper-Row > button') 
#    print("\nclose:", type(search_close))
#    search_close.click()
    #driver.implicitly_wait(20)
#except:
#    print("\nerror botao close")    

#%%
#cargo, local, empresa, descricao = 
#jobs = buscar_campos(driver, url_ED)
#print("jobs: ", jobs)

#print(cargo)
#driver.quit()
#%%
#driver.quit()			
#data = {'Cargo': cargo,
#        'Local': local,
#        'Empresa': empresa,
#        'Descrição': descricao}

#df = pd.DataFrame(data, columns=["Cargo", "Local", "Empresa","Descrição"])
#df_final = df.drop_duplicates()

#cargo = CARGO.replace(' ', '_')
#print("\nCargo:", cargo)
#filename = 'indeed_'+cargo+'.csv'
#print("\nCriando arquivo CSV: ", filename)
#df_final.to_csv(filename, index=False, header=True)
	
