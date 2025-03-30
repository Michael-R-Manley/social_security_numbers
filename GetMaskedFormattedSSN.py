'''-------------------------------------------------------------
| Michael Manley | mike.manley@gmail.com
| Returns a fully masked and formatted Social Security Number 
| (SSN).
| Note: Default mask char is "*", default delimiter char is "-".
| E.g. "***-**-****"
| History:
| 1.
-------------------------------------------------------------'''
def GetMaskedFormattedSSN(p_delimiter:str = '-', p_mask_char:str = '*') -> str:
    try:
        maskChar = p_mask_char.strip()[0:1]
        delimChar = p_delimiter.strip()[0:1]
        return f"{(maskChar * 3)}{delimChar}{(maskChar * 2)}{delimChar}{(maskChar * 4)}"
    except Exception as e:
        return None
    
print(GetMaskedFormattedSSN())