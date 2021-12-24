array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end : # end if only one element
		return
	pivot = start
	left = start + 1
	right = end
	
	while left <= right:
		# repeat until left index value is larger than pivot
		while left <= end and array[left] <= array[pivot]:
			left += 1
		# repeat until right index value is smaller than pivot
		while right > start and array[right] >= array[pivot]:
			right -= 1
		if left > right: # swap right index value with pivot if left index greater than right index
			array[right], array[pivot] = array[pivot], array[right]
		else: # swap left and right index values if right index is equal to or greater then left index
			array[left], array[right] = array[right], array[left]
	# quick sort for both sides after split
	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
