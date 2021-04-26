ROOT_DRIVE = 'J:'
f=open('folding_chair001/standin/folding_chair001.ass','r')
flines = f.readlines()
f.close()
f=open('folding_chair001/standin/folding_chair001_path_list.txt','w')
for line in flines:
    if 'filename' in line or 'path' in line:
        new_line = line.split('"')[0] +  '"' + ROOT_DRIVE + line.split('"')[1]+ '"'
        f.write(line)
        f.write('===>')
        f.write(new_line)
        f.write('\n\n')
f.close()