import Model.AlarmList
import Model.Alarm
import Model.AbleAsset
import xml.etree.ElementTree as ET

xmlFile = 'XML Exports from ABLE\idc ClorAtlWest 2024-10-15.xml'

def able_config_to_csv_asset_list(file):
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

    return assets

asset_list = able_config_to_csv_asset_list(xmlFile)
