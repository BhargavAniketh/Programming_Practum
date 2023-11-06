#Assignment-7
#PART-1

numbers = [200, 5, 4, 10, 8, 5, -3.3, 4.4, 0, -2, 0, -10, -44, 5, 3, 0, 3]


def find_min(numbers):
    min_value = numbers[0]
    for i in numbers:
        if i < min_value:
            min_value = i
    return min_value

#PART - 2 & 3

def sort_list(numbers, ascending=True):
    numbers2 = numbers.copy()
    sorted_numbers = []

    while numbers2:
        min_value = find_min(numbers2)  
        sorted_numbers.append(min_value)
        numbers2.remove(min_value)

    if not ascending:
        sorted_numbers = sorted_numbers[::-1]  
    
    return sorted_numbers

print("List: ", numbers)
print("Minimum value:", find_min(numbers))
print("Ascending numbers from the sorted list :", sort_list(numbers))
print("Descending numbers from the sorted list", sort_list(numbers, ascending=False))


