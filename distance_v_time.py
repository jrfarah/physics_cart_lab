import matplotlib.pyplot as plt
import os

try:
	os.system("rm -f dvt_graph.png")
except:
	pass

def integrate(y_vals, h):
    i=1
    total=y_vals[0]+y_vals[-1]
    for y in y_vals[1:-1]:
        if i%2 == 0:
            total+=2*y
        else:
            total+=4*y
        i+=1
    return total*(h/3.0)

data = 'data.txt'
target = open(data, 'r+w')
lines = target.readlines()
x_values = []
y_values = []
velx = []
vely = []
accely = []
accelx = []
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
y_values2 = []
y_values2.append(y_values[0])
for i in range(1, len(y_values)):
	y_values2.append(y_values2[i-1]+y_values[i])
print len(x_values), len(y_values2)
for i in range(len(x_values)-1):
	velx.append((x_values[i]+x_values[i+1])/2)
for i in range(len(y_values)-1):
	vely.append((y_values[i]+y_values[i+1])/2)
for i in range(len(velx)-1):
	accelx.append((velx[i]+velx[i+1])/2)
for i in range(len(vely)-1):
	accely.append((vely[i]+vely[i+1])/2)
x = velx
y = vely
area = integrate(vely,1)
print area
plt.plot(x,y, marker = 'o')
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (cm/0.1s)')
plt.title('Velocity v Time')
# plt.show()
plt.savefig("vel.png")