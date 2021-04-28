import os, shutil
from os import walk

ROOT = '/Users/gojaehyeog/Documents/PY/parse_ass'
ROOT_DRIVE = 'J:'

def get_all_ass_files():
    ass_files = []
    for root, dirnames, files in walk(ROOT):
        for file_ in files:
            if file_.split('.')[-1] == 'ass':
                ass_files.append(os.path.join(root,file_))
    return ass_files

def copy_backup(ass_files):
    #f=open(ROOT + '/ass_file_list.txt','w')
    for ass in ass_files:
        if '_backup' not in ass:
            src = ass
            dest = ass.split('.')[0] + '_backup.' +ass.split('.')[-1]
            #f.write(src)
            #f.write('\n')
            #f.write('==TO==>')
            #f.write(dest)
            #f.write('\n')
            #print (src, 'TO', dest)
    #f.close()

def replace_path(ass_files):
    for ass in ass_files:
        f=open(ass,'r')
        flines = f.readlines()
        f.close()

        src = ass
        dest = ass.split('.')[0] + '_backup.' +ass.split('.')[-1]
        shutil.move(src, dest)
        f=open(src,'w')
        for line in flines:
            if 'J:' not in line:
                if 'filename' in line or 'path' in line:
                    line = line.split('"')[0] +  '"' + ROOT_DRIVE + line.split('"')[1]+ '"'
                elif 'scene' in line and '###' in line:
                    line = line.split(' ')[0] +' '+line.split(' ')[1] + ' '+ROOT_DRIVE + line.split(' ')[-1]
            f.write(line)
        f.close()

ass_files = get_all_ass_files()
copy_backup(ass_files)
replace_path(ass_files)

