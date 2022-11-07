#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import norm
import math as m
from datetime import datetime, date
import pandas as pd
import pandas_datareader.data as web


# In[2]:


stockPrices = {
    "commServ" : {"AT&T":15.34, "Disney":96.64, "Paramount Global":19.04, "Dish Network":13.83},
    "fin" : {"Capital One":92.17, "JPMorgan Chase":116.11, 'American Express':141.30, "Goldman Sachs":293.05},
    "industrials" : {"Boeing":121.08, "Delta Airlines":28.06, "General Electric":61.91, "American Airlines":13.10},
    "infoTech" : {"Apple":138.20, "PayPal":86.07, "Salesforce":143.84, "Adobe":275.20}
    }


atnt = pd.read_csv('T.csv')
disney = pd.read_csv('DIS.csv')
para = pd.read_csv('PARA.csv')
dish = pd.read_csv('DISH.csv')
capital = pd.read_csv('COF.csv')
jpm = pd.read_csv('JPM.csv')
axp = pd.read_csv('AXP.csv')
gs = pd.read_csv('GS.csv')
boeing = pd.read_csv('BA.csv')
delta = pd.read_csv('DAL.csv')
ge = pd.read_csv('GE.csv')
aal = pd.read_csv('AAL.csv')
apple = pd.read_csv('AAPL.csv')
pypl = pd.read_csv('PYPL.csv')
sforce = pd.read_csv('CRM.csv')
adobe = pd.read_csv('ADBE.csv')


# In[3]:


def d1(S,K,T,r,sigma):
    d1 = (m.log(S/K)+(r+sigma**2/2.)*T)/(sigma*m.sqrt(T))
    return d1

def d2(S,K,T,r,sigma):
    d2 = d1(S,K,T,r,sigma)-sigma*m.sqrt(T)
    return d2

def nd1(d1):
    nd1 = norm.cdf(d1)
    return nd1

def nd2(d2):
    nd2 = norm.cdf(d2)
    return nd2
    
def call_premium(S,K,T,r,sigma):
    c = nd1(d1(S,K,T,r,sigma))*S - nd2(d2(S,K,T,r,sigma))*(K/(m.e**(r*T)))
    return c
    


# In[4]:



stock = 'AAL' #enter any stock ticker
expiry = '03-17-2023'

today = datetime.now()
one_year_ago = today.replace(year=today.year-1)

df = web.DataReader(stock, 'yahoo', one_year_ago, today)

df = df.sort_values(by="Date")
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)


