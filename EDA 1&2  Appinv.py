#!/usr/bin/env python
# coding: utf-8

# Done by Harsh Singh
# Email: harshsengar28@gmail.com

# # Problem Statement - I and Problem Statement - II  Solved

# In[273]:


pip install seaborn


# In[ ]:


#working Start


# In[274]:


import seaborn as sns


# In[291]:


import statistics

import warnings
warnings.filterwarnings("ignore")


# In[286]:


pip install numpy


# In[287]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[6]:


import pandas as pd


# In[7]:


df1 = pd.read_csv(r"C:\Users\Harsh Singh\Desktop\EDA\application_data.csv")


# In[8]:


df1   ##. 'application_data.csv' contains all the information of the client at the time of application.
     #The data is about whether a client has payment difficulties.


# In[9]:


df2 = pd.read_csv(r"C:\Users\Harsh Singh\Desktop\EDA\columns_description.csv",encoding="ISO-8859-1")


# In[10]:


df2 #columns_description.csv' is data dictionary which describes the meaning of the variables.


# In[11]:


df3 = pd.read_csv(r"C:\Users\Harsh Singh\Desktop\EDA\previous_application.csv")


# In[12]:


df3   ##contains information about the client’s previous loan data. 
    #It contains the data on whether the previous application had been Approved, Cancelled, Refused or Unused offer.


# In[13]:


df3.shape


# In[14]:


df3.head()


# df3.info()

# In[15]:


df3.info()   #helping to find out null contain columns
#we will start data cleaning from this dataframe 


# In[16]:


df3.isnull()  #to find the null


# In[17]:


df3.isnull().sum() #to get null count columnwise


# In[18]:


len(df3.index) #total rows


# In[19]:


df3.isnull().sum()/len(df3.index)*100    #finding percentage of nulls columnwise wrt total rows


# In[339]:


#there are so many columns which are having nulls more then 50% or approx 50% and they wont help in analysis so we have to delete them. 


# In[21]:


df3=df3.drop(["AMT_DOWN_PAYMENT", "RATE_DOWN_PAYMENT", "RATE_INTEREST_PRIMARY","RATE_INTEREST_PRIVILEGED","NAME_TYPE_SUITE"], axis=1)


# In[22]:


df3.isnull().sum()/len(df3.index)*100    #checking >>>#finding percentage of nulls columnwise wrt total rows


# In[23]:


##now handling nulls values in columns 


# In[24]:


df3["AMT_ANNUITY"].isnull().sum()


# In[25]:


pd.options.display.float_format = "{:.2f}".format #to display in decimal form
df3["AMT_ANNUITY"].describe()


# In[26]:


#plotting a histogram to see data visually
plt.hist(df3["AMT_ANNUITY"])
plt.show()


# In[27]:


#We can see most values lie between min and 50%. 
#Using median to put missing values as mean would skew the data

df3["AMT_ANNUITY"].median(skipna = True)


# In[28]:


df3["AMT_ANNUITY"]= df3["AMT_ANNUITY"].fillna(df3["AMT_ANNUITY"].median(skipna=True))


# In[29]:


pd.options.display.float_format = "{:.2f}".format #to display in decimal form
df3["AMT_ANNUITY"].describe()


# In[30]:


#after null filling


# In[31]:


#plotting a histogram to see data visually
plt.hist(df3["AMT_ANNUITY"])
plt.show()


# In[32]:


## Y-axis changed from 1.2 to 1.6 after  null values added


# In[33]:


#for outliners


# In[34]:


df3.boxplot(["AMT_ANNUITY"], figsize=[8,8])
plt.show()


# In[35]:


#data seems okay as data is not that much spreaded and no outliners


# In[36]:


df3.isnull().sum()   ##now doing same for all columns which contains null values


# In[37]:


df3["AMT_GOODS_PRICE"].describe()


# In[38]:


plt.hist(df3["AMT_GOODS_PRICE"])
plt.show()


# In[39]:


df3["AMT_GOODS_PRICE"] = df3["AMT_GOODS_PRICE"].fillna(df3["AMT_GOODS_PRICE"].isnull().sum())


# In[40]:


df3["AMT_GOODS_PRICE"].isnull().sum()


# In[41]:


plt.hist(df3["AMT_GOODS_PRICE"])
plt.show() ##after adding missing values


# In[42]:


df3.boxplot(["AMT_GOODS_PRICE"], figsize = [8, 10])
plt.show()


# In[43]:


##Data Seems to be okay


# In[44]:


df3.isnull().sum()


# In[45]:


df3["CNT_PAYMENT"].describe()


# In[46]:


plt.hist(df3["CNT_PAYMENT"])
plt.show()


# In[47]:


df3["CNT_PAYMENT"].mean()


# In[48]:


df3["CNT_PAYMENT"] = df3["CNT_PAYMENT"].fillna(df3["CNT_PAYMENT"].mean()) ##filling missing values


# In[49]:


plt.hist(df3["CNT_PAYMENT"])  #after values added 
plt.show()


# In[50]:


df3["CNT_PAYMENT"].isnull().sum() #verifying now 


# In[51]:


df3["DAYS_FIRST_DRAWING"]


# In[52]:


df3["DAYS_FIRST_DRAWING"].describe()


# In[53]:


df3["DAYS_FIRST_DRAWING"].isnull().sum() #checking total null values


# In[54]:


plt.hist(df3["DAYS_FIRST_DRAWING"])
plt.show()


# In[55]:


##here we have to use median 


# In[56]:


df3["DAYS_FIRST_DRAWING"].median()


# In[57]:


df3["DAYS_FIRST_DRAWING"]= df3["DAYS_FIRST_DRAWING"].fillna(df3["DAYS_FIRST_DRAWING"].median())


# In[58]:


plt.hist(df3["DAYS_FIRST_DRAWING"])
plt.show()   #after filling 


