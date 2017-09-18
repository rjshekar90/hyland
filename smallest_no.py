

#smallest_number

def smallest_no(arr):

    smallest_no = arr[0]

    for num in arr[1:]:
        if smallest_no > num:
            smallest_no = num

    return smallest_no

print smallest_no([100, 200, 500, 300, 55 ])
