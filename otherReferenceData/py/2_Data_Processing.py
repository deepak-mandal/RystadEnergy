# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:10:08 2021

@author: dkmii
"""
import pandas as pd


PADD = pd.read_csv('C:/Users/dkmii/Desktop/PythonTask/RawData.csv')
print(PADD)
PADD.head(10)
#df=PADD

#A/c to the dataFrame,to keep the data from January 2016 onwards, we need only first 62 row's data. 
PADD=PADD.iloc[:63,:]
#df1=PADD
print(PADD.head())
PADD.drop(["Unnamed: 0"], axis=1, inplace=True)
df2=PADD
'''
for x in PADD.iloc[0:1,:]:
    print(x)
'''
period_month=[]
period_quarter=[]
period_year=[]
for x in PADD['Period_Monthly_Frequency']:
    strX=str(x)
    MM=strX[4:]
    period_month.append(MM)
    YYYY=strX[:4]
    period_year.append(int(YYYY))
    MM=int(MM)
    
    if (MM-1)//3 + 1 == 1:
        period_quarter.append('Q1')
    elif (MM-1)//3 + 1 == 2:
        period_quarter.append('Q2')
    elif (MM-1)//3 + 1 == 3:
        period_quarter.append('Q3')
    elif (MM-1)//3 + 1 == 4:
        period_quarter.append('Q4')
    
print(period_month)
print(period_quarter)
print(period_year)




DataFrame_C = {'Period':PADD['Period_Monthly_Frequency'],
               'Year':period_year,
               'Quarter':period_quarter,
               'Month':period_month,
               '(PADD1) Refinery and Blender Net Input of Crude Oil': PADD['PADD1_value_in_Thousand_Barrels_per_Day'],
               '(PADD2) Refinery and Blender Net Input of Crude Oil': PADD['PAAD2_value_in_Thousand_Barrels_per_Day'],
               '(PADD3) Refinery and Blender Net Input of Crude Oil': PADD['PAAD3_value_in_Thousand_Barrels_per_Day'],
               '(PADD4) Refinery and Blender Net Input of Crude Oil': PADD['PAAD4_value_in_Thousand_Barrels_per_Day'],
               '(PADD5) Refinery and Blender Net Input of Crude Oil': PADD['PAAD5_value_in_Thousand_Barrels_per_Day']}

C_Final_dataFrame=pd.DataFrame(DataFrame_C)
print(C_Final_dataFrame)


C_Final_dataFrame['(PADD1) Refinery and Blender Net Input of Crude Oil'].describe()



Total_US_Refinery_and_Blender_Net_Input_of_Crude_Oil=[]
for i in range(len(C_Final_dataFrame['Period'])):
    sumRow=0
    sumRow+=C_Final_dataFrame['(PADD1) Refinery and Blender Net Input of Crude Oil'][i]+C_Final_dataFrame['(PADD2) Refinery and Blender Net Input of Crude Oil'][i]+C_Final_dataFrame['(PADD3) Refinery and Blender Net Input of Crude Oil'][i]+C_Final_dataFrame['(PADD4) Refinery and Blender Net Input of Crude Oil'][i]+C_Final_dataFrame['(PADD5) Refinery and Blender Net Input of Crude Oil'][i]
    Total_US_Refinery_and_Blender_Net_Input_of_Crude_Oil.append(sumRow)
    
print(Total_US_Refinery_and_Blender_Net_Input_of_Crude_Oil)   
    



Total_US={'Period':PADD['Period_Monthly_Frequency'],
            'Quarter':period_quarter,
            '(PADD1) Refinery and Blender Net Input of Crude Oil': PADD['PADD1_value_in_Thousand_Barrels_per_Day'],
               '(PADD2) Refinery and Blender Net Input of Crude Oil': PADD['PAAD2_value_in_Thousand_Barrels_per_Day'],
               '(PADD3) Refinery and Blender Net Input of Crude Oil': PADD['PAAD3_value_in_Thousand_Barrels_per_Day'],
               '(PADD4) Refinery and Blender Net Input of Crude Oil': PADD['PAAD4_value_in_Thousand_Barrels_per_Day'],
               '(PADD5) Refinery and Blender Net Input of Crude Oil': PADD['PAAD5_value_in_Thousand_Barrels_per_Day'],
               '(Total US) Refinery and Blender Net Input of Crude Oil': Total_US_Refinery_and_Blender_Net_Input_of_Crude_Oil}

d_Summarization_monthly_data_by_Quarter=pd.DataFrame(Total_US)


d_Summarization_monthly_data_by_Quarter.describe()






