# In[59]:


#move to next column 


# In[60]:


df3['DAYS_FIRST_DUE'].describe()


# In[61]:


df3['DAYS_FIRST_DUE'].isnull().sum()


# In[62]:


plt.hist(df3["DAYS_FIRST_DUE"])
plt.show()   


# In[63]:


#here gonna use median


# In[64]:


df3['DAYS_FIRST_DUE'].median()


# In[65]:


df3['DAYS_FIRST_DUE']=df3['DAYS_FIRST_DUE'].fillna(df3['DAYS_FIRST_DUE'].median())


# In[66]:


plt.hist(df3["DAYS_FIRST_DUE"])
plt.show()   #after filling 


# In[67]:


df3["DAYS_FIRST_DUE"].isnull().sum()
#checking null


# In[68]:


df3["DAYS_LAST_DUE_1ST_VERSION"].describe()


# In[69]:


plt.hist(df3["DAYS_LAST_DUE_1ST_VERSION"])
plt.show()


# In[70]:


#handling with median


# In[71]:


df3["DAYS_LAST_DUE_1ST_VERSION"].median()


# In[72]:


#filling null


# In[73]:


df3["DAYS_LAST_DUE_1ST_VERSION"] = df3["DAYS_LAST_DUE_1ST_VERSION"].fillna(df3["DAYS_LAST_DUE_1ST_VERSION"].median())


# In[74]:


df3["DAYS_LAST_DUE_1ST_VERSION"].isnull().sum()


# In[75]:


#after filling 
plt.hist(df3["DAYS_LAST_DUE_1ST_VERSION"])
plt.show()


# In[76]:


#next column 

df3["DAYS_LAST_DUE"].describe()


# In[79]:


df3["DAYS_LAST_DUE"].isnull().sum()


# In[80]:


plt.hist(df3["DAYS_LAST_DUE"])
plt.show()


# In[81]:


#using median to fill
df3["DAYS_LAST_DUE"]=df3["DAYS_LAST_DUE"].fillna(df3["DAYS_LAST_DUE"].median())


# In[82]:


df3["DAYS_LAST_DUE"].isnull().sum()


# In[83]:


plt.hist(df3["DAYS_LAST_DUE"])
plt.show() #checking


# In[86]:


df3["DAYS_TERMINATION"].isnull().sum()


# In[85]:


df3["DAYS_TERMINATION"].describe()


# In[87]:


plt.hist(df3["DAYS_TERMINATION"])
plt.show()


# In[88]:


#filling values  with median


# In[89]:


df3["DAYS_TERMINATION"]=df3["DAYS_TERMINATION"].fillna(df3["DAYS_TERMINATION"].median())


# In[90]:


df3["DAYS_TERMINATION"].isnull().sum()


# In[91]:


plt.hist(df3["DAYS_TERMINATION"])
plt.show()


# In[92]:


#moving next 


# In[93]:


df3["NFLAG_INSURED_ON_APPROVAL"].isnull().sum()


# In[94]:


df3["NFLAG_INSURED_ON_APPROVAL"].describe()


# In[95]:


plt.hist(df3["NFLAG_INSURED_ON_APPROVAL"])
plt.show()


# In[96]:


#using median


# In[97]:


df3["NFLAG_INSURED_ON_APPROVAL"]=df3["NFLAG_INSURED_ON_APPROVAL"].fillna(df3["NFLAG_INSURED_ON_APPROVAL"].median())


# In[98]:


df3["NFLAG_INSURED_ON_APPROVAL"].isnull().sum()


# In[99]:


plt.hist(df3["NFLAG_INSURED_ON_APPROVAL"])
plt.show()


# In[100]:


#moving next


# In[101]:


df3["NFLAG_INSURED_ON_APPROVAL"].isnull().sum()


# In[102]:


df3.isnull().sum()


# In[104]:


df3["PRODUCT_COMBINATION"].describe()


# In[105]:


df3["PRODUCT_COMBINATION"]


# In[106]:


df3["PRODUCT_COMBINATION"].value_counts()


# In[107]:


##filling value with cash


# In[108]:


df3["PRODUCT_COMBINATION"]=df3["PRODUCT_COMBINATION"].fillna("Cash")


# In[109]:


#after filling


# In[110]:


df3["PRODUCT_COMBINATION"].value_counts()


# In[111]:


df3["PRODUCT_COMBINATION"].isnull().sum()


# In[112]:


df3["AMT_CREDIT"].isnull().sum()


# In[113]:


df3["AMT_CREDIT"].describe()


# In[114]:


plt.hist(df3["AMT_CREDIT"])
plt.show()


# In[115]:


df3["AMT_CREDIT"].median()


# In[116]:


df3["AMT_CREDIT"]=df3["AMT_CREDIT"].fillna(df3["AMT_CREDIT"].median())


# In[117]:


df3["AMT_CREDIT"].isnull().sum()


# In[118]:


plt.hist(df3["AMT_CREDIT"])
plt.show()


# In[119]:


df3.isnull().sum()  ##all Data has cleaned  for previousApplication


# In[122]:


## now moving on to Application_data >>>>>df1


# In[125]:


df1.info(verbose = True, show_counts = True)


# In[126]:


(df1.isnull().sum()/len(df1))*100


# In[127]:


##all columns are not visible , so we have to do some chnage 


# In[128]:


pd.set_option("display.max_rows", None, "display.max_columns", None)  ##to get all columns visiblity


# In[129]:


(df1.isnull().sum()/len(df1))*100


# In[130]:


#removing all columns which has more then 50% of null values 


# In[133]:


df1.drop(["OWN_CAR_AGE"],axis=1, implace=True)


# In[134]:


df1=df1.drop(["OWN_CAR_AGE"], axis=1)


# In[137]:


