import algorithm
import gdax
import rollingAverages
import pandas as pd
import listGenerator
import time
public_client = gdax.PublicClient()



priceList=public_client.get_product_historic_rates('BTC-USD', granularity=3600)

frame=pd.DataFrame(priceList).iloc[:,4]

roll=rollingAverages.rollingAverages(25,70)

results=[];

for i in range(80,350):
    res=roll.rollingAverageDifference(frame,i);
    results.append(res);
    
lis=([],[]);  

gen=listGenerator.listGenerator();
    
for i in range(20):
    lis=gen.updateLists(lis,"BTC-USD");
    time.sleep(10)
    