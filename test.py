"""
このファイルに解答コードを書いてください


"""
import re

list=[]

num = []
str=[]
ind=[]
ans =[]
n=0

f = open('input.txt')
text = f.read()
f.close()

text = re.split('[\n:]',text)

for i in text:
    n+=1
    if n%2==1:
        num.append(i)
    else:
        str.append(i)

q = int(num[-1])

for i in num:
    y=int(i)
    if q%y==0:
        ind.append(num.index(i))
        
for m in ind:
    z = int(m)
    ans.append(str[m])

print(''.join(ans))
