# use yolo3 to recognize traffic signs

fork from darknet, and I modify some files to train my own data.

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

## usage
- [make voc dataset and train](https://blog.csdn.net/qq_21578849/article/details/84980298)
- test 
  - use `test_txt.py` to generate txt file for testing
  - modify valid path in `cfg/voc.data` and seting for testing in `cfg/yolov3-voc.cfg`
  - run `./darknet detector valid cfg/voc.data cfg/yolov3-voc.cfg backup/yolov3-voc_final.weights` to test, the results is saved to `results` folder
  ```
  -gpu 0,1,2
  -thresh 0.1
  ```
  - this step is to transfer the results to my project required:
    - make folder `converted_txt`(*you can choose whatever you like, don't forget modify the name in the next step*) under `darknet`
    - make sure you have modified every path and folder name, run `convert.py`


