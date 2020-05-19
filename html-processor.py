import re

# open file
text = open('testpage.txt','r').read() 
newTxt = "" # string me to text sto opoi tha ginoun oles oi metatropes

# 1 eksagogi titlou
rexp = re.compile(r'<title>([^(</title>)]+)</title>')
m = rexp.search(text)
firstTxt = "Τιτλος: " + m.group(1) + "\n" +"Κειμενο:\n" # apothikebo prosorina to apotelesma gia na to grapso sto arxio argotera

print(m.group(1))
f1 = open('./myouts/1.txt','w')
f1.write(m.group(1))
f1.close()

# 2 apaloifi sxolion

rexp = re.compile(r'<!--([^-->]+)-->')
m = rexp.sub('<!-- -->', text)
f2 = open('./myouts/2.txt','w')
f2.write(m) # apothikebo to apotelesma se arxeio
newTxt += m # apothikebo to apotelesma gia na to epeksergasto xana

# 3 apaloifi script/style

rexp = re.compile(r'(<(script)|(style)[^>]*>)[^<]*(</(script)|(style))>')
m = rexp.sub(' ', text) # epexergasia sto arxiko keimeno
m2 = rexp.sub(' ', newTxt) # epexergasia sto apotelesma apo to zitoumeno 2
f3 = open('./myouts/3.txt','w')
f3.write(m) # apothikefsi tou apotelesmatos gia na tsekaro oti to re litourgi
newTxt = m2 # apothikebo to apotelesma gia na to epeksergasto xana

# 4 eksagogi href apo a

rexp = re.compile(r'<a .*(href="[^"]*")')
f4 = open('./myouts/4.txt','w')
for m in rexp.finditer(text):
    f4.write(m.group(1) + "\n") # apothikefsi ton href se arxeio


# 5 apaloifi ton tags

rexp = re.compile(r'(<[^>]+>)')
f5 = open('./myouts/5.txt','w')
m = rexp.sub(' ', text) # apotelesma tou re sto arxiko keimeno
m2 = rexp.sub(' ', newTxt) # apotelesma apo to epexargasmeno keimeno apo proigoumeno re
f5.write(m)
newTxt = m2

# 6 metatripi html entities

def cb(b): # briskei to adistixo simbolo gia na antikatastisi
    if b.group(1) =='amp':
        return '&'
    elif b.group(1) == 'gt':
        return '>'
    elif b.group(1) == 'lt':
        return '<'
    elif b.group(1) == 'nbsp':
        return ' '
    return 
rexp = re.compile(r'&((amp)|(gt)|(lt)|(nbsp));')
m = rexp.sub(cb,text) # apotelesma apo to arxiko keimeno
m2 = rexp.sub(cb,newTxt) #apotelesma apo epexergasmeno keimeno
newTxt = m2

f6 = open('./myouts/6.txt','w')
f6.write(m)

# 7 metatropi whitespace

rexp = re.compile(r'\s+')
m = rexp.sub(' ',text) #apotelesma apo to arxiko keimeno
m2 = rexp.sub(' ',newTxt) # apotelesma apo epexergasmeno keimeno
newTxt = m2

f7 = open('./myouts/7.txt','w')
f7.write(m)

fout = open('output.txt', 'w')
fout.write(firstTxt + newTxt) # apothikefsi se arxeio to apotelesma tou keimenou pou perase apo oles tis metatropes

# close file
# text.close()
# f2.close()

