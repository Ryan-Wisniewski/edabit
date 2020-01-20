# def simon_says(lst1, lst2):
# 	#return true if second list is the first shifted voer by 1
#     for x in lst1:
#         pass
#         # print(x)
#     for x in range(1, len(lst2)):
#         if lst2[x] != lst1[x-1]:
#             # print('false')
#             return False
#         else: 
#             # print('true')
#             return True
#         print(lst2[x], 'yeet_son', lst1[x-1])

# # simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
# simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])



# def can_alternate(s):
# 	#takes a binary string and sees if it can split the 0's and 1's evenly
#     counter_x = 0
#     counter_y = 0
#     for x in s:
#         if x == '0':
#             counter_x += 1
#             # print(counter_x)
#         elif x == '1':
#             counter_y += 1
#             # print(counter_y)
        
#     # print(counter_x, counter_y)
#     if counter_x >= counter_y - 1 and counter_x + 1 <= counter_y:
#         # print('t1', counter_x, counter_y)
#         return True
#     elif counter_x + 1 >= counter_y and counter_x - 1 <= counter_y:
#         # print('t2', counter_x, counter_y)
#         return True
#         # print(x)
#     else: 
#         # print('f', counter_x, counter_y)
#         return False

# # can_alternate("000101")
# # can_alternate("010101")
# # can_alternate("1100101")
# # can_alternate("101")
# # can_alternate("000")




# def name_shuffle(txt):
# 	#replaces first with last name
#     x = txt.split(' ')
#     newStr = f'{x[1]} {x[0]}'
#     # print(newStr)

# name_shuffle("Donald Trump")
# name_shuffle("Rosie O'Donnell")
# name_shuffle("Seymour Butts")



##Solution 1
# def filter_list(l):
#     #filters anything not an int
#     for x in l:
#         # print(type(x))
#         if type(x) == int:
#             print(x)

## NW NW
# def filter_list(l):
#     x = [type(x) == int for x in l]
#     print(x)

# filter_list([1, 2, 3, "x", "y", 10])
# filter_list([1, "a", 2, "b", 3, "c"])



# import datetime
# def time_for_milk_and_cookies(date):
#     if date.month == 12 and date.day == 24:
#         return True
#     print(date.month)

# time_for_milk_and_cookies(datetime.date(2013, 12, 24))
# time_for_milk_and_cookies(datetime.date(2013, 1, 23))


# def XO(txt):
#     counter_x = 0
#     counter_y = 0
#     for i in txt:
#         print(i)
#         if i == 'x' or i == 'X':
#             counter_x += 1
#             print('x', counter_x)
#         elif i == 'o' or i == 'O':
#             counter_y += 1
#             print('y', counter_y)
#     if counter_x == counter_y:
#         # print('t')
#         return True
#     else: return False
# XO("ooxx")
# XO("xooxx")


# def double_char(txt):
#     newStr = ''
#     x = [i * 2 for i in txt]
#     # print(x)
#     print(newStr.join(x))
#     # print('plswork', newStr.join(x))

# double_char("String")
# # double_char("Hello World!")


# def length(txt):
# 	index = 0
# 	print(index, txt)
# 	def get_length(txt, index):
# 		count = index
# 		print(len(txt), count)
# 		if len(txt) == 0:
# 			print('ree',count)
# 			return count
# 		else:
# 			count += 1		
# 			get_length(txt[:len(txt)-1], count)
# 		count = index
# 		print('I hate hoisting in python though', index, count)
# 		return index
		
# 	get_length(txt, index)
# 	print('index',index)

# def length(txt):
# 	count = 0
# 	if count == len(txt):
# 		return count
# 	count += 1
# 	length[count:len(txt)]

#freaking reeee... so it just membe's numbers
#okay..
#OHHH derp because thats what its returning. neat now I feels dumb
# def length(txt):
# 	if len(txt) == 0:
# 		return 0
# 	else:
# 		return 1 + length(txt[1:])
# print(length('poop'))

print([x * 2 for x in range(0, 20)])





