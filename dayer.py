import datetime
f = open("EASYSOL326dc49.csv", "r")
rf = open("day_bc_json.csv", "w")
s = f.readline()
s = s.split("|")
print(s)
bci = s.index("BARCODE")
usi = s.index("UPDATE_STAMP\n")
d = {}
for i in range(0,750000):
	s = f.readline()
	s = s.split("|")
	us = s[usi].split(' ')
	wn = us[0]
	try:
		bc = int(s[bci])
	except:
		bc = 0
	if bc >= 8000000000000 and bc <= 9000000000000 and len(s) == 9:
		if wn in d:
			week = d[wn]
			if bc in week:
				week[bc] += 1
			else:
				week[bc] = 1
		else:
			d[wn] = {bc : 1}

		
for i in d:
	for j in d[i]:
		string = ','.join([str(i), str(j), str(d[i][j])+'\n'])
		rf.write(string)
	

'''
{
	2 : {
		8011313513 : 3,
		8013513135 : 5
	}
}
'''