rf = (web.DataReader(
    "^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1])/100 #risk free interest rate
sigma = np.sqrt(252) * df['returns'].std()
strike_price = 230 #enter any strike price
current = df['Close'].iloc[-1]
t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365
print(sigma)
#print('The Option Price is: ', call_premium(current, strike_price, t , rf, sigma))


# In[5]:


atnt = atnt.drop(['Date','Close','Change'], axis = 1)
disney = disney.drop(['Date','Close','Change'], axis = 1)
para = para.drop(['Date','Close','change'], axis = 1)
dish = dish.drop(['Date','Close','change'], axis = 1)
jpm = jpm.drop(['Date','Close','change'], axis = 1)
axp = axp.drop(['Date','Close','change'], axis = 1)
boeing = boeing.drop(['Date','Close','change'], axis = 1)
delta = delta.drop(['Date','Close','change'], axis = 1)
sforce = sforce.drop(['Date','Close','CHANGE'], axis = 1)
adobe = adobe.drop(['Date','Close','Change'], axis = 1)
ge = ge.drop(['Date','Close','change'], axis = 1)
gs = gs.drop(['Date','Close','change'], axis = 1)
apple = apple.drop(['Date','Close','Change'], axis = 1)
pypl = pypl.drop(['Date','Close','change'], axis = 1)
aal = aal.drop(['Date','Close','change'], axis = 1)
capital = capital.drop(['Date','Close','change'], axis = 1)


# In[6]:


disney.iloc[:,0] = disney.iloc[:,0].apply(pd.to_numeric, errors='ignore')
atnt.iloc[:,0] = atnt.iloc[:,0].apply(pd.to_numeric, errors='ignore')
para.iloc[:,0] = para.iloc[:,0].apply(pd.to_numeric, errors='ignore')
dish.iloc[:,0] = dish.iloc[:,0].apply(pd.to_numeric, errors='ignore')
jpm.iloc[:,0] = jpm.iloc[:,0].apply(pd.to_numeric, errors='ignore')
axp.iloc[:,0] = axp.iloc[:,0].apply(pd.to_numeric, errors='ignore')
boeing.iloc[:,0] = boeing.iloc[:,0].apply(pd.to_numeric, errors='ignore')
delta.iloc[:,0] = delta.iloc[:,0].apply(pd.to_numeric, errors='ignore')
sforce.iloc[:,0] = sforce.iloc[:,0].apply(pd.to_numeric, errors='ignore')
adobe.iloc[:,0] = adobe.iloc[:,0].apply(pd.to_numeric, errors='ignore')
ge.iloc[:,0] = ge.iloc[:,0].apply(pd.to_numeric, errors='ignore')
gs.iloc[:,0] = gs.iloc[:,0].apply(pd.to_numeric, errors='ignore')
apple.iloc[:,0] = apple.iloc[:,0].apply(pd.to_numeric, errors='ignore')
pypl.iloc[:,0] = pypl.iloc[:,0].apply(pd.to_numeric, errors='ignore')
aal.iloc[:,0] = aal.iloc[:,0].apply(pd.to_numeric, errors='ignore')
capital.iloc[:,0] = capital.iloc[:,0].apply(pd.to_numeric, errors='ignore')


# In[7]:


strikeatnt = []
strikedisney = []
strikepara = []
strikedish = []
strikejpm = []
strikeaxp = []
strikegs = []
strikege = []
strikecof = []
strikecrm = []
strikeaapl = []
strikepypl = []
strikeba = []
strikedal = []
strikeaal = []
strikeadobe = []

for sp in atnt.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikeatnt.append(sp)

for sp in ge.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikege.append(sp)

for sp in disney.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikedisney.append(sp)

for sp in para.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikepara.append(sp)
    
for sp in delta.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikedal.append(sp)
    
for sp in boeing.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikeba.append(sp)
    
for sp in apple.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikeaapl.append(sp)
    
for sp in aal.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikeaal.append(sp)
    
for sp in axp.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikeaxp.append(sp)
    
for sp in jpm.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikejpm.append(sp)
    
for sp in sforce.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikecrm.append(sp)
    
for sp in capital.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikecof.append(sp)
    
for sp in dish.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikedish.append(sp)
    
for sp in pypl.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikepypl.append(sp)
    
for sp in gs.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikegs.append(sp)

for sp in adobe.iloc[1:,0]:
    if m.isnan(sp) == False:
        strikeadobe.append(sp)
    
predATNT = []
predDISNEY  = []
predPARA = []
predDISH = []
predAXP = []
predJPM = []
predGS = []
predCOF = []
predBA = []
predDAL = []
predAAL = []
predGE = []
predAAPL = []
predPYPL = []
predCRM = []
predADOBE = []
    
R = 0.038 #approximate
T = 0.5

for sp in strikeatnt:
    predATNT.append(call_premium(stockPrices["commServ"]['AT&T'], sp, T , R, 0.266572525))

for sp in strikedisney:
    predDISNEY.append(call_premium(stockPrices["commServ"]['Disney'], sp, T , R, 0.317694567))
    
for sp in strikepara:
    predPARA.append(call_premium(stockPrices["commServ"]['Paramount Global'], sp, T , R, 0.499767388))
    
for sp in strikedish:
    predDISH.append(call_premium(stockPrices["commServ"]['Dish Network'], sp, T , R, 0.580966578))

for sp in strikecof:
    predCOF.append(call_premium(stockPrices["fin"]['Capital One'], sp, T , R, 0.384996668))
    
for sp in strikeaxp:
    predAXP.append(call_premium(stockPrices["fin"]['American Express'], sp, T , R, 0.3628258778574487))
    
for sp in strikejpm:
    predJPM.append(call_premium(stockPrices["fin"]['JPMorgan Chase'], sp, T , R, 0.2935601946637155))
    
for sp in strikegs:
    predGS.append(call_premium(stockPrices["fin"]['Goldman Sachs'], sp, T , R, 0.291868415))
    
for sp in strikeba:
    predBA.append(call_premium(stockPrices["industrials"]['Boeing'], sp, T , R, 0.459194432))
    
for sp in strikedal:
    predDAL.append(call_premium(stockPrices["industrials"]['Delta Airlines'], sp, T , R, 0.473444318))
    
for sp in strikeaal:
    predAAL.append(call_premium(stockPrices["industrials"]['American Airlines'], sp, T , R, 0.5764688267150839))
    
for sp in strikege:
    predGE.append(call_premium(stockPrices["industrials"]['General Electric'], sp, T , R, 0.336833244))
    
for sp in strikeaapl:
    predAAPL.append(call_premium(stockPrices["infoTech"]['Apple'], sp, T , R, 0.319472125))
    
for sp in strikepypl:
    predPYPL.append(call_premium(stockPrices["infoTech"]['PayPal'], sp, T , R, 0.572627466))
    
for sp in strikecrm:
    predCRM.append(call_premium(stockPrices["infoTech"]['Salesforce'], sp, T , R, 0.440401275))

for sp in strikeadobe:
    predADOBE.append(call_premium(stockPrices["infoTech"]['Adobe'], sp, T , R, 0.447453299))
    

    


# In[8]:


GS = pd.DataFrame(predGS)
GS.to_csv('PREDGS.csv')


# In[133]:


call_premium(stockPrices["commServ"]['Dish Network'], 16, T , R, 0.580966578)


# In[177]:


call_premium(stockPrices["industrials"]['General Electric'], 72, T , R, 0.336833244)


# In[ ]:




