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

# print([x * 2 for x in range(0, 20)])

# def unique_sort(lst):
# 	new_list = list(dict.fromkeys(lst))
# 	ordered_list = sorted(new_list)
# 	return ordered_list

# print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))


# def filter_list(lst):
# 	array = []
# 	# print(array)
# 	for x in lst:
# 		if type(x) == int:
# 			array.append(x)
# 	print(array)
# 	return array

# filter_list([1, 2, "a", "b"])

# arr = [x not in lst for x in range(1,10)]
# def missing_num(lst):
# 	arr = []
# 	for x in range (1,11):
# 		if x in lst:
# 			print('yeet',x)
# 			pass
# 		else:
# 			arr.append(x)
# 	print(arr)
# 	return arr

# missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])

# ###SORTED works on both letters and numbers lol.
# def alphabet_soup(txt):
# 	x = sorted(txt)
# 	ans = ''.join(x)
# 	print(ans)
# print(alphabet_soup("hello"))


# def unique(lst):
# 	num = 0
# 	for x in lst:
# 		if lst.count(x) == 1:
# 			print('yayy',x)
# 			num = x
# 			print('yeet',num)
# 	print(x, num)
# 	return num

# unique([3, 3, 3, 7, 3, 3])


# def is_stretched(s1, s2):
# 	new_arr = [x for x in s1]
# 	ans = []
# 	print(new_arr)
# 	for x in range(len(new_arr)):
# 		print(x, len(new_arr))
# 		try:
# 			if new_arr[x] == new_arr[x+1]:
# 				print('duupHERE0')
# 				pass
# 			else:
# 				ans.append(new_arr[x])
# 				print(ans)
# 		except IndexError:
# 			pass
# 		if len(s1) -1 == x:

# 			print('sweet')
# 			ans.append(new_arr[x])
# 			print(ans)
# print(is_stretched("pppaaannndddaaa", "panda"))

# def find_even_nums(num):
# 	ans = []
# 	for x in range(1, num + 1):
# 		if x % 2 == False:
# 			ans.append(x)
# 	return ans

# find_even_nums(8)


# import math
# def cone_volume(h, r):
# 	v = math.pi * (r ** 2) * (h/3)
# 	return round(v, 2)

# cone_volume(3, 2)

# def binary(decimal):
# 	x = bin(decimal)

# 	print(x[2:])
# 	return x[2:]

# binary(123)


# import hashlib
# def get_sha256_hash(txt):
# 	#nope im far to lazy to not use haslib
# 	#remember pass by reference vs passing by value.......
# 	t = txt.encode()
# 	t = hashlib.sha256(t).hexdigest()
# 	print(t)
# 	# print(hashlib.sha256(txt).hexdigest()) <-- This is using the og text even if you manipulate it
# 	return t
# get_sha256_hash('ree')


# def sum_numbers(n):
# 	#non recursive
# 	ans = 0
# 	## for x in range(1, n + 1):	
# 	## 	ans += x
# 	## return ans

# 	# recursive
# 	if n == 0:
# 		return n
# 	else:
# 		return n + sum_numbers(n-1)

# print(sum_numbers(5))

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)
# print(recur_factorial(5))

# def counterpartCharCode(char):
# 	if char.isupper() == True:
# 		return ord(char) + 32
# 	elif char.islower() == False:
# 		return ord(char) - 32
# 	else: return ord(char)

# counterpartCharCode('a')
import math
def scale_tip(lst):
	half = math.floor(len(lst) / 2)
	lst_left = lst[:half]
	lst_right = lst[half + 1:]
	print(lst_left, lst_right)
	left_check = 0
	right_check = 0
	for x in lst_left:
		left_check += x
	print(left_check)
	for x in lst_right:
		right_check += x
	print(right_check)
	if left_check > right_check:
		print('left')
		return "left"
	elif left_check < right_check:
		print('right')
		return "right"
	else:
		return "balanced"
scale_tip([1, 2, 3, "I", 4, 0, 0])