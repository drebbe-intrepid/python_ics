# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

class ethernet_settings(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('duplex', ctypes.c_uint8), 
        ('link_speed', ctypes.c_uint8), 
        ('auto_neg', ctypes.c_uint8), 
        ('led_mode', ctypes.c_uint8), 
        ('rsvd', ctypes.c_uint8 * 4), 
    ]

# Extra names go here:
ETHERNET_SETTINGS = ethernet_settings
# End of extra names

