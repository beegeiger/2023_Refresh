import itertools

perm = itertools.product("-+", repeat=4)

for it in list(perm):
	print(it, type(it))