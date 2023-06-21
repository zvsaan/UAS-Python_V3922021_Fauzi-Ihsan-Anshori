#!/usr/bin/env python
# coding: utf-8

# In[38]:


import requests #Mengirim permintaan HTTP
from bs4 import BeautifulSoup
import csv

#link yg akan diambil datanya
web_url = 'https://www.bukalapak.com/c/handphone/power-bank?page=' 

data_list = [] #menyimpan data

#scraping 6 halaman
for page in range(1, 7):
    url = web_url + str(page)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    
    #mencari semua elemen yang memiliki class ini
    product_items = soup.find_all('div', {'class': 'bl-product-card'})
    
    for item in product_items:
        
        #ambil nama produk sesuai tag dan classnya
        nama_produk = item.find('a', {'class': 'bl-link'}).text.strip()
        #ambil harga dari produk sesuai tag dan classnya
        harga = item.find('p', {'class': 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1'}).text.strip()
        #ambil alamat toko sesuai dengan tag dan classnya
        alamat = item.find('span', {'class': 'mr-4 bl-product-card__location bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1'}).text.strip()
        data_list.append([nama_produk, harga, alamat])

#menyimpan file dalam bentuk .csv disini saya membuat file .csv dengan nama File.csv
filename = 'File.csv'

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['NAMA PRODUK', 'HARGA', 'ALAMAT']) #header dalam file csv nya
    writer.writerows(data_list)

#menampilkan pesan ketika file berhasil disimpan
print(' ')
print('Data telah berhasil disimpan dalam file', filename)


# In[39]:


import pandas as pd

data=pd.read_csv("File.csv")

display(data.head(5))


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("File.csv")

plt.scatter(data['HARGA'], data['ALAMAT'])

plt.title("Scatter Plot")

plt.xlabel('HARGA')
plt.ylabel('ALAMAT')

#menyimpan ke dalam bentuk .png karena saya kasih transprent/png
plt.savefig("Scatter Plot", facecolor='y', bbox_inches="tight",
           pad_inches=0.3, transparent=True)


# In[44]:


import pandas as pd 
import matplotlib.pyplot as plt
 
data = pd.read_csv("File.csv")

plt.hist(data['ALAMAT'])

plt.title("Histogram")

#menyimpan dalam bentuk jpg
plt.savefig("Histogram.jpg")


# In[ ]:




