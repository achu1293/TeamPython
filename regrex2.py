import re
#s=[210^"AAA"^"#COIMBATORE"^9876543213,211^"ABC"^"#MADRAS"^9877543213,212^"XYC"^9897543213,213^"#ERODE"^9897543218]
t=int(input())
d,l,l1,l2={},[],[],[]
d1={}
for n in range(t):
    s=input()
    m=len(s.split('^'))        
    for j in s.split('^'):
        if re.match("^[7]",j):       
            a=j
        elif re.findall("^#[a-zA-Z]+",j):            
            d['address']=j        
        elif re.findall("^[a-zA-Z].+",j):            
            d['name']=j        
        elif re.findall("^[7|8|9][0-9]{9}$",j):
            d['mobile']=j
    
    if a not in d1:
        d1[a]=d
    else:
        d1[a].update(d)
    d={}   
for i,j in d1.items():
    if m<len(j.keys()):
        m=len(j.keys())
        l=list(j.keys())
for i,j in d1.items():    
    for n in l:
        if n in list(j.keys()):
            pass
        else:
            j[n]="null"     
#print(d1)
for i,j in d1.items():
    l1.extend([i,j['name'],j['address'],j['mobile']])
    l2.append(l1)
    l1=[]
l2=sorted(l2,key=lambda i:i[0])
#print(l2)
for i in l2:
    for j in i:
        print(j,end="   ")
    print()
#210^AAA^#COIMBATORE^9876543213,211^ABC^#MADRAS^9877543213,212^XYC^9897543213,212^#ERODE       
            
        

            
        
