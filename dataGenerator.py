
#original: 13.7MB (f0)

# f1 : f0*18 = 246.6MB
# f2 : f0*36 = 493.2MB
# f3 : f0*72 = 986.4MB
# f4 : f0*144 = 1972.8MB
# f5 : f0*288 = 3945.6MB


f1data = ""
with open('tweets_antic.json') as f1:
    f1data = f1.read()

f2data = ""
for i in range(18):
    f2data += "\n"
    f2data += f1data
with open ('250MB.json', 'a+') as f2:
    f2.write(f2data)

f3data = ""
for i in range(36):
    f3data += "\n"
    f3data += f1data
with open ('500MB.json', 'a+') as f3:
    f3.write(f3data)

f4data = ""
for i in range(72):
    f4data += "\n"
    f4data += f1data
with open ('1GB.json', 'a+') as f4:
    f4.write(f4data)

f5data = ""
for i in range(144):
    f5data += "\n"
    f5data += f1data
with open ('2GB.json', 'a+') as f5:
    f5.write(f5data)


#f6data = ""
#for i in range(288):
#    f6data += "\n"
#    f6data += f1data
#with open ('nousDat/4GB.json', 'a+') as f6:
#    f6.write(f6data)
