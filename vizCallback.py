import numpy as np
from plot import Mapper 
from compress import Compressor
from tensorflow.keras.callbacks import Callback

class TrainViz(Callback):
	def __init__(self, metricColors : list, bg_color : tuple = (1, 1, 1), fps: int = 3):
		super(TrainViz, self).__init__()
		self.frames = []
		self.colors = metricColors 
		self.bg_color = bg_color 
		self.fps = fps 
		self.names =  [] 
		self.frames = [] 
		self.points = [] 

#---------------------------------------------------------------------------------------|

	def on_epoch_end(self, epoch, logs=None): 
		if logs is not None:
			for i, (name, val) in enumerate(logs.items()):
				if len(self.names) < len(logs):
					self.names.append(name)
				if len(self.points) < len(logs):
					self.points.append([[epoch, val]])
				else:
					self.points[i].append([epoch, val])
			if len(self.points[0]) >= 2:
				mapper = Mapper(np.array(self.points), self.colors, self.bg_color)
				graph = mapper.plot(self.names) 
				self.frames.append(graph)

#---------------------------------------------------------------------------------------|

	def on_train_end(self, logs=None):
		mapper = Mapper(np.array(self.points), self.colors, self.bg_color)
		graph = mapper.plot(self.names) 
		self.frames.append(graph)
		compressor = Compressor(self.frames)
		compressor.compress()
