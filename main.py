import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

url = 'http://books.toscrape.com/'
navegador.get(url)

caminho_arquivo = 'dados.txt'
###

for number in range(1, 21):
    path = f'/html/body/div/div/div/div/section/div[2]/ol/li[{number}]/article/h3/a'
    navegador.find_element('xpath', path).click()

    title       = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1').text
    upc         = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[1]/td').text
    prod_type   = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[2]/td').text
    price1      = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[3]/td').text
    price2      = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[4]/td').text
    tax         = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[5]/td').text
    avaiability = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[6]/td').text
    reviews     = navegador.find_element('xpath', '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[7]/td').text

    try:
        arquivo = open(caminho_arquivo, 'r')
    except FileNotFoundError:
        arquivo = open(caminho_arquivo, 'w')

    with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
        arquivo.write(f'{title}\n')
        arquivo.write(f'{upc}\n')
        arquivo.write(f'{prod_type}\n')
        arquivo.write(f'{price1}\n')
        arquivo.write(f'{price2}\n')
        arquivo.write(f'{tax}\n')
        arquivo.write(f'{avaiability}\n')
        arquivo.write(f'{reviews}\n')
        arquivo.write('')

    # print(f'título: {title}\nupc: {upc}\ntype: {prod_type}\nprice1: {price1}\nprice2: {price2}\ntax: {tax}\navaiability: {avaiability}\nreviews: {reviews}')

    navegador.back()
navegador.quit()

"""
    books = {
        'titulo': title,
        'upc': upc,
        'type': prod_type,
        'price1': price1,
        'price2': price2,
        'tax': tax,
        'avaiability': avaiability,
        'reviews': reviews,
    }

    dataframe = pd.DataFrame(books)
    dataframe.to_excel('./books.xls')

"""