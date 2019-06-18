# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

try: # 1
    from can_settings import can_settings
except:
    from ics.structures.can_settings import can_settings

class seevb_settings(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('ecu_id', ctypes.c_uint32), 
        ('can1', can_settings), 
        ('network_enables', ctypes.c_uint16), 
        ('network_enabled_on_boot', ctypes.c_uint16), 
        ('iso15765_separation_time_offset', ctypes.c_uint16), 
        ('perf_en', ctypes.c_uint16), 
        ('ain_sample_period', ctypes.c_uint16), 
        ('ain_threshold', ctypes.c_uint16), 
        ('rsvd', ctypes.c_uint32), 
    ]

# Extra names go here:
SEEVBSettings = seevb_settings
# End of extra names

