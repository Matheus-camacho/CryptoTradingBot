import gdax

class gdaxBroker(object):
	"""docstring for broker"""

	#TODO: authentication and private methods
	def __init__(self):
		super(gdaxBroker, self).__init__();
		self.publicClient=gdax.PublicClient();

	def getProducts(self):
		return self.publicClient.get_products();

	def getOrderBook(self,product,level=1):
		return self.publicClient.get_product_order_book(product,level=level);

	def getTicker(self,product):
		return self.publicClient.get_product_ticker(product);

	def getHistoric(self,product,granularity):
		return self.publicClient.get_product_historic_rates(product,granularity); 

	def getTime(self):
		return self.publicClient.get_time();

	def getReferenceList(self):
		prod=self.getProducts();
		for x in prod:
			referenceList=[];
			if (x['quote_currency']=="USD"):
				referenceList.append(x["id"]);

		return referenceList




	
