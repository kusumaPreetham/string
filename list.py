#clear
a = ["preetham", "navya", "naveen"]
a.clear()
print(a)

#delete

#syntax:del variableName

name=["Navya","Preetham","Navven","Ahmed"]
del name[2]
print(name)

#input values

a=input("Enter a name:")
b=input("Enter a name:")
names=[]
names.append(a)
names.append(b)
print(names)


#sort

#syntax:lst.sort()

a=["Rose","Horse","Apple"]
a.sort()
print(a)

#without sort

a= [90,78,56,32,12,2]
n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)



#reverse

#syntax:lst.reverse()

a=["Rose","Horse","Apple"]
a.reverse()
print(a)


#Tuple

#implicit

#syntax:variableName=(item1,item2,...)

tpl=("eagle","monkey")
print(type(tpl))

#Explicit

#syntax:variableName=tpl((item1,item2,...))

tpl=tuple(("Ashok","Vijay"))
print(type(tpl))

#data type/Variable Annotation

#Syntax:variableName:tpl=((item1,item2,...)

tpl:tuple=(("Ashok","Vardhan"))
print(type(tpl))

#tuple Methods

#Count,Index

#count

#syntax:tpl.count(item)

tpl=(("eagle","money","snake","lion"))
print(tpl.count("money"))

tpl=tuple((1,2,3,1))
print(tpl.count(1))

#index

#syntax:tpl.index(item)

tpl=tuple(("eagle","money","lion"))
print(tpl.index("money"))


#conversion

tpl=tuple(("eagle","money","lion"))
lst=list(tpl)
print(type(lst))





