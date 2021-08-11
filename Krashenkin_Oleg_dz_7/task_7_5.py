import collections
import os
import django
import re
import json

root_dir = django.__path__[0]
count = collections.defaultdict(int)
extension = collections.defaultdict(set)
for root, dirs, files in os.walk(root_dir):
    for f in files:
        for i in [100, 1000, 10000, 100000]:
            if os.stat(os.path.join(root, f)).st_size <= i:
                count[i] += 1
                extension[i].add(re.split(r'[.]', f)[-1])
                break
result = {k_c: (v_c, list(v_e)) for k_c, v_c in count.items() for k_e, v_e in extension.items()}
result = {i: result[i] for i in sorted(result)}
with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)