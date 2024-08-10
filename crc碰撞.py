#coding:utf-8
import zipfile
import string
import binascii
 
def CrackCrc(crc):
    for i in dic:
        for j in dic:
            for p in dic:
                #for q in dic:
                    s = i + j + p
                    if crc == (binascii.crc32(s) & 0xffffffff):
                        #print s
                        f.write(s+"\n")
                        return
 
def CrackZip():
    for I in range(36):
        file = 'flag' + str(I) + '.zip'
        f = zipfile.ZipFile(file, 'r')
        GetCrc = f.getinfo('flag.txt')
        crc = GetCrc.CRC
        #以上3行为获取压缩包CRC32值的步骤
        #print hex(crc)
        CrackCrc(crc)
 
dic = string.ascii_letters + string.digits + '+/='
 
f = open('out.txt', 'w')
CrackZip()
f.close()