import ctypes
from dlt.dlt import DLTClient, DLT_RECEIVE_SOCKET
from dlt import dlt
c = dlt.DLTClient(servIP="127.0.0.1")
c.connect()
dlt.dltlib.dlt_receiver_receive(ctypes.byref(c.receiver), DLT_RECEIVE_SOCKET)  
#c.read_message()
print(c.read_message())
