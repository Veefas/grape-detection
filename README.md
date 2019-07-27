## EcoBot-Grape-Detection

The computer vision used in our participation in SFU's sustainable waste-sorting robots competition [2nd Place](http://www.sfu.ca/fas/news-and-outreach/years/2019/student-teams-battle-eco-bots-at-fas-competition.html)
   
Grapes are detected based on the colour, the circular shape and size of the contour. 


### Getting Started
1. Clone the project 
```
https://github.com/tsa87/EcoBot-Grape-Detection.git
```
2. Install the prerequisites
```
pip install argparse
pip install numpy
pip install opencv-contrib-python
pip install imutils
```
3. Run the demo
```
# on video file
python objectTracking.py -v PATH_TO_VIDEO
```
```
# from camera stream
python objectTracking.py.py
```

### Project Demo
![](https://media.giphy.com/media/WQCTg6mky4hwlubgjg/giphy.gif)

### Limitations

1. Green grapes are not detected in this implementation, multiple colour support could be added in the future./

2. Under a purple/green background, a simple colour detection implementation is not sufficent.

### Author

* **Tony Shen** - *Initial work* 

