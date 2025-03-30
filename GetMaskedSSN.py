'''-------------------------------------------------------------
| Michael Manley | mike.manley@gmail.com
| Returns a fully masked Social Security Number (SSN).
| Note: Default masking char is "*".
| History:
| 1.
-------------------------------------------------------------'''
def GetMaskedSSN(p_mask_char:str = '*') -> str:
    try:
        return f"{p_mask_char.strip()[0:1] * 9}"
    except Exception as e:
        return None
    
print(GetMaskedSSN())
print(GetMaskedSSN("x"))