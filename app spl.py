#string concatenation/joining append
#operation over loading
fname="preetham"
lname="kusuma"
print(fname+" "+lname)

#f"string/interpolation
fname="preetham"
lname="kusuma"
fullname=f"{fname} {lname}"
print(fullname)

#string join method
fname="preetham"
lname="kusuma"
lst=(fname, lname)
print(" ".join(lst))

#spring split
email="preethamkusuma@gmail.com"
print(email.split("@"))

#string split line
address: str="""
  alwyn colony,
  kphb colony,
  hyderabad,
  telangana,
  """
print(address.splitlines())

#string partion
email="@@.preethamkusuma007@gmail.com"
print(email.partition("@"))

#string repartition
email="a@preethamkusuma007@gmail.com"
print(email.rpartition("@"))