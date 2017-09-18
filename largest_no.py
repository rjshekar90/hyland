
# largest number in array

def largest(arr):
    largest_no = arr[0]

    for num in arr[1:]:
        if num > largest_no:
            largest_no = num

    return largest_no

print largest([100, 200, 500, 300, 55 ])