delete = [ "EXT_SOURCE_1", "APARTMENTS_AVG", 
                   "BASEMENTAREA_AVG", "YEARS_BUILD_AVG", "COMMONAREA_AVG", "ELEVATORS_AVG", 
                   
                   "ENTRANCES_AVG", "FLOORSMIN_AVG", "LANDAREA_AVG", "LIVINGAPARTMENTS_AVG", 
                   
                   "LIVINGAREA_AVG", "NONLIVINGAPARTMENTS_AVG", "NONLIVINGAREA_AVG", "APARTMENTS_MODE", 
                   
                   "BASEMENTAREA_MODE", "YEARS_BUILD_MODE", "COMMONAREA_MODE", "ELEVATORS_MODE", 
                   
                   "ENTRANCES_MODE", "FLOORSMIN_MODE", "LANDAREA_MODE", "LIVINGAPARTMENTS_MODE", 
                   "LIVINGAREA_MODE", "NONLIVINGAPARTMENTS_MODE", "NONLIVINGAREA_MODE", "APARTMENTS_MEDI",
                   "BASEMENTAREA_MEDI", "YEARS_BUILD_MEDI", "COMMONAREA_MEDI", "ELEVATORS_MEDI",
                   "ENTRANCES_MEDI", "FLOORSMIN_MEDI", "LANDAREA_MEDI", "LIVINGAPARTMENTS_MEDI", "LIVINGAREA_MEDI",
                   "NONLIVINGAPARTMENTS_MEDI", "LIVINGAREA_MEDI", "NONLIVINGAPARTMENTS_MEDI", 
                   "NONLIVINGAREA_MEDI", "FONDKAPREMONT_MODE", "HOUSETYPE_MODE", "WALLSMATERIAL_MODE"]


# In[138]:


df1=df1.drop(delete, axis=1)


# In[139]:


(df1.isnull().sum()/len(df1))*100


# In[140]:


#now deleting columns who are lear to 50%


# In[141]:


delete2=["YEARS_BEGINEXPLUATATION_AVG","FLOORSMAX_AVG","YEARS_BEGINEXPLUATATION_MODE","FLOORSMAX_MODE",
         "YEARS_BEGINEXPLUATATION_MEDI","FLOORSMAX_MEDI","TOTALAREA_MODE","EMERGENCYSTATE_MODE"]


# In[142]:


df1=df1.drop(delete2, axis=1)


# In[143]:


(df1.isnull().sum()/len(df1))*100


# In[144]:


##now filling missing valuesss 


# In[145]:


df1["AMT_GOODS_PRICE"].describe()


# In[146]:


df1["AMT_GOODS_PRICE"].isnull().sum()


# In[147]:


plt.hist(df1["AMT_GOODS_PRICE"])
plt.show()


# In[148]:


df1["AMT_GOODS_PRICE"].median()


# In[149]:


df1["AMT_GOODS_PRICE"] = df1["AMT_GOODS_PRICE"].fillna(df1["AMT_GOODS_PRICE"].median())


# In[150]:


df1["AMT_GOODS_PRICE"].isnull().sum()


# In[151]:


#doing same with all column


# In[152]:


df1["NAME_TYPE_SUITE"].isnull().sum()


# In[153]:


df1["NAME_TYPE_SUITE"].describe()


# In[154]:


df1["NAME_TYPE_SUITE"].value_counts()


# In[155]:


df1[df1["NAME_TYPE_SUITE"].isnull()]


# In[156]:


df1["NAME_TYPE_SUITE"] = df1["NAME_TYPE_SUITE"].fillna("Unaccompanied")


# In[157]:


pd.set_option("display.max_rows", 100, "display.max_columns", 100)
df1.isnull().sum()


# In[158]:


df1[df1["AMT_ANNUITY"].isnull()]


# In[159]:


plt.hist(df1["AMT_ANNUITY"])
plt.show()


# In[160]:


#filling with median


# In[161]:


df1["AMT_ANNUITY"].median()


# In[164]:


df1["AMT_ANNUITY"] = df1["AMT_ANNUITY"].fillna(df1["AMT_ANNUITY"].median())


# In[165]:


df1["AMT_ANNUITY"].isnull().sum()


# In[166]:


df1["OCCUPATION_TYPE"].describe()


# In[167]:


df1["OCCUPATION_TYPE"].head()


# In[168]:


df1["OCCUPATION_TYPE"].value_counts()


# In[169]:


df1["OCCUPATION_TYPE"].notna()


# In[170]:


#removing missing valuesss


# In[171]:


df1["OCCUPATION_TYPE"] = df1["OCCUPATION_TYPE"][~df1["OCCUPATION_TYPE"].isnull()]


# In[172]:


df1.dropna(subset=['OCCUPATION_TYPE'], inplace = True)


# In[173]:


df1["OCCUPATION_TYPE"].isnull().sum()


# In[174]:


df1.isnull().sum()


# In[179]:


df1["CODE_GENDER"].describe() ##managin unknown gender


# In[176]:


df1["CODE_GENDER"].value_counts()


# In[177]:


df1["CODE_GENDER"].mode()


# In[178]:


df1["CODE_GENDER"].isnull().sum()


# In[181]:


#adding F instead of XNA 

df1["CODE_GENDER"].replace("XNA", "F", inplace = True)


# In[186]:


