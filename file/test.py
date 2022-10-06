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
# factorial(10)

# # def decor(fun):
# #     def inner():
# #         a=fun()
# #         add = a+5
# #         return add
# #     return inner
# # @decor
# # def num():
# #     return 10
# # # res=decor(num)
# # print(num())


# def decor(func):
#     def inner_fun():
#         print("start execution")
#         func()
#         print("end execution")
#     return inner_fun
# @decor
# def num():
#     print("this is main function")
# num()



# # def hello_decorator(func):
# # 	def inner1():
# # 		print("Hello, this is before function execution")
# # 		func()
# # 		print("This is after function execution")
# # 	return inner1
# # def function_to_be_used():
# # 	print("This is inside the function !!")
# # function_to_be_used = hello_decorator(function_to_be_used)
# # function_to_be_used()



# # def create_adder(x):
# # 	def adder(y):
# # 		return x+y
# # 	return adder

# # add_15 = create_adder(15)
# # print (add_15(10))



# # string = 'abcCDCDCDCD'
# # substring = 'CDC'

# # count = 0
# # for i in range(len(string) - len(substring) + 1):
# #     if string[i:i+len(substring)] == substring:
# #         print(string)
# # print (count)




# # # Python program to illustrate functions
# # # can be passed as arguments to other functions
# # def shout(text):
# # 	return text.upper()
# # def whisper(text):
# # 	return text.lower()
# # def greet(func):
# # 	# storing the function in a variable
# # 	greeting = func("""Hi, I am created by a function
# # 					passed as an argument.""")
# # 	print (greeting)

# # greet(shout)
# # greet(whisper)



# # def shout(text):
# #     return text.upper()

# # yell = shout
# # print (yell('Hello'))


# # def outer_function():
# #     task = 'Read Python book chapter 3.'
# #     def inner_function():
# #         print(task)
# #     return inner_function
# # homework = outer_function()
# # homework()

# # def outer_function():

# #     def inner_function():

# #         print('I came from the inner function.')

# #     # Executing the inner function inside the outer function.
# #     inner_function()
# # outer_function()


# # def my_function():
# #     print('I am a function.')

# # description = my_function
# # print(description())

# # import os
# # def executor(func):
# #     func("this")




# # os.system('clear')
# # executor(print)

