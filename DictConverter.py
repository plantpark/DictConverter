dicts = []
dictfilename = raw_input('please type in file name of dicts : ')
with open(dictfilename) as f:
	content = f.readlines()
for i in range(0,len(content)):
	if i % 3 == 0:
		dicts.append(content[i].split('[')[0])
thefile = open('dicts.txt','w')
for item in dicts:
	thefile.write('%s\n'%item)
thefile.close()
print 'dict has been write to dicts.txt files ,please import it to your dicts!'