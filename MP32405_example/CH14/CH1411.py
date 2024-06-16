from io import BytesIO

fo = BytesIO(b'Python')
#取得緩衝區
view = fo.getbuffer()
#代換字元
view[2:4] = b"Cr"
print(fo.getvalue())

data = BytesIO(b'\x50\x79\x74\x68\x6f\x6e')
print(data.read())
