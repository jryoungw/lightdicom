# LightDICOM

## Basic Usage

```
from LightClass import LightDCMClass

lc = LightDCMClass()
lc.path = path_to_dicom
d = lc.get_data('0010,0010') # Read tag (0010, 0010), which is "Patient's Name"
npy = lc.read_pixel() # Read pixel values
```

Or

```
from LightClass import LightDCMClass

lc = LightDCMClass(path=path_to_dicom)
d = lc.get_data('0010,0010') # Read tag (0010, 0010), which is "Patient's Name"
npy = lc.read_pixel() # Read pixel values
```

## How to read all headers and their values?

```
lc = LightDCMClass()
lc.path = path_to_dicom 
# Equivalent code : lc = LightDCMClass(path=path_to_dicom)
all_headers = lc.read_all(with_pixel=True)
```


## Notes

This is prototype version. Other advanced version will be released soon ... (maybe?)
