

def bynary_search(numbers, number_to_find, low, high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    
    if numbers[mid] == number_to_find :
        return True
    elif numbers[mid] > number_to_find :
        return bynary_search(numbers, number_to_find, low, mid-1)    
    else:
    
        return bynary_search(numbers, number_to_find, mid+1, high)
    
    
    
    
if __name__ == "__main__" :
    numbers = [1,3,4,5,6,7,67,78,89,99]
    #          0 1 2 3 4 5 6 7 8 9  10
    number_to_find = int(input("Ingrese numero a buscar: "))
    
    result = bynary_search(numbers, number_to_find, 0, len(numbers)-1)
    
    if result:
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")