#dropping columns which has no use in this analysis
df1.drop([ "FLAG_MOBIL", "FLAG_EMP_PHONE", "FLAG_WORK_PHONE", "FLAG_CONT_MOBILE",
                      "FLAG_PHONE", "REGION_RATING_CLIENT", "REGION_RATING_CLIENT_W_CITY", 
                      "FLAG_EMAIL", "REGION_RATING_CLIENT", "REGION_RATING_CLIENT_W_CITY",
                      "DAYS_LAST_PHONE_CHANGE","FLAG_DOCUMENT_2", "FLAG_DOCUMENT_3", "FLAG_DOCUMENT_4", 
                      "FLAG_DOCUMENT_5", "FLAG_DOCUMENT_6", "FLAG_DOCUMENT_7", "FLAG_DOCUMENT_8", 
                      "FLAG_DOCUMENT_9", "FLAG_DOCUMENT_10", "FLAG_DOCUMENT_11", "FLAG_DOCUMENT_12",
                      "FLAG_DOCUMENT_13", "FLAG_DOCUMENT_14", "FLAG_DOCUMENT_15", "FLAG_DOCUMENT_16",
                      "FLAG_DOCUMENT_17", "FLAG_DOCUMENT_18", "FLAG_DOCUMENT_19", "FLAG_DOCUMENT_20", 
                      "FLAG_DOCUMENT_21", "EXT_SOURCE_2", "EXT_SOURCE_3"], axis=1, inplace = True)


# In[187]:


df1.isnull().sum()


# In[188]:


df1.OBS_30_CNT_SOCIAL_CIRCLE.describe()


# In[189]:


df1.OBS_30_CNT_SOCIAL_CIRCLE.mean()


# In[190]:


df1.OBS_30_CNT_SOCIAL_CIRCLE = df1["OBS_30_CNT_SOCIAL_CIRCLE"].fillna(df1.OBS_30_CNT_SOCIAL_CIRCLE.mean())


# In[191]:


plt.hist(df1.OBS_30_CNT_SOCIAL_CIRCLE)
plt.show()


# In[192]:


df1.boxplot("OBS_30_CNT_SOCIAL_CIRCLE")
plt.show()


# In[193]:


#Outlier is present but as per the problem statement, we do not need to remove it


# In[194]:


df1["DEF_30_CNT_SOCIAL_CIRCLE"].describe()


# In[195]:


df1.boxplot("DEF_30_CNT_SOCIAL_CIRCLE")
plt.show()


# In[196]:


#no need to remove outliner


# In[197]:


#filling missing values with mean as the data is continuous
df1["DEF_30_CNT_SOCIAL_CIRCLE"] = df1["DEF_30_CNT_SOCIAL_CIRCLE"].fillna(df1["DEF_30_CNT_SOCIAL_CIRCLE"].mean())


# In[198]:


df1.boxplot("DEF_30_CNT_SOCIAL_CIRCLE")
plt.show()


# In[199]:


#no need to remove outliner


# In[200]:


df1["OBS_60_CNT_SOCIAL_CIRCLE"].describe()


# In[201]:


df1.boxplot("OBS_60_CNT_SOCIAL_CIRCLE")
plt.show()


# In[204]:


df1["OBS_60_CNT_SOCIAL_CIRCLE"] = df1["OBS_60_CNT_SOCIAL_CIRCLE"].fillna(df1["OBS_60_CNT_SOCIAL_CIRCLE"].median())


# In[205]:


df1.boxplot("OBS_60_CNT_SOCIAL_CIRCLE")
plt.show()


# In[206]:


df1.isnull().sum()


# In[207]:


df1["DEF_60_CNT_SOCIAL_CIRCLE"].describe()


# In[208]:


df1.boxplot("DEF_60_CNT_SOCIAL_CIRCLE")
plt.show()


# In[209]:


##filling missing values


# In[210]:


df1["DEF_60_CNT_SOCIAL_CIRCLE"] = df1["DEF_60_CNT_SOCIAL_CIRCLE"].fillna(df1["DEF_60_CNT_SOCIAL_CIRCLE"].median())


# In[211]:


df1.boxplot("DEF_60_CNT_SOCIAL_CIRCLE")
plt.show()


# In[212]:


df1["AMT_REQ_CREDIT_BUREAU_HOUR"].describe()


# In[213]:


plt.hist(df1["AMT_REQ_CREDIT_BUREAU_HOUR"])
plt.show()


# In[214]:


#filling missing values

df1["AMT_REQ_CREDIT_BUREAU_HOUR"] = df1["AMT_REQ_CREDIT_BUREAU_HOUR"].fillna(df1["AMT_REQ_CREDIT_BUREAU_HOUR"].mean())


# In[215]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_HOUR")
plt.show()


# In[216]:


df1["AMT_REQ_CREDIT_BUREAU_DAY"].describe()


# In[217]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_DAY")
plt.show()


# In[218]:


#filling 
df1["AMT_REQ_CREDIT_BUREAU_DAY"] = df1["AMT_REQ_CREDIT_BUREAU_DAY"].fillna(df1["AMT_REQ_CREDIT_BUREAU_DAY"].mean())


# In[219]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_DAY")
plt.show()


# In[220]:


df1["AMT_REQ_CREDIT_BUREAU_WEEK"].describe()


# In[221]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_WEEK")
plt.show()


# In[222]:


#filling data


# In[223]:


df1["AMT_REQ_CREDIT_BUREAU_WEEK"] = df1["AMT_REQ_CREDIT_BUREAU_WEEK"].fillna(df1["AMT_REQ_CREDIT_BUREAU_WEEK"].mean())


# In[224]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_WEEK")
plt.show()


# In[225]:


df1["AMT_REQ_CREDIT_BUREAU_MON"].describe()


# In[226]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_MON")
plt.show()


# In[228]:


#filling

df1["AMT_REQ_CREDIT_BUREAU_MON"] = df1["AMT_REQ_CREDIT_BUREAU_MON"].fillna(df1["AMT_REQ_CREDIT_BUREAU_MON"].mean())


# In[229]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_MON")
plt.show()


# In[230]:


df1.isnull().sum()


# In[231]:


df1["AMT_REQ_CREDIT_BUREAU_QRT"].describe()


# In[232]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_QRT")
plt.show()


# In[233]:


#outliner is there but no need to handle


# In[234]:


df1["AMT_REQ_CREDIT_BUREAU_QRT"] = df1["AMT_REQ_CREDIT_BUREAU_QRT"].fillna(df1["AMT_REQ_CREDIT_BUREAU_QRT"].median())


