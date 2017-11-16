import os
import hashlib

h = hashlib.md5
rawdisk0 = r'\\.\PhysicalDrive0'

# Read MBR from raw disk
with open(rawdisk0, "rb+") as d:
    mbr1 = d.read(512)

# MD5 of MBR
hash1 = h(mbr1).hexdigest()

# Write copy of mbr to filesystem
with open('c:\\temp\\mbr1.bin', 'wb') as d:
    d.write(mbr1)

# Write MBR back to raw disk to test for MBR overwrite protection
with open(rawdisk0, 'rb+') as d:
    d.write(mbr1)

# Read newly written MBR from disk
with open(rawdisk0, "rb+") as d:
    mbr2 = d.read(512)

# MD5 of new MBR
hash2 = h(mbr2).hexdigest()

# Write new MBR to file2
with open('c:\\temp\\mbr2.bin', 'wb') as d:
    d.write(mbr2)

outreport = "Original MBR has MD5: "+hash1+"\n"
outreport += "Re-written MBR has MD5: "+hash2+"\n\n"
outreport += "MBR hashes are equal: "+str(hash1==hash2)+"\n"
outreport += "The space-time continuum is safe: "+str(hash1==hash2)+"\n"

with open('c:\\temp\\mbr_report.txt', 'w') as d:
    d.write(outreport)
