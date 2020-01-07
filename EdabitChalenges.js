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

def can_alternate(s):
	#takes a binary string and sees if it can split the 0's and 1's evenly
    counter_x = 0
    counter_y = 0
    for x in s:
        if x == '0':
            counter_x += 1
            # print(counter_x)
        elif x == '1':
            counter_y += 1
            # print(counter_y)
        
    # print(counter_x, counter_y)
    if counter_x >= counter_y - 1 and counter_x + 1 <= counter_y:
        print('t1', counter_x, counter_y)
        return True
    elif counter_x + 1 >= counter_y and counter_x - 1 <= counter_y:
        print('t2', counter_x, counter_y)
        return True
        # print(x)
    else: 
        print('f', counter_x, counter_y)
        return False

can_alternate("000101")
can_alternate("010101")
can_alternate("1100101")
can_alternate("101")
can_alternate("000")