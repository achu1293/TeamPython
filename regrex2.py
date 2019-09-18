import re
#s=[210^"AAA"^"#COIMBATORE"^9876543213,211^"ABC"^"#MADRAS"^9877543213,212^"XYC"^9897543213,213^"#ERODE"^9897543218]
t=int(input())
d,l={},[]
d1={}
for n in range(t):
    s=input()
    m=len(s.split('^'))
    #for i in s.split(','):    
    for j in s.split('^'):
        if re.match("^[2]",j):            
            #d['id']=j
            a=j
        elif re.findall("^#[a-zA-Z]+",j):            
            d['address']=j        
        elif re.findall("^[a-zA-Z].+",j):            
            d['name']=j        
        elif re.findall("^[7|8|9][0-9]{9}$",j):
            d['mobile']=j
    #print("id is",d,d['id'])
    #a=d['id']
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
    print(i,end=" ")
    for n,m in j.items():
        print(m,end=" ")
    print()

#[['raj',23,5678],['ram',45,54768],['sam',34,7658]]


'''d3={}
for i in range(len(l)):
    k=l[i]['id']    
    if k not in d3:
        d3[k]=l[i]        
    else:
        d3[k].update(l[i])
print(d3)


print(d)
    l.append(d)
    d={}
print(l)
m,l1=0,[]
for i in l:
    m=len(i)
    l1.append(m)
m1=max(l1)
for i in l:
    if len(i)==m1:
        a=i.keys()
a=list(a)
m=list(l[0].keys())'''


#210^AAA^#COIMBATORE^9876543213,211^ABC^#MADRAS^9877543213,212^XYC^9897543213,212^#ERODE       
            
        
