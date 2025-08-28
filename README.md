# Contrast Vision

A simple Python project that processes live video from the user's webcam and applies **color-contrast filtering** to enhance visibility. Each pixel is categorized into one of eight high-contrast colors (red, green, blue, yellow, magenta, cyan, black, or white) to improve distinction.

## Demo

>The program opens a webcam feed and shows the contrasted video in real time. The user can press any key to exit.
<img width="2001" height="1256" alt="image" src="https://github.com/user-attachments/assets/933c6ec6-f5ee-4ed1-8235-8858bda6506a" />
Figure 1: An outdoors image processed using contrastVision

## Features
- Real-time video processing using **OpenCV**
- Pixel-level color classification with **NumPy**
- Eight-color contrasted output for better visibility
- Lightweight frame processing for minimal latency

## Setup

Follow the steps below to get started:

1. Clone the repository:
```bash
git clone https://github.com/AdwitaK/contrast-vision.git
cd contrast-vision
```

2.  Install dependencies with:
```bash
pip install -r requirements.txt
```

3. Run program with:
```
python contrastVision.py
```
