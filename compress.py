import cv2 
import numpy as np 

#Convert graphs into a video
class Compressor:
	#Initialization
	def __init__(self, frames : list, fps: int = 2):
		self.frames = frames
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		self.save = cv2.VideoWriter('MetricViz-Output.avi', fourcc, fps, (760,480))

#-----------------------------------------------------------------------------------|

	#Convert
	def compress(self):
		for frame in self.frames:
			self.save.write(frame)
		self.save.release()
