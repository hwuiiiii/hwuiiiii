array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end : # end if only one element
		return
	pivot = start
	left = start + 1
	right = end
	
	while left <= right:
		
		while left <= end
