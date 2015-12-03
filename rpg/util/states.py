

class States:
    AK = {"label": "Alaska", "code": "AK"},
    AL = {"label": "Alabama", "code": "AL"},
    AR = {"label": "Arkansas", "code": "AR"},
    AZ = {"label": "Arizona", "code": "AZ"},
    CA = {"label": "California", "code": "CA"},
    CO = {"label": "Colorado", "code": "CO"},
    CT = {"label": "Connecticut", "code": "CT"},
    DC = {"label": "District Of Columbia", "code": "DC"},
    DE = {"label": "Delaware", "code": "DE"},
    FL = {"label": "Florida", "code": "FL"},
    GA = {"label": "Georgia", "code": "GA"},
    HI = {"label": "Hawaii", "code": "HI"},
    IA = {"label": "Iowa", "code": "IA"},
    ID = {"label": "Idaho", "code": "ID"},
    IL = {"label": "Illinois", "code": "IL"},
    IN = {"label": "Indiana", "code": "IN"},
    KS = {"label": "Kansas", "code": "KS"},
    KY = {"label": "Kentucky", "code": "KY"},
    LA = {"label": "Louisiana", "code": "LA"},
    MA = {"label": "Massachusetts", "code": "MA"},
    MD = {"label": "Maryland", "code": "MD"},
    ME = {"label": "Maine", "code": "ME"},
    MI = {"label": "Michigan", "code": "MI"},
    MN = {"label": "Minnesota", "code": "MN"},
    MO = {"label": "Missouri", "code": "MO"},
    MS = {"label": "Mississippi", "code": "MS"},
    MT = {"label": "Montana", "code": "MT"},
    NC = {"label": "North Carolina", "code": "NC"},
    ND = {"label": "North Dakota", "code": "ND"},
    NE = {"label": "Nebraska", "code": "NE"},
    NH = {"label": "New Hampshire", "code": "NH"},
    NJ = {"label": "New Jersey", "code": "NJ"},
    NM = {"label": "New Mexico", "code": "NM"},
    NV = {"label": "Nevada", "code": "NV"},
    NY = {"label": "New York", "code": "NY"},
    OH = {"label": "Ohio", "code": "OH"},
    OK = {"label": "Oklahoma", "code": "OK"},
    OR = {"label": "Oregon", "code": "OR"},
    PA = {"label": "Pennsylvania", "code": "PA"},
    RI = {"label": "Rhode Island", "code": "RI"},
    SC = {"label": "South Carolina", "code": "SC"},
    SD = {"label": "South Dakota", "code": "SD"},
    TN = {"label": "Tennessee", "code": "TN"},
    TX = {"label": "Texas", "code": "TX"},
    UT = {"label": "Utah", "code": "UT"},
    VA = {"label": "Virginia", "code": "VA"},
    VT = {"label": "Vermont", "code": "VT"},
    WA = {"label": "Washington", "code": "WA"},
    WI = {"label": "Wisconsin", "code": "WI"},
    WV = {"label": "West Virginia", "code": "WV"},
    WY = {"label": "Wyoming", "code": "WY"}
    __table__ = None


    @staticmethod
    def table():
        tbl = States.__table__
        if not tbl:
            tbl = {}
            states = dir(States)
            for state in states:
                val = getattr(States, state)
                val = val[0] if isinstance(val, tuple) else val
                if isinstance(val, dict):
                    tbl[state] = val

            States.__table__ = tbl
        return tbl


    @staticmethod
    def all():
        tbl = States.table()
        return tbl.values()


    @staticmethod
    def get(name):
        lst = States.all()
        name = name.upper() if len(name) == 2 else name.lower()
        match = [s for s in lst if s["label"].lower() == name or s["code"] == name]
        if not match:
            return None
        return match[0]


