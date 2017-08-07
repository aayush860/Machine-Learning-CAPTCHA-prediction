# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:35:22 2017



@author: aayush bahrgava
"""
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("D:/EC_B_sem6.txt",sep="\t")
df=df[df.branch == 'EC']

x=len(df.branch)
w=df[df.status != 'PASS']
failnglen=len(w)
print w
fail=len(w[w.status != 'PASS WITH GRACE'])
passlen=x-failnglen
print "pass:"+str(passlen)
print "fail:"+str(fail)
pswgr=x-((passlen)+fail)
print "pass with grace:"+str(pswgr)


                ###pie chart

slices=[passlen,pswgr,fail]
acti=["PASS","PASS WITH GRACE","FAIL"]
color=["r","orangered","lightgray"]
pie=plt.pie(slices,
        labels=acti,
        colors=color,
        startangle=180,
        shadow= False,
        explode=(0.2,0.1,0.1),
        autopct='%1.1f%%')

plt1=plt.gcf()
plt.legend(slices,loc="lower left")
plt1.savefig("D:/ec/pieec.png",dpi=500)
plt.close()


                    ###acc to SGPA

df=df.sort(["SGPA"],inplace=False,ascending=False)
y=df.SGPA
x=range(len(df.SGPA))
print x
plt.bar(x,y,color='r')
#plt.((df.SGPA).plot(kind='bar'))

plt.xticks(x,df.name,rotation=90)
plt1=plt.gcf()
plt1.set_size_inches(20, 12)
for i,j in zip(x,y):
    plt.annotate(str(i+1),xy=(i-0.10,j))
    plt.annotate(str(j),xy=(i,j-.25),ha="center",rotation="90")

plt.title("Ranks according to SGPA",fontsize=22)
plt.xlabel("NAMES")
plt.ylabel("POINTERS")
plt.show()
plt.draw()
plt1.savefig("D:/ec/ecsem6-SGPA.png",dpi=500)
plt.close()
#plt.show()



                    ###acc to CGPA
df=df.sort(["CGPA"],inplace=False,ascending=False)
y=df.CGPA
x=range(len(df.CGPA))
print y
plt.bar(x,y,color='b')
#plt.((df.SGPA).plot(kind='bar'))

plt.xticks(x,df.name,rotation=90)
plt1=plt.gcf()
plt1.set_size_inches(20, 12)
for i,j in zip(x,y):
    plt.annotate(str(i+1),xy=(i-0.10,j))
    plt.annotate(str(j),xy=(i,j-.25),ha="center",rotation="90")
plt.grid(True)
plt.title("Ranks according to CGPA",fontsize=22)
plt.xlabel("NAMES")
plt.ylabel("POINTERS")
plt.show()
plt.draw()
plt1.savefig("D:/ec/pltEC-CGPA.png",dpi=600)
plt.close()
#plt.show()



                    ###acc to NAME(SGPA) pass fail

df=df.sort(["name"],inplace=False,ascending=True)                    
y=df.SGPA
x=range(len(df.SGPA))
#print y
#(df.status).iteritems()
col11=list()
for xx in (df.status).iteritems():
    print xx[1]
    if str(xx[1])=='PASS':
        col11.append('b')
    elif str(xx[1])=='PASS WITH GRACE':
        col11.append('lime')
    else:
        col11.append('r')
    

print("dfffdgggggggggggg")
print col11
plt.bar(x,y,color=col11)
#plt.((df.SGPA).plot(kind='bar'))

plt.xticks(x,df.name,rotation=90)
plt1=plt.gcf()
plt1.set_size_inches(20, 12)
#df.status
for i,j in zip(x,y):
    if col11[i]=="b":
        plt.annotate("PASS",xy=(i,j-.25),ha="center",rotation="90")
    elif col11[i]=="lime":
        plt.annotate("PASS WITH GRACE",xy=(i,j-.25),ha="center",rotation="90")
    else:
        plt.annotate("FAIL",xy=(i,j-.25),ha="center",rotation="90")

            #www[t].set_color('r')
    #plt.annotate(str("RNo.")+str(i+1),xy=(i-0.10,j))

#plt.grid(True)
plt.title("STATUS ANALYSIS ACCORDING TO NAMES",fontsize=22)
plt.xlabel("NAMES")
plt.ylabel("POINTERS")
plt.show()
plt.draw()
plt1.savefig("D:/ec/EC-SGPA.png",dpi=500)
plt.close()
#plt.show()


