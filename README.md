# MetricViz
As you may have already seen in the description, this project is supposed to be a keras callback to visualize the computed **metrics** as graphs in an animation. <br />
Take a look at what i meant by the above sentence <br />
![Game Process](https://github.com/Moeed1mdnzh/MetricViz/blob/master/assests/video_test.gif)
<br />
To accomplish such a thing for your own keras models, you first need to complete a few steps.Don't be lazy ;)
## Steps
### step 1
Clone the repo and install requirements.txt using the below commands to get the packages installed on your *virtual environment*.
```python
git clone https://github.com/Moeed1mdnzh/MetricViz.git
pip install -r requirements.txt 
```
### step 2
Say that you are currently in the file of your keras model.Import the callback from the file **vizCallback.py**. 
```python
from vizCallback import TrainViz 
```
### step 3
Before using the callback,compile your model.To use the callback you have
to specify the callback and pass a couple of optional arguments to the model.Let me give you a quick guide about what these arguments are about
```python
callback = TrainViz(metricColors, bg_color = (1, 1, 1), fps = 3)
```
***1 - metricColors : A list containing each color for each metric*** <br />
***2 - bg_color : The color of the background(Don't set it to (0, 0, 0) for axes color purposes)*** <br />
***3 - fps : The frame rate for the animation(Default is recommended)*** <br />
*Set them on your own conditions.*

### step 4
Congrats you've made it through to the final step.<br />Pass the callback to the .fit function like the given example below
```python
model.fit(X_train, y_train, epochs=30, batch_size=64, callbacks=[callback], validation_data=(X_test, y_test))
```
Once the training finishes you should have two new files in your directory.One named as *<MetricViz-Output.avi>* which is the animation and the other one 
*<final.jpg>* which is the final graph associated with your model performance like the following image.
![](https://github.com/Moeed1mdnzh/MetricViz/blob/master/assests/image_test.jpg)
