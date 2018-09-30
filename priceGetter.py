import gdax
import gdaxBroker
import pandas as pd

class priceGetter(object):
	"""docstring for dataTreatment"""
	def __init__(self):
		super(priceGetter, self).__init__();
		self.broker=gdaxBroker.gdaxBroker();

	def getAsk(self,product):
                    
                    try:
                        return float(self.broker.getTicker(product)["ask"]);
                    except: 
                        return self.getAsk(product)

	def getBid(self,product):
                    try:
                       return float(self.broker.getTicker(product)["bid"]);	
                    except:
                        return self.getBid(product)

	def getSpread(self,product):
		return self.getAsk(product)-self.getBid(product);

	def getSize(self,product):
		return self.broker.getTicker(product)["size"];	




		