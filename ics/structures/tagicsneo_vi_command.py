# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

class tagicsneo_vi_command(ctypes.Structure):
    _fields_ = [
        ('CommandType', ctypes.c_uint8), 
        ('CommandByteLength', ctypes.c_uint8), 
        ('Data', ctypes.c_uint8 * 14), 
    ]

# Extra names go here:
icsneoVICommand = tagicsneo_vi_command
# End of extra names

