from ultralytics import YOLO
import cv2
import urllib.request

# Download and read image
url, filename = ("https://images.unsplash.com/photo-1520919971261-fe0be1461d0b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTV8fHBlb3BsZSUyMGFuZCUyMGNhcnMlMjBpbiUyMHN0cmVldHxlbnwwfHwwfHx8MA%3D%3D", "scene.jpg")
urllib.request.urlretrieve(url, filename)    # Download image
image = cv2.imread(filename)

# Load a model
model = YOLO("yolo11x.pt")  # pretrained YOLO11x model

# Run batched inference on a list of images
results = model(image)  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk