def binary_search(list,target):
    first = 0;
    last = len(list) -1
    
    while first <= last:
        mid_point = (first + last) // 2
        if list[mid_point] == target:
            return mid_point
        elif list[mid_point] < target:
            first = mid_point + 1
        else:
            last = mid_point - 1

    return None

numbers = [8,6,2,4,7,1,3,0]
numbers.sort()

result = binary_search(numbers, 7);
print(result)       
