import msgpack
import msgpack_numpy as mp_np
mp_np.patch()

f= open('hist_dict.mp', 'rb')
s= f.read()
d = msgpack.unpackb(s, object_hook=mp_np.decode)


