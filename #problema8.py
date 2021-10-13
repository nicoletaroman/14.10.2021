#problema8
x=[]
for i in range(65,91):
    x+=[" ",chr(i),]
print(x)


for e in range(0,len(x)+1):
    if e in range(0,len(x)-1):
        x[e]=x[e+1]
print(x)

for i in range(len(x)):
    if x[i] == "Z":
        x[i] = "A"
    if x[i] == " ":
        x[i]= "-"
print(x)