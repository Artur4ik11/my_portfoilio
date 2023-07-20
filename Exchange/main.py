import eel
from urllib.request import urlopen
from bs4 import BeautifulSoup

def for_usd(valuta,in_s,out_s):
    if in_s == 'USD' and out_s == 'BYN':
        responce = urlopen('https://myfin.by/converter/usd-byn')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'USD' and out_s == 'EUR':
        responce = urlopen('https://myfin.by/converter/usd-eur')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'USD' and out_s == 'RUB':
        responce = urlopen('https://myfin.by/converter/usd-rub')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    

def for_eur(valuta,in_s,out_s):
    if in_s == 'EUR' and out_s == 'BYN':
        responce = urlopen('https://myfin.by/converter/eur-byn')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'EUR' and out_s == 'USD':
        responce = urlopen('https://myfin.by/converter/eur-usd')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'EUR' and out_s == 'RUB':
        responce = urlopen('https://myfin.by/converter/eur-rub')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    
def for_rub(valuta,in_s,out_s):
    if in_s == 'RUB' and out_s == 'BYN':
        responce = urlopen('https://myfin.by/converter/rub-byn')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'RUB' and out_s == 'USD':
        responce = urlopen('https://myfin.by/converter/rub-usd')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'RUB' and out_s == 'EUR':
        responce = urlopen('https://myfin.by/converter/rub-eur')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    
def for_byn(valuta,in_s,out_s):
    if in_s == 'BYN' and out_s == 'EUR':
        responce = urlopen('https://myfin.by/converter/byn-eur')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'BYN' and out_s == 'USD':
        responce = urlopen('https://myfin.by/converter/byn-usd')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    elif in_s == 'BYN' and out_s == 'RUB':
        responce = urlopen('https://myfin.by/converter/byn-rub')
        soup = BeautifulSoup(responce)
        tag_list = soup.find_all('td')
        pars = tag_list[1].text.split()
        x = float(pars[0]) * float(f'{valuta}.0')
        return x
    


@eel.expose
def get_course(valuta,in_s,out_s):
    if in_s == out_s:
        return valuta
    elif in_s == 'USD':
        output_data =  for_usd(valuta,in_s,out_s)
    elif in_s == 'EUR':
        output_data = for_eur(valuta,in_s,out_s)
    elif in_s == 'RUB':
        output_data = for_rub(valuta,in_s,out_s)
    elif in_s == 'BYN':
        output_data = for_byn(valuta,in_s,out_s)
    
    return output_data

    
    
    
    


eel.init("web")

eel.start("index.html",size = (400,600))


