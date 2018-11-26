This is the repository (moved from gitlab) of the Spring 2018 project "Video as a Sensor" through the Illinois Geometry Lab. The configuration and weights will need to be downloaded from https://pjreddie.com/darknet/yolov2/. We post-processed the output of the darknet neural network (see below) to remember detections over multiple frames of a video and add features like blurring. Note that we did not modify the topology of the network, nor did we use any kind of RNN. Most of the changes from the vanilla darknet code are in src/image.c.

![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

#Darknet#
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).
