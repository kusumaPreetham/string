
list=["Preetham",1,True]
print(list)

lst:list=[]
lst.append("Preetham")
print(lst)

#Insert
a=["Preetham","Chanty","Ananth"]
a.insert(1,"Srikanth")
print(a)

#Count
a=["Preetham","Chanty","Ananth"]
print(a.count("Chanty"))
print(a.count("Srikanth"))

b=["Naveen","Preetham","Ananth"]
if(b.count("Srikanth")>0):
   print(b.index("Srikanth"))

#Update
a=["Preetham","Naveen","Ananth","Naveen"]
a[3]=("Naveen Kumar")
print(a)

#Extend
a=["Naveen","Preetham","Ananth"]
a1=["Srikanth","Gopi","Narendra"]
a.extend(a1)
print(a)
print(a1)

#Delete
#1)Remove
b=["Naveen","Preetham","Ananth"]
b.remove("Ananth")
print(b)

#2)Pop with index
a=["Naveen","Chanty","Preetham"]
a.pop(1)
print(a)

#3)Pop without index
a=["Naveen","Preetham","Ananth"]
a.pop()
print(a)
