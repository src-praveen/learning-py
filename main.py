''' this for for loop test '''
def print_value():
    for i, itm in enumerate(list(range(100))):
        if itm == 50:
            print(i)
   
if __name__ == "__main__" :
    print_value()
