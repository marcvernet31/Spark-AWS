
#   250MB : A
#   500MB : B
#   1G : C
#   2G : D
#   4G : E
#   8G : F


f1data = f2data = ""
with open('Tweets.json') as f1:
    f1data = f1.read()

#250MB
A = f1data
with open ('datos/250MB.json', 'a') as f3:
    f3.write(A)

#500MB
A += "\n"
A += A
with open ('datos/500MB.json', 'a') as f3:
    f3.write(A)

#1GB
A += "\n"
A += A
with open ('datos/1G.json', 'a') as f3:
    f3.write(A)

#2GB
A += "\n"
A += A
with open ('datos/2G.json', 'a') as f3:
    f3.write(A)

#4GB
A += "\n"
A += A
with open ('datos/4G.json', 'a') as f3:
    f3.write(A)

#8GB
A += "\n"
A += A
with open ('datos/8G.json', 'a') as f3:
    f3.write(A)

del A
