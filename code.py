#!/usr/bin/python

import matplotlib.pyplot as plt
import os

try:
	os.system("rm -f table.png")
except:
	pass

data = 'data.txt'
target = open(data, 'r+w')
lines = target.readlines()
x_values = []
y_values = []
labels = []
values = []
for line in lines:
	print line
	if line[0]=="#":
		labels.append(line)
		pass
	else:
		if line[0]=='=':
			y_value_begins = lines.index(line) + 1
			break
		else:
			num = line.rstrip()
			print num
			x_values.append(float(num))
for i in range(y_value_begins,len(lines)-1):
	print line
	if lines[i][0]=='=':
		break
	else:
		num = lines[i].rstrip()
		print num
		y_values.append(float(num))

print x_values
print '\n'
print y_values
print len(x_values), len(y_values)
final_x_values = []
final_y_values = []
for i in range(len(x_values)-1):
	values.append([x_values[i],y_values[i]])
colLabels=('Time (sec)', 'Length (cm)')
hcell, wcell = 0.3, 4.
hpad, wpad = 0, 0  
nrows, ncols = len(values)+1, len(colLabels)
fig=plt.figure(figsize=(ncols*wcell+wpad, nrows*hcell+hpad))
ax = fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
the_table = ax.table(cellText=values,
          colLabels=colLabels,
          		loc='center')
plt.title("Distance Traveled vs. Time")
plt.savefig("table.png")