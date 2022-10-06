def decor(fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner
@decor
def num():
    return 10
# num=decor(num)
print(num())











# importing libraries
# import time
# import math

# def calculate_time(func):
# 	def inner1(*args, **kwargs):
# 		begin = time.time()
# 		func(*args, **kwargs)
# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)
# 	return inner1
# @calculate_time
# def factorial(num):
# 	time.sleep(2)
# 	print(math.factorial(num))
# # calling the function.
# factorial(10)




