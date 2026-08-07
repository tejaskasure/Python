#date 23/07/2025
#use for space removing


name=" tejas"
print(name)
print(name.strip())

#left side space remove
name=" tejas"
print(name.lstrip())

#right side space remove
name="tejas "
print(name.rstrip())

#replace method
a="hello dear tejas"
print(a.replace("hello","hey"))

a="hello dear hello"
print(a.replace("hello","hey"))

a="hello dear hello"
print(a.replace("hello","hey",1))

a="hello dear hello"
print(a.replace("hello","hey",2))

#find function
#to find the index of character in string

h="annirudha"
print(h.index("r"))

#startwith() and Endwith()

#start with function()
d="tejas"
print(d.startswith("t"))

e="tejas" 
print(e.endswith("s"))
