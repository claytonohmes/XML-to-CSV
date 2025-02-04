import csv
import xml.etree.ElementTree as ET
from ReasonCode import ReasonCode

def able_config_to_csv_alarm_list(file, csvfile):
    '''
    the purpose of this function is to take the ABLE config alarms and output a csv file. 
    '''
    #parse the xml file
    tree = ET.parse(file)
    root = tree.getroot()

    #get the site name
    site_name = root.get('name')

    #get the reason lists
    reason_lists = root.findall(".//reasonlist")
    reason_list_names = []

    #get the names of the reason lists
    for item in reason_lists:
        reason_list_names.append(item.get('name'))

    #create a dictionary to store the reason codes
    reason_dict = {}

    #iterate through the reason lists and get the reason codes
    for name in reason_list_names:
        reasons = root.findall(f".//*[@name='{name}']/reason")
        for reason in reasons:
            reasonclass = ReasonCode(site_name, name, reason.get('reasonlevel1'),reason.get('reasonlevel2'),reason.get('reasonlevel3'),reason.get('opccode'),reason.get('superreason'))
            reason_dict.setdefault(f"{site_name}|{name}", []).append(reasonclass)

    #write the reason codes to a csv file
    fieldnames = ['reas_group','reas_desc', 'state', 'category1','spare4']

    with open(csvfile, 'w', newline='') as alarmlist:
        writer = csv.DictWriter(alarmlist, fieldnames=fieldnames)
        print('File Created.')
        # Write header row
        writer.writeheader()
        print('Starting File Write.')
        # Write data rows
        for _, value in reason_dict.items():
            for item in value:
                if item.reas2 == None and item.reas3 != None:
                    print("No good! Orphan Reason 3: " + str(item))
                
                if item.reas2 == None:
                    #reason level 2 none
                    writer.writerow({'reas_group': f"{item.siteName}|{item.reasArea}",
                                     'reas_desc': f"{item.reas1}",
                                     'state': 'DOWNTIME',
                                     'category1': f"{item.category}",
                                     'spare4': f"{item.opccode}"})
                elif item.reas3 == None:
                    #reason leval 3 none
                    writer.writerow({'reas_group': f"{item.siteName}|{item.reasArea}|{item.reas1}",
                                     'reas_desc': f"{item.reas2}",
                                     'state': 'DOWNTIME',
                                     'category1': f"{item.category}",
                                     'spare4': f"{item.opccode}"})
                else:
                    writer.writerow({'reas_group': f"{item.siteName}|{item.reasArea}|{item.reas1}|{item.reas2}",
                                     'reas_desc': f"{item.reas3}",
                                     'state': 'DOWNTIME',
                                     'category1': f"{item.category}",
                                     'spare4': f"{item.opccode}"}) 
    
if __name__ == "__main__":
    able_config_to_csv_alarm_list('idc - Belle 20250124 - 03.xml', 'alarmList.csv')