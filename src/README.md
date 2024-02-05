
```
roslaunch yolov5_ros yolov5.launch input_image_topic:=/zed2/zed_node/rgb/image_rect_color/compressed
rosbag play -r 0.1 ./data/rosbag/02152023_front_avoid_passenger_1.bag
```