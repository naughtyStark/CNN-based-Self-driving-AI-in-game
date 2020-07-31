from pyroutelib3 import Router # Import the router
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter
from Bezier import *

def find_route(start_lat,start_lon,end_lat,end_lon):
	router = Router("car") # Initialise it
	start = router.findNode(start_lat, start_lon) # Find start and end nodes
	end = router.findNode(end_lat, end_lon)

	status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes

	if status == 'success':
		routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates
		# print(routeLatLons)
	Y = np.array([i[0] for i in routeLatLons])
	X = np.array([i[1] for i in routeLatLons])
	start_Y = Y[0]
	start_X = X[0]

	Y -= Y[0]
	Y *= 111392.84
	Y = np.dstack((Y[:-1],Y[:-1] + np.diff(Y)/2.0)).ravel()
	Y = np.dstack((Y[:-1],Y[:-1] + np.diff(Y)/2.0)).ravel()
	Y = gaussian_filter(Y,sigma=2)
	X -= X[0]
	X *= 111392.84
	X = np.dstack((X[:-1],X[:-1] + np.diff(X)/2.0)).ravel()
	X = np.dstack((X[:-1],X[:-1] + np.diff(X)/2.0)).ravel()
	X = gaussian_filter(X,sigma=2)
	
	set_track_width(10)
	slope = generate_slopes(X,Y)
	bx,by = get_bezier_track(X,Y,slope)

	# doing the following because working directly with GPS coordinates is not a great idea tbh. Also, these equations will only work near the equator (great for us as we live in india :P)
	bx /= 111392.84
	by /= 111392.84
	bx += start_X
	by += start_Y
	print(len(bx))
	plt.scatter(bx,by)
	# plt.scatter(X,Y)
	plt.axis('equal')
	plt.show()

if __name__ == '__main__':
	find_route(28.546655, 77.185267,28.544310, 77.192469)