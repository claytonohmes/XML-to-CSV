class ReasonCode:
    '''
    This class is used to represent each reason code:
    siteName: The name of the site. This will be the same for all reason codes in the file

    reasArea: the area of the plant the reason code resides in.

    reas1: the first reason level

    reas2: the second reason level

    reas3: the third reason level

    opccode: this is the offset produced by ABLE. This will be unique value.

    category: GME Superreason
    '''
    def __init__(self, siteName, reasArea, reas1, reas2, reas3, opccode, category):
        self.siteName = siteName
        self.reasArea = reasArea
        self.reas1 = reas1
        self.reas2 = reas2
        self.reas3 = reas3
        self.opccode = opccode
        self.category = category

    def __repr__(self):
        return f"ReasonCode({self.siteName},{self.reasArea},{self.reas1},{self.reas2},{self.reas3},{self.opccode},{self.category})"

    def __str__(self):
        return f"{self.siteName}|{self.reasArea}|{self.reas1}|{self.reas2}|{self.reas3}|{self.opccode}|{self.category}"