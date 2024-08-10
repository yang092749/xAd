import os
import binascii
import struct

crcbp = open("qwq.png", "rb").read()    #打开图片
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + \
            struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if(crc32 == 0xB63F502C):    #图片当前CRC
            print(i, j)
            print('hex:', hex(i), hex(j))
