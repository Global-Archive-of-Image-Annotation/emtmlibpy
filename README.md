# emtmlibpy
## Python wrapper for EMTLib for EventMeasure

To use you need a copy of `libEMTMLib.so` and valid licence to use it.  Available from https://www.seagis.com.au/
```bash
sudo mv libEMTMLib.so /usr/local/lib
sudo ldconfig
```
## Example use 
```python
import emtmlibpy as emtm
from emtmlibpy import EMTMResult

print(emtm_version())
```

For a full list of examples look at the [unit tests](https://github.com/AutomatedFishID/emtmlibpy/blob/main/src/test_emtmlibpy.py)

