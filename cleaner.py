f = open("EASYSOL326dc49.csv", "r")
rf = open("cleaned_data.csv", "w")
s = f.readline()
s = s.split("|")
ind = s.index("BARCODE")
for i in range(0,750000):
	s = f.readline()
	s = s.split("|")
	try:
		bc = int(s[ind])
	except:
		bc = 0
	if bc >= 1000000000000 and bc <= 9000000000000 and len(s) == 9:
		string = ','.join(s)
		rf.write(string)
