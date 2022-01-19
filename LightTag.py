from Tags import DicomDictionary
from Errors import LightError

from typing import Union, Any

class Tag:
    def __init__(self):
        self._dict = DicomDictionary
        for k in DicomDictionary.keys():
            setattr(self, DicomDictionary[k][4], None)
    
    def __getitem__(self, tag:Union[str, int, tuple]) -> Any:
        if isinstance(tag, str):
            return getattr(self, tag)
        elif isinstance(tag, int):
            field = self._dict[tag][4]
            return getattr(self, field)
        elif isinstance(tag, tuple):
            tag1, tag2 = tag
            field = self._dict[tag1 * (16**4) + tag2][4]
            return getattr(self, field)
        else:
            raise LightError("This is not valid indexing. Try one of:\n"+\
                             "          1. dcm[0x10,0x10]\n"+\
                             "          2. dcm[0x100010]\n"+\
                             "          3. dcm.PatientName")

