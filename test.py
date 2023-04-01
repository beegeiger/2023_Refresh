import itertools

perm = itertools.product("01", repeat=4)

for it in list(perm):
	print(it, type(it))