'''-------------------------------------------------------------
| Michael Manley | mike.manley@gmail.com
| Returns True if a supplied Social Security Number (SSN) is
| conformant and returns False if not.
| Note: Conforms to randomization standard (June 2011)
| Supported format: AAAGGSSSS (string)
| E.g. "010329876" -> True
| E.g. "666129182" -> False
| History:
| 1.
-------------------------------------------------------------'''
def IsValidSSN(p_ssn:str = None) -> bool:
    try:
        if p_ssn is None:
            return False
        else:
            v_ssn = str(p_ssn).strip()
            if len(v_ssn) != 9: return False                # Must be exactly 9 characters in length
            if not v_ssn.isdigit(): return False            # Must be all numerals
            if v_ssn[0:3] in ("000", "666"): return False   # 000 and 666 are prohibited Area Numbers
            if v_ssn[0:1] == "9": return False              # 900 through 999 are prohibited Area Numbers
            if v_ssn[3:5] == "00": return False             # Group Number cannot be "00"
            if v_ssn[5:9] == "0000": return False           # Serial Number cannot be "0000"
            return True
    except Exception as e:
        return False
    
print(IsValidSSN('666129182'))
print(IsValidSSN(None))
print(IsValidSSN())