# In[235]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_QRT")
plt.show()


# In[236]:


df1["AMT_REQ_CREDIT_BUREAU_YEAR"].describe()


# In[237]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_YEAR")
plt.show()


# In[238]:


df1["AMT_REQ_CREDIT_BUREAU_YEAR"] = df1["AMT_REQ_CREDIT_BUREAU_YEAR"].fillna(df1["AMT_REQ_CREDIT_BUREAU_YEAR"].mean())


# In[239]:


df1.boxplot("AMT_REQ_CREDIT_BUREAU_YEAR")
plt.show()


# In[240]:


df1["AMT_REQ_CREDIT_BUREAU_YEAR"].isnull().sum()


# In[241]:


df1.isnull().sum()


# In[243]:


df1["CNT_FAM_MEMBERS"].describe()


# In[244]:


plt.hist(df1["CNT_FAM_MEMBERS"])
plt.show()


# In[245]:


df1["CNT_FAM_MEMBERS"]=df1["CNT_FAM_MEMBERS"].fillna(df1["CNT_FAM_MEMBERS"].median())


# In[247]:


df1.isnull().sum()


# # Data CLeaning Done for all, now moving forward for analysis
# 

# In[248]:


#some column has negetive number, converting them into abs


# In[ ]:





# In[249]:


df1['DAYS_BIRTH'] = abs(df1['DAYS_BIRTH'])
df1['DAYS_ID_PUBLISH'] = abs(df1['DAYS_ID_PUBLISH'])
df1['DAYS_ID_PUBLISH'] = abs(df1['DAYS_ID_PUBLISH'])


# In[253]:


df1.head()


# In[254]:


# Creating bin/buckets for income amount (AMT_INCOME_TOTAL)

bins = [0,25000,50000,75000,100000,125000,150000,175000,200000,225000,250000,275000,300000,325000,350000,375000,400000,425000,450000,475000,500000,10000000000]
slot = ['0-25000', '25000-50000','50000-75000','75000,100000','100000-125000', '125000-150000', '150000-175000','175000-200000',
       '200000-225000','225000-250000','250000-275000','275000-300000','300000-325000','325000-350000','350000-375000',
       '375000-400000','400000-425000','425000-450000','450000-475000','475000-500000','500000 and above']

df1['AMT_INCOME_RANGE'] = pd.cut(df1['AMT_INCOME_TOTAL'], bins=bins, labels=slot)


# In[255]:


df1["AMT_INCOME_RANGE"].head()


# In[256]:


#Creating bins for Credit amount (AMT_CREDIT)

bins = [0,150000,200000,250000,300000,350000,400000,450000,500000,550000,600000,650000,700000,750000,800000,850000,900000,1000000000]
slots = ['0-150000', '150000-200000','200000-250000', '250000-300000', '300000-350000', '350000-400000','400000-450000',
        '450000-500000','500000-550000','550000-600000','600000-650000','650000-700000','700000-750000','750000-800000',
        '800000-850000','850000-900000','900000 and above']

df1['AMT_CREDIT_RANGE'] = pd.cut(df1['AMT_CREDIT'], bins=bins, labels=slots)


# In[257]:


df1["AMT_CREDIT_RANGE"].head()


# In[258]:


#Dividing the dataset into two datasets of  target=1 (client with payment difficulties) and target=0 (all other cases)
#We will be using these two datasets for few comparisons
target0 = df1[df1["TARGET"]==0]
target1 = df1[df1["TARGET"]==1]


# In[259]:


print(target0.shape)
print(target1.shape)


# In[340]:


#Calculating Imbalance percentage for target 0 and target 1. 
#Visualizing the above result in a pie plot

total = len(df1["TARGET"])
explode = [0, 0.05]

def my_fmt(x):
    return '{:.2f}%\n({:.0f})'.format(x, total*x/100) #to print both the percentage and value together





plt.figure(figsize = [6, 6])
plt.title("Imbalance between target0 and target1")
df1["TARGET"].value_counts().plot.pie(autopct = my_fmt, colors = ["blue", "green"], explode = explode)

plt.show()


# In[262]:


##8.79% clients has payment issues


# In[271]:


##Plotting graphs for Target0



# In[275]:


#creating a function for plotting (to reduce repetitive code)
def functionPlot(df, col, title, xtitle, ytitle, hue = None):
    
    sns.set_style("white")
    sns.set_context("notebook")    
    
    temp = pd.Series(data = hue)
    fig, ax = plt.subplots()
    width = len(df[col].unique()) + 7 + 4*len(temp.unique())
    fig.set_size_inches(width , 8)
    plt.xticks(rotation = 45)
    plt.yscale('log')
    plt.title(title)
    ax = sns.countplot(data = df, x= col, order=df[col].value_counts().index,hue = hue, palette='deep') 
    ax.set(xlabel = xtitle, ylabel = ytitle)    
    plt.show()
    
    
    
    


# In[276]:


# PLotting for income range (AMT_INCOME_RANGE) (Segregated based on gender)

functionPlot(target0, col='AMT_INCOME_RANGE', 
             title='Distribution of Income Range (Repayers)',
             hue='CODE_GENDER', xtitle = "Income Range", ytitle = "Count")


# Females counts are more then males.
# 
# Income range from 100000 to 250000 is having more count of loans.
# 
# In the slots 250000-275000 and 375000-400000,the count are same almost for male and female.
# 

# In[277]:


# Plotting for Income type (NAME_INCOME_TYPE) (Segregated based on gender)

functionPlot(target0, col='NAME_INCOME_TYPE', title='Distribution of Income type (Repayers)', hue='CODE_GENDER', xtitle = "Income type of the client", ytitle = "Count")


