sourceFile = open('text.txt','a')
a = int(input())
b = int(input())
c = int(input())

m = a
if m < b:
    m = b
if m < c:
    m = c

print(m, file = sourceFile)
sourceFile.close()
