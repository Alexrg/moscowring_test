import math

def calculate_delta(variable_a, variable_b):
	"""
	Calculates the delta between two given variables.

	Args:
		variable_a (float): Variable a
		variable_b (float): Variable b

	Returns:
		variable_b - variable_a (float): The difference between the two given variables.
	"""
	return variable_b - variable_a

def calculate_haversine_angle(variable_a, variable_b):
	"""
	Calculates the haversine angle of the two given points. The haversine function
	computes half a versine of the angle θ.

	Args:
		variable_a (float): Variable a
		variable_b (float): Variable b

	Returns:
		haversine_angle (float): The calculated versine angle.  
	"""
	haversine_angle = math.pow(math.sin(math.radians(calculate_delta(variable_a=variable_a, variable_b=variable_b))/2),2)
	
	return haversine_angle