f = open("day_bc_json.csv", "r")
rf = open("bread_json_day.csv", "w")
for i in range(0, 49000):
	s = f.readline()
	s = s.split(",")
	if s[1] == '8906020460010':
		string = ','.join(s)
		rf.write(string)