# working people took more loans among all. 
# 
# female students lit less in taking loan in student segments else they are top in taking loans in working, commerical and state servants.
# 
# females clients are more tendency to take loan. 

# In[278]:


# Plotting for Contract type (NAME_CONTRACT_TYPE) (Segregated based on gender)

functionPlot(target0, col='NAME_CONTRACT_TYPE', title='Distribution of contract type (Segregated based on gender)', hue='CODE_GENDER', xtitle = "Type of Contract", ytitle = "Count")


# 
# 
# 
# in both cases female clients are on top..
# cash loans has more clients compared to revolving loans.

# In[279]:


# Plotting for Organization type

sns.set_style('darkgrid')
sns.set_context('notebook')
plt.figure(figsize = [15,30])

plt.title("Distribution of Organization type for target0 (All other cases)")
plt.xscale('log')

sns.countplot(data=target0,y='ORGANIZATION_TYPE',order=target0['ORGANIZATION_TYPE'].value_counts().index, palette='deep')

plt.show()


# Clients which have applied for credits are from most of the organization type ‘Business entity Type 3’ , ‘Self employed’, ‘Other’ , ‘Medicine’, ‘Government’ and 'Business entity type2'.
# Fewer clients are from Industries type 8, type 5, Industry: type 13, Trade: type4, Religion, Industry type 6 and type 10.

# Plotting graphs for Target1

# In[280]:


# PLotting for income range (Segregated based on gender)

functionPlot(target1, col='AMT_INCOME_RANGE', title='Distribution of Income Range (Customers with payment difficulties)', hue='CODE_GENDER', xtitle = "Income Range", ytitle = "Count")


# Income range from 100000 to 200000 is having the highest number of credits.
# Very less count for income range 400000 and above.
# On average, there are more number of male clients where the number of credits are less.

# In[281]:


# Plotting for Income type (Segregated based on house ownership)

functionPlot(target1, col='NAME_INCOME_TYPE', title='Distribution of Income type (Customers with payment difficulties)', hue='FLAG_OWN_REALTY', xtitle = "Income type of the client", ytitle = "Count")


# Working customers, obviously, have a higher count.
# As we can see, most customers do have their own property (house or a flat) but a large number of customers can be stated as otherwise.

# In[282]:


# Plotting for Contract type (Segregated based on education level)

functionPlot(target1, col='NAME_CONTRACT_TYPE', title='Distribution of Contract Type (Customers with payment difficulties)', hue='NAME_EDUCATION_TYPE', xtitle = "Type of contract", ytitle = "Count")


# Cash loans, as we can see, are preferred by clients of all education backgrounds with an overwhelming majority.
# People with only an academic degree do not prefer revolving loans at all.

# In[283]:


# Plotting for Organization type

sns.set_style('darkgrid')
sns.set_context('notebook')
plt.figure(figsize=(15,30))

plt.title("Distribution of Organization type of Clients with payment difficulties (Target1)")

plt.xticks(rotation=90)
plt.xscale('log')

sns.countplot(data = target1, y = 'ORGANIZATION_TYPE', order = target1['ORGANIZATION_TYPE'].value_counts().index, palette='deep')

plt.show()


# As compared to the clients with NO payment difficulties, clients WITH payment difficulties have the 'construction' business type in the top 5 count replacing the 'medicine' business type.
# 
# Most of the business types are the same as clients with NO payment difficulties, except we have the business type 'Transport: type1' in the case of clients WITH payment difficulties which wasn't present before.

# In[ ]:





# In[ ]:





# In[294]:


plt.figure(figsize = [20, 6])

plt.suptitle("Distribution of clients with difficulties and all other cases")

plt.subplot(1,2,1)
ax = df1["TARGET"].value_counts().plot(kind = "barh", colormap = "summer")

plt.subplot(1,2,2)
df1["TARGET"].value_counts().plot.pie(autopct = "%.2f%%", startangle = 60, colors = ["teal", "gold"])



for i,j in enumerate(df1["TARGET"].value_counts().values):
    ax.text(.7, i, j, weight = "bold")

plt.show()


# 8.79% (18547) out of total client population (192573) have difficulties in repaying loans

# # Joining applicationData and previousApplication

# In[295]:


#Joining the two data sets by a common column (SK_ID_CURR) for further comparison and analysis

data = pd.merge(df1, df3, on = 'SK_ID_CURR', how = 'inner')
data.sort_values(by = ['SK_ID_CURR','SK_ID_PREV'], ascending = [True, True], inplace = True)


# In[296]:


data.head(10)


# In[297]:


#Distribution of Contract type
plt.figure(figsize = [14, 6])
plt.subplot(1,2,1)
plt.title("distribution of contract types in data (combined dataset)")
data["NAME_CONTRACT_TYPE_x"].value_counts().plot.pie(autopct = "%1.0f%%", startangle = 60, colors = ["teal", "gold"])

plt.show()


# The percentage of revolving loans and cash loans are 8% & 92%.
# 

# In[298]:


## Gender Distribution in the combined dataset

fig = plt.figure(figsize=(13,6))
explode = [0, 0.05]

plt.subplot(1,2,1)
data["CODE_GENDER"].value_counts().plot.pie(autopct = "%1.0f%%", colors = ["teal", "gold"], explode = explode)
plt.title("Distribution of gender")
plt.show()


# in the applicationData file, we saw females had 61% and males had 39% but now in the combined dataset we see:- Females: 62% Males: 38%

# In[332]:





# In[ ]:





# In[304]:


fig = plt.figure(figsize = [15,6])
explode = (0, 0.1)

plt.subplot(1,2,1)
plt.title("Distribution of Client by car ownership", weight = "bold")
data["FLAG_OWN_CAR"].value_counts().plot.pie(autopct = "%1.0f%%", colors=["teal", "gold"], explode = explode, startangle = 60)

