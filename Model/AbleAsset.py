import Alarm, AlarmList
import xml.etree.ElementTree as ET

class Asset:
    def __init__(self, name, asset_type, xmlFile):
        self.name = name
        self.asset_type = asset_type
        self.xmlFile = xmlFile
        self.alarmList = AlarmList(name)

    def get_alarms(self):
        tree = ET.parse(self.xmlFile)
        root = tree.getroot()
        asset = root.findall(f".//asset[@name='{self.name}']")
        reasonlist = asset.get('reasonlist')
        alarms = root.findall(f".//reasonlist[@name='{reasonlist}']/reason")

        for alarm in alarms:
            site = root.get('name')
            area = asset.get('area')
            reason1 = alarm.get('reasonlevel1')
            reason2 = alarm.get('reasonlevel2')
            reason3 = alarm.get('reasonlevel3')
            opccode = alarm.get('opccode')
            superreason = alarm.get('superreason')
            code = Alarm(site, area, reason1, reason2, reason3, opccode, superreason)
            self.alarmList.append(code)