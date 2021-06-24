# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:29:53 2021

@author: dkmii
"""

import bs4
import requests
import pandas as pd


# Main URL: "https://www.eia.gov/dnav/pet/pet_pnp_inpt_a_epc0_yir_mbbl_m.htm"
        

url1 = "https://www.eia.gov/opendata/qb.php?sdid=PET.MCRRIP12.M"   #for PADD1
        
ResponseData = requests.get(url1)
ResponseData

soup = bs4.BeautifulSoup(ResponseData.text, 'html.parser')
print(soup.prettify())

filename = "index1.html"
formatted_text = soup.prettify()
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)


table=soup.find("table", attrs={"class":"basic_table"})
results=table.find_all("tr")
print("No. of results: ", len(results))
print(results)

headers=[]
for i in table.find_all("th"):
    title=i.text
    print(title)
    headers.append(title)

df1=pd.DataFrame(columns=headers)
print(df1)


for row in table.find_all("tr")[1:]:
    data=row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df1)
    df1.loc[length] = row_data
        
print(df1)   
df1.to_csv('PADD1.csv')
df1.to_excel('PADD1.xlsx')
PADD1 = pd.read_csv('PADD1.csv')
    
    
#######################################################
#########################################################
######################################################### 
    
url2 = "https://www.eia.gov/opendata/qb.php?sdid=PET.MCRRIP22.M"   #for PADD2  
     
ResponseData = requests.get(url2)
ResponseData

soup = bs4.BeautifulSoup(ResponseData.text, 'html.parser')
print(soup.prettify())

filename = "index2.html"
formatted_text = soup.prettify()
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)


table=soup.find("table", attrs={"class":"basic_table"})
results=table.find_all("tr")
print("No. of results: ", len(results))
print(results)

headers=[]
for i in table.find_all("th"):
    title=i.text
    print(title)
    headers.append(title)

df2=pd.DataFrame(columns=headers)
print(df2)


for row in table.find_all("tr")[1:]:
    data=row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df2)
    df2.loc[length] = row_data
        
print(df2)   
df2.to_csv('PADD2.csv')
df2.to_excel('PADD2.xlsx') 
PADD2 = pd.read_csv('PADD2.csv')    
    
    
########################################################
#######################################################
#########################################################


url3 = "https://www.eia.gov/opendata/qb.php?sdid=PET.MCRRIP32.M"   #for PADD3  
     
ResponseData = requests.get(url3)
ResponseData

soup = bs4.BeautifulSoup(ResponseData.text, 'html.parser')
print(soup.prettify())

filename = "index3.html"
formatted_text = soup.prettify()
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)


table=soup.find("table", attrs={"class":"basic_table"})
results=table.find_all("tr")
print("No. of results: ", len(results))
print(results)

headers=[]
for i in table.find_all("th"):
    title=i.text
    print(title)
    headers.append(title)

df3=pd.DataFrame(columns=headers)
print(df3)


for row in table.find_all("tr")[1:]:
    data=row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df3)
    df3.loc[length] = row_data
        
print(df3)   
df3.to_csv('PADD3.csv')
df3.to_excel('PADD3.xlsx') 
PADD3 = pd.read_csv('PADD3.csv')


########################################################
#########################################################
#######################################################
url4 = "https://www.eia.gov/opendata/qb.php?sdid=PET.MCRRIP42.M"   #for PADD4  
     
ResponseData = requests.get(url4)
ResponseData

soup = bs4.BeautifulSoup(ResponseData.text, 'html.parser')
print(soup.prettify())

filename = "index4.html"
formatted_text = soup.prettify()
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)


table=soup.find("table", attrs={"class":"basic_table"})
results=table.find_all("tr")
print("No. of results: ", len(results))
print(results)

headers=[]
for i in table.find_all("th"):
    title=i.text
    print(title)
    headers.append(title)

df4=pd.DataFrame(columns=headers)
print(df4)


for row in table.find_all("tr")[1:]:
    data=row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df4)
    df4.loc[length] = row_data
        
print(df4)   
df4.to_csv('PADD4.csv')
df4.to_excel('PADD4.xlsx')
PADD4 = pd.read_csv('PADD4.csv')

#######################################################
####################################################
######################################################

url5 = "https://www.eia.gov/opendata/qb.php?sdid=PET.MCRRIP52.M"   #for PADD5
     
ResponseData = requests.get(url5)
ResponseData

soup = bs4.BeautifulSoup(ResponseData.text, 'html.parser')
print(soup.prettify())

filename = "index5.html"
formatted_text = soup.prettify()
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)


table=soup.find("table", attrs={"class":"basic_table"})
results=table.find_all("tr")
print("No. of results: ", len(results))
print(results)

headers=[]
for i in table.find_all("th"):
    title=i.text
    print(title)
    headers.append(title)

df5=pd.DataFrame(columns=headers)
print(df5)


for row in table.find_all("tr")[1:]:
    data=row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df5)
    df5.loc[length] = row_data
        
print(df5)   
df5.to_csv('PADD5.csv')
df5.to_excel('PADD5.xlsx') 
PADD5 = pd.read_csv('PADD5.csv')

######################################################
############################################################
#############################################################
url = "https://www.eia.gov/opendata/qb.php?sdid=PET.MCRRIUS2.M"   #for total US
     
ResponseData = requests.get(url)
ResponseData

soup = bs4.BeautifulSoup(ResponseData.text, 'html.parser')
print(soup.prettify())

filename = "indexTotalUS.html"
formatted_text = soup.prettify()
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)


table=soup.find("table", attrs={"class":"basic_table"})
results=table.find_all("tr")
print("No. of results: ", len(results))
print(results)

headers=[]
for i in table.find_all("th"):
    title=i.text
    print(title)
    headers.append(title)

df=pd.DataFrame(columns=headers)
print(df)


for row in table.find_all("tr")[1:]:
    data=row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data
        
print(df)   
df.to_csv('Total_US.csv')
df.to_excel('Total_US.xlsx') 
###############################################################
###########################################################
##############################################################

#Since all data has Exactly the same monthly frequency Period value
RawData={'Period_Monthly_Frequency': PADD1['Period'],
         'PADD1_value_in_Thousand_Barrels_per_Day':PADD1["Value"],
         'PAAD2_value_in_Thousand_Barrels_per_Day': PADD2['Value'],
         'PAAD3_value_in_Thousand_Barrels_per_Day': PADD3['Value'],
         'PAAD4_value_in_Thousand_Barrels_per_Day': PADD4['Value'],
         'PAAD5_value_in_Thousand_Barrels_per_Day': PADD5['Value']}


RawDataFrame=pd.DataFrame(RawData)
print(RawDataFrame)
RawDataFrame.to_csv('RawData.csv')

















