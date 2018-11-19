dict = {}
list = []
max_age = 0
def maxAge(smth):
	if len(smth) > 0:
		dict = smth.pop(0)
		list.append(dict["age"])
		return maxAge(smth)
	else:
		max_age = max(list)
		return max_age
op = [
	{
		"name":"Bob",
		"age":20,
		"marks":{
					"Math":98,
					"Python":100
				}
	},
	{
		"name":"Boba",
		"age":19,
		"marks":{
					"Physic":98
				}
	},
	{
		"name":"Boban",
		"age":22,
		"marks":{}
	}
]
print(maxAge(op))