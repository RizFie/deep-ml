import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	mag = 0
	for each in gradient:
		mag += each**2
	magnitude = float(np.sqrt(mag))

	unit_vector = []
	for each in gradient:
		if int(magnitude) == 0:
			unit_vector.append(0.0)
		else:
			unit_vector.append(each/magnitude)

	descent = []
	for each in unit_vector:
		descent.append(-each)

	grad_dict = {
		'magnitude':magnitude,
		'direction':unit_vector,
		'descent_direction':descent
	}

	return grad_dict
