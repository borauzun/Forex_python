from datetime import datetime, timedelta
class Position:
    def setPosition(self,openDT,openPrice,targetPrice,stopLoss,closePrice):
        self.openDT=openDT
        self.openPrice=openPrice
        self.targetPrice=targetPrice
        self.stopLoss=stopLoss
        self.closePrice=closePrice

def main():
    past = datetime.now() - timedelta(days=1)
    present = datetime.now()
    print(past < present)
    print(present-past)

    p1=Position()
    #p1.openDT='01.01.2010'
    #p1.closePrice=2
    dt='2011.01.02,17:02,1.541300'
    #datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    datetime_object = datetime.strptime(dt, '%Y.%m.%d,%H:%M,%S.%f')
    p1.setPosition(datetime.now(),2.5,2.6,2.4,None)
    p1.openDT=datetime_object
    print(p1.openDT)
    print(p1.closePrice)


if __name__ == '__main__':main()