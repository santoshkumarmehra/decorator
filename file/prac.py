#  *args 

# def myFun(*argv):
#     print(type(argv))
#     for arg in argv:
#         print(arg)


# myFun('Hello', 'santosh', '')


# def myFun(arg1, *argv):
# 	print("First argument :", arg1)
# 	for arg in argv:
# 		print("Next argument through *argv :", arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')





