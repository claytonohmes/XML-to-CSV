class Asset:
    '''
    Asset class to store the asset information
    '''
    def __init__(self, site_name, name, devicename, type, defaultplc, reasonlist, defaultreason, area, templateref, primaryref):
        self.site_name = site_name
        self.name = name
        self.devicename = devicename
        self.type = type
        self.defaultplc = defaultplc
        self.reasonlist = reasonlist
        self.defaultreason = defaultreason
        self.area = area
        self.templateref = templateref
        self.primaryref = primaryref
    
    def __repr__(self):
        return f'<asset name="{self.name}" devicename="{self.devicename}" type="{self.type}" scanpriority="10" defaultplc="{self.defaultplc}" reasonlist="{self.reasonlist}" defaultreason="{self.defaultreason}" area="{self.area}" templateref="{self.templateref}" primaryref="{self.primaryref}">'