# YOLO11: Run the Latest Real-time Object Detection Model Locally

![Cover Image](https://github.com/Brianhulela/yolov11_object_detection/blob/master/images/cover.jpg)

## Overview

This repository provides a simple guide on how to run the [YOLO11](https://docs.ultralytics.com/models/yolo11/) object detection model locally. YOLO11 improves on previous versions with faster inference times and enhanced accuracy, making it ideal for real-time applications like object tracking, image segmentation, and pose estimation.

By following the steps below, you’ll be able to set up the environment, load an image, and run YOLO11 to detect objects in your chosen images.

## How to Run

### 1. Create a Virtual Environment
Before running the YOLO11 model, create a Python virtual environment to manage the required dependencies. If you're unfamiliar with virtual environments, please check my [virtual environment tutorial](https://medium.com/@brianhulela/how-python-virtual-environments-transformed-my-coding-workflow-b116457db157).

Once you have created and activated the virtual environment, install the required library with the following command:

```
pip install -r requirements.txt
```

### 2. Download and Load an Image
After setting up your environment, you'll need an image to run object detection on. You can either use an image of your choice or download one from a free image source such as [Unsplash](https://unsplash.com/). 

Use any image loading tool (like OpenCV) to load the image into your script.

### 3. Load the YOLO11 Model and Run Inference
Next, load the pre-trained YOLO11 model. YOLO11 offers several model sizes (YOLO11n, YOLO11s, YOLO11m, YOLO11l, YOLO11x), each optimized for different use cases. In this example, we'll be using YOLO11x for its balance of speed and accuracy.

Once the model is loaded, run inference on the image to detect objects and obtain bounding boxes.

### 4. Draw Bounding Boxes
To visualize the detections, draw bounding boxes around the detected objects. You can use any visualization tool (like OpenCV) to display the image with the bounding boxes.

### 5. Save the Results
Finally, save the image with the detected objects to your local machine.

## Conclusion
This repository provides an easy way to run YOLO11 locally for real-time object detection. Feel free to modify the code to suit your needs, experiment with different model sizes, or even try out different datasets. 

If you have any questions or run into issues, feel free to open an issue or leave a comment.
