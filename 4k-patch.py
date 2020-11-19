# Modify laptop 4k panel edid for big sur
# This will make panel running at 48Hz
# Created by xxxzc
# Reference: http://bbs.pcbeta.com/forum.php?mod=viewthread&tid=1866466&highlight=edid
from subprocess import check_output
from base64 import b64encode
from platform import system

edid = ''
try:
    if system() == 'Darwin':
        edid = check_output('ioreg -lw0 | grep -i "IODisplayEDID2"',
                            shell=True, encoding='utf-8')
        if '<' not in edid:
            raise Exception
        edid = edid.split('<')[1].split('>')[0]
        print('Display EDID:', edid)
except Exception:
    edid = ''

if not edid:
    edid = input('No edid found, please input it manually: ').replace(
        ' ', '').strip()

edid = edid[:108] + 'a6a6' + edid[112:]  # set refresh rate to 48Hz
data = [int(edid[i:i+2], 16) for i in range(0, len(edid), 2)]
checksum = hex(256 - sum(data[:-1]) % 256)[2:]
print('Modified EDID:', edid[:-2] + checksum)
data[-1] = int(checksum, 16)
data = b64encode(bytes(data)).decode('utf-8')
print('data:', data)
print()
print('You should add following to PciRoot(0x0)/Pci(0x2,0x0):')
print('<key>AAPL00,override-no-connect</key>')
print(f'<data>{data}</data>')