plt.subplot(1,2,2)
plt.title("Distribution of Client by car ownership based on repayment status", weight = "bold")
data[data["FLAG_OWN_CAR"] == "Y"]["TARGET"].value_counts().plot.pie(autopct = "%1.0f%%", colors=["brown","grey"], explode = explode)
plt.show()


# 1st pie plot : Only 38% of clients own a car .
# 
# 2nd pie plot : Only 8% of clients who own a car have difficulty in payments

# In[305]:


#Distribution of client owning a house or flat and by target

#FLAG_OWN_REALTY - Flag if client owns a house or flat
fig = plt.figure(figsize = [15,6])
explode = [0, 0.05]

plt.subplot(1,2,1)
plt.title("Distribution of Client by house ownership", weight = "bold")
data["FLAG_OWN_REALTY"].value_counts().plot.pie(autopct = "%1.0f%%", colors = ["teal","gold"], startangle = 60, explode = explode)


plt.subplot(1,2,2)
plt.title("Distribution of client by house ownership based on repayment status", weight = "bold")
data[data["FLAG_OWN_REALTY"] == "Y"]["TARGET"].value_counts().plot.pie(autopct = "%1.0f%%", colors = ["brown","grey"], explode = explode)

plt.show()


# SUBPLOT 1 : 71% of clients own a house or a flat.
# 
# SUBPLOT 2 : Out of all the clients who own a house, 9% of clients have difficulty in making payments.

# In[ ]:





# In[ ]:





# In[310]:


#NAME_INCOME_TYPE: Client's income type
plt.figure(figsize = [22, 8])

plt.subplot(1,2,1)
plt.title("Distribution of client income type",  weight = "bold")
ax = sns.countplot(y = data["NAME_INCOME_TYPE"], palette = "deep", order = data["NAME_INCOME_TYPE"].value_counts().index[:4])
ax.set(xlabel = "Count", ylabel = "Income Type")

plt.subplot(1,2,2)
plt.title("Distribution of client income  type by target (repayment status)",  weight = "bold")
ax = sns.countplot(y = data["NAME_INCOME_TYPE"],  hue = data["TARGET"], palette="deep", order = data["NAME_INCOME_TYPE"].value_counts().index[:4])
ax.set(xlabel = "Count", ylabel = "")

plt.show()


# Most clients as per both cases of repayment status, are working.
# Conversely, the least amount of clients are pensioners (retired clients)

# In[311]:


#Distribution of Education type by repayment status


explode = [0, 0.05, 0.08, 0.08, 0.08]

plt.figure(figsize = [20, 8])
plt.subplot(1,2,1)
plt.title("Distribution of Education for Repayers",  weight = "bold")
data[data["TARGET"] == 0]["NAME_EDUCATION_TYPE"].value_counts().plot.pie(fontsize=12, autopct = "%1.0f%%", explode = explode)

plt.subplot(1,2,2)
plt.title("Distribution of Education for Defaulters",  weight = "bold")
data[data["TARGET"] == 1]["NAME_EDUCATION_TYPE"].value_counts().plot.pie(fontsize=12, autopct = "%1.0f%%", explode = explode)

plt.show()


# Clients who default are proportionally 9% higher compared to clients who do not default (for clients with education as secondary).
# In the higher education category, clients who default are 8% fewer.
# In both cases of repayment status, lower secondary and academic degree categories are the minority.

# In[ ]:





# In[316]:


#NAME_FAMILY_STATUS - Family status of the client

plt.figure(figsize = [16, 8])
plt.subplot(1,2,1)
plt.title("Distribution of Family status for Repayers (Target0)",  weight = "bold")
data[data["TARGET"]==0]["NAME_FAMILY_STATUS"].value_counts().plot.pie(autopct = "%1.0f%%")

plt.subplot(1,2,2)
plt.title("Distribution of Family status for Defaulters (Target1)", weight = "bold")
data[data["TARGET"]==1]["NAME_FAMILY_STATUS"].value_counts().plot.pie(autopct = "%1.0f%%")

plt.show()


# There's a difference of -4% in married clients who have difficulty in making payments.
# Family status for both cases of repayment status have an almost evenly distributed family status (family members living with the client)

# In[317]:


# Box plotting for Credit amount and Housing type (Segregated by repyament status (Target))

plt.figure(figsize = [16,12])
plt.title('Credit amount vs Housing type',  weight = "bold")

sns.barplot(data = data, x = 'NAME_HOUSING_TYPE', y = 'AMT_CREDIT_x', hue = 'TARGET', palette = "deep")
plt.xticks(rotation = 0)

plt.xlabel("Housing type", weight = "bold")
plt.ylabel("Credit Amount", weight = "bold", rotation = 0)

plt.show()


# Clients with office, co-op, municipal aparments have the highest repayers.
# Clients living with parents or in a parents' aparment have the least amount of repayers and defaulters.

# In[319]:


####Distribution of Loan purpose (Segregated by repyament status (Target)


#Using log scale for distribution
sns.set_style('dark')
sns.set_context('notebook')

plt.figure(figsize = [15, 30])
plt.xscale('log')
plt.title('Distribution of purposes with target (Repayment status)',  weight = "bold")

ax = sns.countplot(data = data, y = 'NAME_CASH_LOAN_PURPOSE', order = data['NAME_CASH_LOAN_PURPOSE'].value_counts().index, hue = 'TARGET', palette = 'deep') 
plt.ylabel("Purpose of Loan", weight = "bold")
plt.xlabel("Count", weight = "bold")

plt.legend(loc = "right")
plt.show()


# Repair purposes are on top with most defaulters and repayers.
# Proportion wise, there are high amount of repayers when the client refuses to name the purpose of the loan. Although such clients are rare.

# In[320]:


###Distribution of contract status

sns.set_style('dark')
sns.set_context('notebook')

plt.figure(figsize = [15, 30])
plt.xscale('log')
plt.title('Distribution of purposes with target (Repayment status)',  weight = "bold")

