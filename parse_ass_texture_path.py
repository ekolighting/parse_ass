ROOT_DRIVE = 'J:'
f=open('folding_chair001/standin/folding_chair001.ass','r')
flines = f.readlines()
f.close()
f=open('folding_chair001/standin/folding_chair001_texture_fixed_w_binary.ass','w')
for line in flines:
    if 'filename' in line or 'path' in line:
        line = line.split('"')[0] +  '"' + ROOT_DRIVE + line.split('"')[1]+ '"'
    elif 'scene' in line and '###' in line:
        line = line.split(' ')[0] +' '+line.split(' ')[1] + ' '+ROOT_DRIVE + line.split(' ')[-1]
    f.write(line)

        #print (line.split(' ')[-1])

     #   line = ' filename "J:' + line.split('"')[-2] + '"'
    #f.write(line)
        #print (line + '"J:' + line.split('"')[-2] + '"')

    #a = line.split('b85')[-1]
 #   if len(a) < 200:
 #       f.write(line)
 #       print(len(a), a)
f.close()