import priceGetter
import gdaxBroker

import gdax

class rollingAverages(object):
    """docstring for algorithm"""

    def __init__(self, size1, size2):
        super(rollingAverages, self).__init__();
        
        self.size1 = size1;
        self.size2 = size2;
        

    def calculateRollingAverage(self, priceList, time):

        rollingAverage1 = 0;
        rollingAverage2 = 0;
        
        for i in range(self.size1):
            rollingAverage1 += float(priceList[time - i ]);
        rollingAverage1 = rollingAverage1 / self.size1;

        for i in range(self.size2):
            rollingAverage2 += float(priceList[time - i ]);
        rollingAverage2 = rollingAverage2 / self.size2;
        
        return (rollingAverage1, rollingAverage2)

    def rollingAverageDifference(self, priceList, time):
        ra = self.calculateRollingAverage(priceList, time);
        return (ra[0] - ra[1]);
