# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

class ethernet_settings2_t(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('flags', ctypes.c_uint8), 
        ('link_speed', ctypes.c_uint8), # 0=10, 1=100, 2=1000
        ('ip_addr', ctypes.c_uint32), 
        ('netmask', ctypes.c_uint32), 
        ('gateway', ctypes.c_uint32), 
        ('rsvd', ctypes.c_uint8 * 2), 
    ]

# Extra names go here:
ETHERNET_SETTINGS2 = ethernet_settings2_t
# End of extra names

