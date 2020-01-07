def simon_says(lst1, lst2):
	#return true if second list is the first shifted voer by 1
    for x in lst1:
        pass
        # print(x)
    for x in range(1, len(lst2)):
        if lst2[x] != lst1[x-1]:
            # print('false')
            return False
        else: 
            # print('true')
            return True
        print(lst2[x], 'yeet_son', lst1[x-1])

# simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])