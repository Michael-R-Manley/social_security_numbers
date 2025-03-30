'''-------------------------------------------------------------
| Michael Manley | mike.manley@gmail.com
| Returns a formatted Social Security Number with embedded
| delimiter characters.
| E.g. "010329876" -> "010-32-9876"
| E.g. "666129182", "." -> "666.12.9182"
| History:
| 1.
-------------------------------------------------------------'''
def GetFormattedSSN(p_ssn:str, p_delimiter:str = "-") -> str:
    try:
        if p_ssn is None: return None
        delim = p_delimiter.strip()[0:1]
        return f"{p_ssn[:3]}{delim}{p_ssn[3:5]}{delim}{p_ssn[5:]}"
    except Exception as e:
        return None
    
print(GetFormattedSSN("010329876"))
print(GetFormattedSSN("010329876", "  "))