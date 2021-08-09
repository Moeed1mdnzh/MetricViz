import cv2
import numpy as np 

class Mapper:
	#Initialization
	def __init__(self, points : np.ndarray, metricColors : list, bg_color : tuple = (1, 1, 1)):
		self.points = points 
		self.colors = metricColors 
		self.bg_color = bg_color

#--------------------------------------------------------------------------------------------------------------|

	#Plotting points from every given metric
	def plot_points(self, graph : np.ndarray, points : np.ndarray
					, colors : list, minimas : list, maximas : list) -> np.ndarray: 
		space_map = np.zeros((400, 550, 3), np.uint8)
		H, W = graph.shape[:2]
		H, W = H - 10, W - 20
		space_map = self.fill(space_map.copy(), self.bg_color)
		for pts, color in zip(points, colors):
			new_pts = np.array(np.vstack((
				np.interp(pts[:, 0], tuple(minimas), (10, 540)),
				np.absolute(400-np.interp(pts[:, 1], tuple(maximas), (10, 390))))
				).T, dtype=np.int0)
			cv2.polylines(space_map, [new_pts], False, color, 2)
			last_point = new_pts[-1]
			cv2.circle(space_map, (last_point[0]-8, last_point[1]), 10, color, -1)
		graph[30:H-40, 70:W] = space_map
		return graph

#--------------------------------------------------------------------------------------------------------------|

	#Fill the graph with the given color
	def fill(self, graph : np.ndarray, color : tuple) -> np.ndarray:
		graph[:] = color 
		return graph

#--------------------------------------------------------------------------------------------------------------|

	#Configure the info related to each plot
	def show_legend(self, org : np.ndarray, detail : list, color : tuple) -> list:
		graph = np.zeros((480, 760, 3), dtype=np.uint8)
		graph = self.fill(graph.copy(), self.bg_color)
		graph[:, 120:760] = org
		color = - np.array(color, np.uint8)
		neg_color = (int(color[0]), int(color[1]), int(color[2]))
		X, y = 20, 40 
		for metric, color in zip(*detail):
			cv2.putText(graph, metric, (X-5, y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, neg_color, 2)
			cv2.line(graph, (X, y+20), (X+60, y+20), color, 4) 
			y += 40
		cv2.rectangle(graph, (10, 20), (130, y-10), neg_color, 2)
		return graph

#--------------------------------------------------------------------------------------------------------------|

	#Calculate global minimas and maximas
	def calc_globalPoints(self, points : list):
		#=======================================================|
		#                X                      Y               |
		minimas = [points[:, :, 0].min(), points[:, :, 1].min()]
		#===> [epoch-batch.min(), points.min()]                 |
		#=======================================================|
		#===> [epoch-batch.max(), points.max()]                 |  
		maximas = [points[:, :, 0].max(), points[:, :, 1].max()]
		#                X                      Y               |
		#=======================================================|
		return minimas, maximas

#--------------------------------------------------------------------------------------------------------------|

	#The name itself says it all
	def show_axes(self, graph : np.ndarray, minimas : list, maximas : list, color : tuple):
		H, W = graph.shape[:2]
		H, W = H - 10, W - 20
		color = - np.array(color, np.uint8)
		color = (int(color[0]), int(color[1]), int(color[2]))
		#Draw the axes
		#===============================================
		cv2.line(graph, (20, H-10), (20, 10), color, 2)
		cv2.line(graph, (20, H-10), (W, H-10), color, 2)
		#===============================================
		#Draw xticks and yticks based on global points
		#======================================================================================================
		xticks = [[[50, H-15], [50, H-5]], [[W-20, H-15], [W-20, H-5]]]
		yticks = [[[15, H-40], [25, H-40]], [[15, 30], [25, 30]]] 
		minimas[1], maximas[0] = maximas[0], minimas[1]  
		for xtick, ytick, gb_pt1, gb_pt2 in zip(xticks, yticks, minimas, maximas):
			cv2.line(graph, tuple(xtick[0]), tuple(xtick[1]), color, 2)
			cv2.line(graph, tuple(ytick[0]), tuple(ytick[1]), color, 2)
			xtick[0][0] -= 5
			xtick[0][1] -= 5
			ytick[0][0] += 10 
			ytick[0][1] -= 5
			cv2.putText(graph, str(int(gb_pt1)), tuple(xtick[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
			cv2.putText(graph, str(round(gb_pt2, 2)), tuple(ytick[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
		#======================================================================================================
		return graph

#--------------------------------------------------------------------------------------------------------------|

	#Adds required details
	def preprocess(self, points : list):
		graph = np.zeros((480, 640, 3), dtype=np.uint8)
		graph = self.fill(graph.copy(), self.bg_color)
		minimas, maximas = self.calc_globalPoints(points)
		graph = self.show_axes(graph.copy(), minimas, maximas, self.bg_color)
		self.plot_points(graph, self.points, self.colors, minimas, maximas)
		return graph


#--------------------------------------------------------------------------------------------------------------|

	#Main function(brain of the class)
	def plot(self, metrics : list) -> np.ndarray:
		graph = self.preprocess(self.points)
		graph = self.show_legend(graph, [metrics, self.colors], self.bg_color)
		return graph