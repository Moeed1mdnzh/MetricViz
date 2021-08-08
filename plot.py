import cv2
import numpy as np 

class Mapper:
	#Initialization
	def __init__(self, points : np.ndarray, metricColors : list, bg_color : tuple = (1, 1, 1)):
		self.points = points 
		self.colors = metricColors 
		self.bg_color = bg_color

#--------------------------------------------------------------------------------------------------------------

	#Plotting points from every given metric
	def plot_points(self, points : np.ndarray) -> np.ndarray:
		pass 

#--------------------------------------------------------------------------------------------------------------

	#Fill the graph with the given color
	def fill(self, graph : np.ndarray, color : tuple) -> np.ndarray:
		graph[:] = color 
		return graph

#--------------------------------------------------------------------------------------------------------------

	#Configure the info related to each plot
	def show_legend(self, detail : list) -> list:
		pass 

#--------------------------------------------------------------------------------------------------------------

	#Remove point if the graph is filled up
	def update(self, length : int) -> bool:
		pass

#--------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------

	#The name itself says it all
	def show_ticks(self, graph : np.ndarray, minimas : list, maximas : list, color : tuple):
		H, W = graph.shape[:2]
		H, W = H - 10, W - 20
		color = - np.array(color, np.uint8)
		color = (int(color[0]), int(color[1]), int(color[2]))
		cv2.line(graph, (20, H-10), (20, 10), color, 2)
		cv2.line(graph, (20, H-10), (W, H-10), color, 2)
		xticks = []
		yticks [] 
		for minima, maxima, loc in zip(minimas, maximas):
			pass
		return graph

#--------------------------------------------------------------------------------------------------------------

	#Adds required details
	def preprocess(self, points : list):
		graph = np.zeros((480, 640, 3), dtype=np.uint8)
		graph = self.fill(graph.copy(), self.bg_color)
		minimas, maximas = self.calc_globalPoints(points)
		graph = self.show_ticks(graph.copy(), minimas, maximas, self.bg_color)
		return graph


#--------------------------------------------------------------------------------------------------------------

	#Main function(brain of the class)
	def plot(self, metrics : list) -> np.ndarray:
		graph = self.preprocess(self.points)
		cv2.imshow("", graph)
		cv2.waitKey(0)

#--------------------------------------------------------------------------------------------------------------

def main():
	mapper = Mapper(np.array([[[1, 0.8], [2, 0.5], [3, 0.7], [4, 0.3], [5, 0.2]]]),
			[(150, 0, 150)], bg_color=(255, 255, 255))
	graph = mapper.plot(["loss", "accuracy"]) 


if __name__ == '__main__':
	main()