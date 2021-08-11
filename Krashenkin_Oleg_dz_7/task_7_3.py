import os
import shutil

path_ = os.path.join(os.getcwd(), 'my_project')
for root, dirs, files in os.walk(path_):
    for f in files:
        if f.endswith('.html'):
            if not os.path.isdir(os.path.join('my_project/templates', os.path.split(root)[1])):
                shutil.copytree(root, os.path.join('my_project/templates', os.path.split(root)[1]))
print('Done!=)')