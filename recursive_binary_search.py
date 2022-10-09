def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        mid_point = (len(list)) // 2 

        if list[mid_point] == target:
            return True
        else:
            if list[mid_point] < target:                
                return recursive_binary_search(list[mid_point + 1:],target)
            else:
                return recursive_binary_search(list[:, mid_point],target)


numbers = [8,6,2,4,7,1,3,0]
numbers.sort()

result = recursive_binary_search(numbers, 7);
print(result)       
