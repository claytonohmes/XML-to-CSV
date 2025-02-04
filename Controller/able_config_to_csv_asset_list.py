import csv
import xml.etree.ElementTree as ET
from Model.Asset import Asset

def able_config_to_csv_asset_list(file, csvfile):
    '''
    the purpose of this function is to take the ABLE config alarms and output a csv file. 
    '''
    #parse the xml file
    tree = ET.parse(file)
    root = tree.getroot()

    #get the site name
    site_name = root.get('name')

    #get the reason lists
    asset_list = root.findall(".//asset")
    assets = []

    #iterate through the reason lists and get the reason codes
    for asset in asset_list:
        '''
        <asset name="Retort" 
        devicename="ROL_RT" 
        type="LINE" 
        scanpriority="10" 
        defaultplc="Concentrator PLC" 
        reasonlist="Retort" 
        defaultreason="Retort" 
        area="Retort" 
        templateref="LineWithUserCommands" 
        primaryref="Retort">
        '''
        assetClass = Asset(site_name
                      , asset.get('name')
                      , asset.get('devicename')
                      , asset.get('type')
                      , asset.get('defaultplc')
                      , asset.get('reasonlist')
                      , asset.get('defaultreason')
                      , asset.get('area')
                      , asset.get('templateref')
                      , asset.get('primaryref'))
        assets.append(assetClass)

    #write the reason codes to a csv file
    fieldnames = ['Site','Asset Name', 'MES Ent in ABLE', 'Type','PLC']

    with open(csvfile, 'w', newline='') as assetlist:

        writer = csv.DictWriter(assetlist, fieldnames=fieldnames)
        print('File Created.')

        # Write header row
        writer.writeheader()
        print('Starting File Write.')

        # Write data rows
        for asset in assets:
            if asset.type == 'LINE' or asset.type == 'SEC':
                #reason level 2 none
                writer.writerow({'Site': f"{asset.site_name}",
                                    'Asset Name': f"{asset.name}",
                                    'MES Ent in ABLE': f'{asset.devicename}',
                                    'Type': f"{asset.type}",
                                    'PLC': f"{asset.defaultplc}"})
            else:
                pass
    
if __name__ == "__main__":
    able_config_to_csv_asset_list('.\\XML Exports from ABLE\\idc - Belle 20250124 - 03.xml', 'assetList.csv')