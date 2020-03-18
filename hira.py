import sys
import re
from pathlib import Path

p = re.compile('^[ぁ-ゟ]+')

path = Path(sys.argv[1])
name = path.name
print(name)
kpath = path.parent / f'K{name}'
hpath = path.parent / f'H{name}'

with path.open() as f:
    with open(str(kpath), 'w') as kf:
        with open(str(hpath), 'w') as hf:
            for line in f:
                if p.match(line):
                    hf.write(line)
                else:
                    kf.write(line)
