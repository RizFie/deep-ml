def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	result_matrix = []
	result_multi = 0
	if len(a[0]) != len(b):
    	return -1

	for row in a:
		for x, y in zip(row, b):
			result_multi += x * y
			#print(result_multi)
		result_matrix.append(result_multi)
		result_multi = 0
		#print(result_matrix)
	
	return result_matrix