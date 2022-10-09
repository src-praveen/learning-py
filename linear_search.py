def linear_search(list, target_value):
    '''
        Return the index position of the taget value in the list else return None
    '''
    for idx in range(1,len(list)):
        if target_value == list[idx]:
            return idx

    return None        


def verify(idx):
    if idx is not None:
        print(f'Index found {idx}')
    else:
        print('Index not found')


numbers = [1,6,8,3,2,9,7,5]

result = linear_search(numbers, 9);

verify(result)
