import os, shutil
from os import walk

ROOT = '/Users/gojaehyeog/Documents/PY/parse_ass'
ROOT_DRIVE = 'J:'

def get_all_bk_ass_files():
    ass_files = []
    for root, dirnames, files in walk(ROOT):
        for file_ in files:
            if file_.split('.')[-1] == 'ass' and '_backup' in file_:
                ass_files.append(os.path.join(root,file_))
    return ass_files

def restore_backup(ass_files):
    f=open(ROOT + '/ass__file_list.txt','w')
    for ass in ass_files:
        src = ass
        dest = ass.split('.')[0] + '_backup.' +ass.split('.')[-1]
        shutil.move(src, dest)
        f.write(src)
        f.write('\n')
        f.write('==TO==>')
        f.write(dest)
        f.write('\n')
        print (src, 'TO', dest)
    f.close()

ass_files = get_all_ass_files()
copy_backup(ass_files)
replace_path(ass_files)