ax = sns.countplot(data = data, y = 'NAME_CASH_LOAN_PURPOSE', order = data['NAME_CASH_LOAN_PURPOSE'].value_counts().index, hue = 'NAME_CONTRACT_STATUS', palette = 'deep') 
plt.ylabel("Purpose of Loan", weight = "bold")
plt.xlabel("Count", weight = "bold")

plt.show()


# Most rejection of loans is when the purpose of the client is based on Repairs.
# For education purposes we have equal number of approvals and refusals.

# # Correlation variables

# In[321]:


repayerData = data[data['TARGET'] == 0]
defaulterData = data[data['TARGET'] == 1]


# In[322]:


#to find the most correlated columns (positive and negative)
repayerData.corr().unstack().sort_values(ascending = False).drop_duplicates()


# In[323]:


#making a dataframe with only the columns with high correlation
top10_CorrTarget0 = repayerData[["OBS_30_CNT_SOCIAL_CIRCLE", "OBS_60_CNT_SOCIAL_CIRCLE", "AMT_APPLICATION", "DAYS_TERMINATION", "DAYS_LAST_DUE", "CNT_FAM_MEMBERS", "CNT_CHILDREN", "REG_REGION_NOT_WORK_REGION", "LIVE_REGION_NOT_WORK_REGION", "DEF_30_CNT_SOCIAL_CIRCLE", "DEF_60_CNT_SOCIAL_CIRCLE", "AMT_GOODS_PRICE_y", "REG_CITY_NOT_WORK_CITY", "LIVE_CITY_NOT_WORK_CITY", "AMT_CREDIT_y", "AMT_ANNUITY_y"]].copy()


# In[324]:


top10_CorrTarget0.shape


# In[325]:


#Visually showcasing the top10 correlated columns through a heatmap

corr_target0 = top10_CorrTarget0.corr()

plt.figure(figsize = [15, 15])
sns.heatmap(data = corr_target0, cmap="Blues", annot=True)

plt.show()

AMT_GOODS_PRICE and AMT_APPLICATION have a high correlation, which means the more credit the client asked for previously is proportional to the goods price that the client asked for previously.
AMT_ANNUITY and AMT_APPLICATION also have a high correlation, which means the higher the loan annuity issued, the higher the goods price that the client asked for previously.
If the client's contact address does not match the work address, then there's a high chance that the client's permanent address also does not match the work address.
First due of the previous application is highly correlated with Relative to the expected termination of the previous application
CNT_CHILDREN and CNT_FAM_MEMBERS are highly correlated which means a client with children is higly likely to have family members as well.
# In[326]:


defaulterData.corr().unstack().sort_values(ascending = False).drop_duplicates()


# In[327]:


#Adding the top10 correlated columns into a new dataframe:
top10_CorrTarget1 = data[["OBS_60_CNT_SOCIAL_CIRCLE", "OBS_30_CNT_SOCIAL_CIRCLE", "AMT_APPLICATION", "AMT_CREDIT_y", "DAYS_TERMINATION", "DAYS_LAST_DUE", "CNT_FAM_MEMBERS", "CNT_CHILDREN", "LIVE_REGION_NOT_WORK_REGION", "REG_REGION_NOT_WORK_REGION", "DEF_30_CNT_SOCIAL_CIRCLE", "DEF_60_CNT_SOCIAL_CIRCLE", "AMT_ANNUITY_y", "LIVE_CITY_NOT_WORK_CITY", "REG_CITY_NOT_WORK_CITY", "AMT_GOODS_PRICE_y", "AMT_ANNUITY_x", "AMT_CREDIT_x"]].copy()


# In[328]:


corr_target1 = top10_CorrTarget1.corr()

plt.figure(figsize = [15, 15])
sns.heatmap(data = corr_target1, cmap="Blues", annot=True)
plt.show()

In comparison to the repayer heatmap, AMT_GOODS_PRICE and AMT_APPLICATION have a high correlation here as well, which means the more credit the client asked for previously is proportional to the goods price that the client asked for previously.
In comparison to the repayer heatmap, AMT_ANNUITY and AMT_APPLICATION also have a high correlation, which means the higher the loan annuity issued, the higher the goods price that the client asked for previously.
In comparison to the repayer heatmap, If the client's contact address does not match the work address, then there's a high chance that the client's permanent address also does not match the work address.
Higher the goods price, higher the credit by the client
First due of the previous application is highly correlated with Relative to the expected termination of the previous application (same as with the repayer heatmap)
CNT_CHILDREN and CNT_FAM_MEMBERS are highly correlated which means a client with children is higly likely to have family members as well (same as with the repayer heatmap)
# 1. Clients who are Students, Pensioners and Commercial Associates with a housing type such as office/co-op/municipal apartments NEED TO BE targeed by the bank for successful repayments. These clients have the highest amount of repayment history.
# 2. Female clients on maternity leave should NOT be targeted as they have no record of repayments (therefore they are highly likely to default and targeting them would lead to a loss)
# 3. While clients living with parents have the least amount of repayers, they also have the least amount of defaulters. So, in cases where the risk is less, such clients can be targeted.
# 4. Clients who are working need to be targeted LESS by the bank as they have the highest amount of defaulters.
# 
# 5. Clients should NOT be targeted based on their education type alone as the data is very inconclusive.
# 6. Banks should target clients who own a car.
# 7. There are NO repayers/negligible repayers when the contract type is of revolving loan.
# 8. Banks should target more people with no children.
# 9. 'Repairs' purpose of loan is the one with the most defaulters and repayers. Therefore, clients with very low risk SHOULD be given loans for such purpose to yield high profits.
# 
# 
# 10. Banks should also target female clients as they are the highest repayers (almost as double as males) amongst both the genders.

# In[337]:





# In[338]:





# In[ ]:





# In[ ]:




