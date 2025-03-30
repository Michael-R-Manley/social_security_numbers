'''-------------------------------------------------------------
| Michael Manley | mike.manley@gmail.com
| Returns a partially masked Social Security Number (SSN) with
| only the last four (right-most) characters exposed.
| E.g. "010329876" -> "*****9876"
| E.g. "666129182", "x" -> "xxxxx9182"
| History:
| 1.
-------------------------------------------------------------'''
def GetPartialMaskedSSN(p_ssn:str, p_mask_char:str = '*') -> str:
    try:
        sSN = p_ssn.strip()
        if len(p_mask_char) == 0: maskChar = '*'
        else: maskChar = p_mask_char.strip()[0:1]
        return f"{(maskChar * 5) + sSN[-4:]}"
    except Exception as e:
        return None
    
print(GetPartialMaskedSSN("666129182", "x"))