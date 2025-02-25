import Alarm

class AlarmList:
    def __init__(self, assetName):
        self.alarms = []
        self.name = assetName

    def append(self, Alarm):
        self.alarms.append(Alarm)