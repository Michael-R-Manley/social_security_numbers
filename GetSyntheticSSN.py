'''-------------------------------------------------------------
| Michael Manley | mike.manley@gmail.com
| Returns a synthetic, conformant US Social Security Number.
| If a valid state code is supplied, a state-specific SSN will 
| be returned prior to randomization (June 25, 2011).  If a
| valid state code is not supplied or is None, then a random,
| conforming SSN will be returned.
| Format: AAAGGSSSS (string)
| E.g. GetSyntheticSSN("NH") -> "001382734"
| E.g. GetSyntheticSSN(" ma") -> "025106153"
| E.g. GetSytheticSSN() -> "529412854"
| History:
| 1.
-------------------------------------------------------------'''
import random as r

def GetSyntheticSSN(p_StateCode:str = None) -> str:
    # Returns a synthetic Social Security Number
    # Source: https://web.archive.org/web/20050830025754/http://www.ssa.gov/foia/stateWeb.html
    state_aaa_dict = {
        "AK": ["574", "676-679"],                   # Alaska
        "AL": ["416-424"],                          # Alabama
        "AR": ["429-432"],                          # Arkansas
        "AS": ["586"],                              # American Samoa (Territory)
        "AZ": ["526-527", "600-601", "764-765"],    # Arizona
        "CA": ["545-573", "602-626"],               # California
        "CO": ["521-524", "650-653"],               # Colorado
        "CT": ["040-049"],                          # Connecticut
        "DC": ["577-579"],                          # District of Columbia (Federal District)
        "DE": ["221-222"],                          # Delaware
        "EE": ["729-733"],                          # Enumeration at Entry (Immigration Process)
        "FL": ["261-267", "589-595", "766-772"],    # Florida
        "GA": ["252-260", "667-675"],               # Georgia
        "GU": ["586"],                              # Guam (Territory)
        "HI": ["575-576", "750-751"],               # Hawaii
        "IA": ["478-485"],                          # Iowa
        "ID": ["518-519"],                          # Idaho
        "IL": ["318-361"],                          # Illinois
        "IN": ["303-317"],                          # Indiana
        "KS": ["509-515"],                          # Kansas
        "KY": ["400-407"],                          # Kentucky
        "LA": ["433-439", "659-665"],               # Louisiana
        "MA": ["010-034"],                          # Massachusetts
        "MD": ["212-220"],                          # Maryland
        "ME": ["004-007"],                          # Maine
        "MI": ["362-386", "486-500"],               # Michigan
        "MN": ["468-477"],                          # Minnesota
        "MP": ["586"],                              # Northern Mariana Island (Territory)
        "MS": ["425-428", "587-588", "752-755"],    # Missouri
        "MT": ["516-517"],                          # Montana
        "NC": ["237-246", "681-690"],               # North Carolina
        "ND": ["501-502"],                          # North Dakota
        "NE": ["505-508"],                          # Nebraska
        "NH": ["001-003"],                          # New Hampshire
        "NJ": ["135-158"],                          # New Jersey
        "NM": ["525, 585", "648-649"],              # New Mexico
        "NV": ["530, 680"],                         # Nevada
        "NY": ["050-134"],                          # New York
        "OH": ["268-302"],                          # Ohio
        "OK": ["440-448"],                          # Oklahoma
        "OR": ["540-544"],                          # Oregon
        "PA": ["159-211"],                          # Pennsylvania
        "PH": ["586"],                              # Phillipines (Former Territory)
        "PR": ["580-584", "596-599"],               # Puerto Rico (Territory)
        "RI": ["035-039"],                          # Rhode Island
        "RR": ["700-728"],                          # Railroad Retirement Board (RRB)
        "SC": ["247-251", "654-658"],               # South Carolina
        "SD": ["503-504"],                          # South Dakota
        "TN": ["408-415", "756-763"],               # Tennessee
        "TX": ["449-467", "627-645"],               # Texas
        "UT": ["528-529", "646-647"],               # Utah
        "VA": ["223-231", "691-699"],               # Virginia
        "VI": ["580"],                              # United States Virgin Islands (Territory)
        "VT": ["008-009"],                          # Vermont
        "WA": ["531-539"],                          # Washington
        "WI": ["387-399"],                          # Wisconsin
        "WV": ["232-236"],                          # West Virginia
        "WY": ["520"]                               # Wyoming
    }

    def GetAreaNumber(p_StateCode:str = None) -> int:
        # Returns the Area Number of the Social Security Number
        def GetDefault() -> str:
            # If no state code is supplied or not found in dictionary
            while True:
                areaNumber = r.randint(0, 899)
                if areaNumber not in (0, 666): return areaNumber
        try:
            if p_StateCode is None: return GetDefault()
            stateCode = p_StateCode.strip().upper()

            if stateCode in state_aaa_dict:
                ranges = state_aaa_dict[stateCode]
                range = r.choice(ranges)
                if "-" in range:
                    first, last = map(int, range.split("-"))
                    areaNumber = r.randint(first, last)
                else:
                    areaNumber = int(range)
            else:
                return GetDefault()
            return int(areaNumber)
        except Exception as e:
            return int("001") # This is also an Area Number for NH
    
    def GetGroupNumber() -> int:
        # Returns the Group Number of the Social Security Number
        try:
            while True:
                groupNumber = r.randint(0,99)
                if groupNumber != 0: return groupNumber
        except Exception as e:
            return int("01")
            
    def GetSerialNumber() -> int:
        # Returns the Serial Number portion of the Social Security Number
        try:
            while True:
                serialNumber = r.randint(0,9999)
                if serialNumber != 0: return serialNumber
        except Exception as e:
            return int("0001")
    try:
        aNum = GetAreaNumber(p_StateCode)
        gNum = GetGroupNumber()
        sNum = GetSerialNumber()
        if None not in (aNum, gNum, sNum): return f"{aNum:03d}{gNum:02d}{sNum:04d}"
    except Exception as e:
        return e
    
print(GetSyntheticSSN('WV'))