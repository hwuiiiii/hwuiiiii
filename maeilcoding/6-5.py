array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  # return if list contains only one element
  if len(array) <= 1:
    return array
  
  pivot = array[0] # set first element as pivot
  tail = array[1:] # set tail as rest
  
  left_side = [x for x in tail if x <= pivot] # elements equal to or smaller than of pivot
  right_side = [x for x in tail if x > pivot] # elements larger than pivot
  
  # return full quick sorted list 
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
  
