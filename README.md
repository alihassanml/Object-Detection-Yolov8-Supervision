# Object Detection with YOLOv8 and Supervision

This project demonstrates object detection using the YOLOv8 model with video annotation, utilizing `supervision` for tracking and labeling, and `opencv` for video processing.

![Watch the video](./Annotated.gif)
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/alihassanml/Object-Detection-Yolov8-Supervision.git
   cd Object-Detection-Yolov8-Supervision
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have `opencv-python`, `supervision`, and `ultralytics` installed.

## Usage

1. Place your input video in the root directory of the project (e.g., `Shopping.mp4`).

2. Run the object detection script:

   ```bash
   python detect.py
   ```

3. The annotated video will be saved as `Annotated_Shopping.mp4`.

## Description

- **Object Detection**: YOLOv8 is used to detect objects in a video.
- **Tracking**: `ByteTrack` is used for tracking objects across frames.
- **Annotation**: Bounding ellipses and labels are drawn for detected objects.
- **Output**: Annotated video is saved to a file.
