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

def calculate_haversine_area(latitude_a, longitud_a, latitude_b, longitud_b):
	"""
	The haversine formula determines the great-circle distance between two points on
	a sphere given their longitudes and latitudes. The law of haversines, calculates
	the area of a spherical triangle.
	
	Args:
		latitude_a (float): Latitude point of the main location.
		longitude_a (float): Longitud point of the main location.
		latitude_b (float): Latitude point of the secondary location.
		longitude_b (float): Longitud point of the secondary location.

	Returns:
		area (float): The area of the spherical triangle
	"""
	haversine_longitud = calculate_haversine_angle(variable_a=longitud_a, variable_b=longitud_b)
	haversine_latitude = calculate_haversine_angle(variable_a=latitude_a, variable_b=latitude_b)

	area = haversine_latitude + math.cos(math.radians(latitude_a)) * math.cos(math.radians(latitude_b)) * haversine_longitud
	
	return area

def calculate_distance(latitude_a, longitud_a, latitude_b, longitud_b):
	"""
	Using the haversine formula, calculate the distance in km, between two points.
	The haversine formula determines the great-circle distance between two points
	on a sphere given their latitude and longitude.

	Args:
		latitude_a (float): Latitude point of the main location.
		longitude_a (float): Longitud point of the main location.
		latitude_b (float): Latitude point of the secondary location.
		longitude_b (float): Longitud point of the secondary location.

	Returns:
		distance (float): The distance in kilometers between two points.
	"""
	earth_radius = 6371
	distance = 0

	distance = 2 * earth_radius * math.asin(math.sqrt(calculate_haversine_area(latitude_a, longitud_a, latitude_b, longitud_b)))

	return round(distance, 1)
