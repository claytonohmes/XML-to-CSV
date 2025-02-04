import xml.etree.ElementTree as ET

def get_site_name(file):
    '''
    the purpose of this function is to take the ABLE config alarms and output the name of the site.
    '''
    #parse the xml file
    tree = ET.parse(file)
    root = tree.getroot()

    #get the site name
    site_name = root.get('name')
    return site_name

if __name__ == "__main__":
    print(get_site_name('C:\\Users\\cohmes\OneDrive - Clorox Services Company\\Projects\\ABLE\\Python\\Alarm List from config to CSV\\XML Exports from ABLE\\idc ClorAtlWest 2024-10-15.xml'))