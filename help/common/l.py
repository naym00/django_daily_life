import datetime

class L:
    def listToTuple(self, demoList):
        return tuple(map(lambda a: (a, a), demoList))
    
    def uniqueNumber(self):
        datetime_now = str(datetime.datetime.now())
        return datetime_now.replace(' ', '').replace('-', '').replace(':', '').replace('.', '')