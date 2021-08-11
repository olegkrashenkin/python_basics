import os
from yaml import safe_load


def mk_starter(config_dict, path_=os.getcwd()):
    if isinstance(config_dict, dict):
        for k, v in config_dict.items():
            if not os.path.isdir(os.path.join(path_, k)):
                os.mkdir(os.path.join(path_, k))
            mk_starter(v, os.path.join(os.path.abspath(path_), k))
    else:
        for i in config_dict:
            if not isinstance(i, dict):
                with open(os.path.join(os.path.abspath(path_), i), 'w', encoding='utf-8') as f:
                    f.write(f'# {i}')
            else:
                mk_starter(i, path_)


with open('config.yaml', 'r') as f:
    config_f = safe_load(f)
if len(config_f) != 1:
    exit('Что-то потом написать')

mk_starter(config_f)
print('Уииииииии! Работает! =)')
