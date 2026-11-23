# Computer Vision with OpenCV

**Section 07 — Computer Vision · Part of AI Engineering Notes**

A complete, practical **Computer Vision** series in **Python with OpenCV** — **18 notebooks and 9 sample images**, organised in the exact order to learn them: image basics first, then transformations, colour, filtering, thresholding, morphology, edges, histograms, contours, detection, features and tracking, and finally six mini projects.

Every notebook follows the same pattern: concept in simple English, runnable code with saved outputs, key points, and a mini task to practise. All sample images live in [`assets/`](assets/) and every path is repo-relative — clone the repository and everything runs as-is.

---

## What This Section Covers

- Reading, writing, displaying and modifying images at the pixel level
- Drawing shapes and text, GUI events, blending and overlays
- Geometric transformations: resize, crop, flip, rotate, affine, perspective, letterboxing
- Colour spaces (BGR, grayscale, HSV, LAB, YCrCb) and HSV colour detection
- Arithmetic and bitwise operations, masks and compositing
- Filtering and blurring: convolution, Gaussian, median, bilateral, sharpening
- Thresholding: global, Otsu, adaptive, and `inRange`
- Morphological operations: erosion, dilation, opening, closing, gradient, top-hat
- Image gradients and Canny edge detection
- Histograms, equalization and CLAHE
- Contours, shape measurement and shape classification
- Template matching, Hough lines and circles, corner detection
- Video files and the webcam pattern, frame processing and FPS
- Face and object detection with Haar cascades — including their honest limits
- Feature detection and matching: ORB, SIFT, brute-force matching, homography
- Background subtraction, optical-flow tracking and QR code detection
- Six mini projects that combine everything

---

## Notebook Index

All notebooks are in [`opencv/`](opencv/).

| # | Notebook | What It Covers |
|---|----------|----------------|
| 01 | [Introduction and Image Basics](opencv/01-introduction-and-image-basics.ipynb) | Reading/writing images, shape and channels, pixels, splitting channels, ROI |
| 02 | [Drawing, Text and GUI Events](opencv/02-drawing-text-and-gui-events.ipynb) | Shapes, polygons, text labels, mouse callbacks, trackbar idea, blending |
| 03 | [Geometric Transformations](opencv/03-geometric-transformations.ipynb) | Resize, crop, flip, translation, rotation, perspective, pyramids, letterboxing |
| 04 | [Colour Spaces and Channels](opencv/04-color-spaces-and-channels.ipynb) | BGR, gray, HSV, LAB, YCrCb, `inRange` colour detection, centroids |
| 05 | [Arithmetic, Bitwise and Masking](opencv/05-arithmetic-bitwise-and-masking.ipynb) | `cv2.add`, AND/OR/XOR/NOT, masking, compositing, masked statistics |
| 06 | [Filtering and Blurring](opencv/06-filtering-and-blurring.ipynb) | `filter2D` kernels, Gaussian, median, bilateral, sharpening, blur score |
| 07 | [Thresholding](opencv/07-thresholding.ipynb) | Global, five threshold types, Otsu, adaptive, band thresholding |
| 08 | [Morphological Operations](opencv/08-morphological-operations.ipynb) | Erosion, dilation, opening, closing, gradient, line extraction |
| 09 | [Gradients and Edge Detection](opencv/09-gradients-and-edge-detection.ipynb) | Sobel, Scharr, Laplacian, gradient magnitude, Canny tuning |
| 10 | [Histograms and Equalization](opencv/10-histograms-and-equalization.ipynb) | `calcHist`, equalization, CLAHE, comparison, back projection |
| 11 | [Contours and Shape Detection](opencv/11-contours-and-shape-detection.ipynb) | `findContours`, area/perimeter, bounding boxes, shape classification, hull |
| 12 | [Template Matching, Hough and Corners](opencv/12-template-matching-hough-and-corners.ipynb) | `matchTemplate`, Hough lines/circles, Harris and Shi-Tomasi corners |
| 13 | [Video and Webcam](opencv/13-video-and-webcam.ipynb) | `VideoWriter`, `VideoCapture`, frame loops, seeking, webcam pattern, FPS |
| 14 | [Face and Object Detection — Haar](opencv/14-face-and-object-detection-haar.ipynb) | Haar cascades, `detectMultiScale` tuning, eye/smile, limits vs DNN |
| 15 | [Feature Detection and Matching](opencv/15-feature-detection-and-matching.ipynb) | Keypoints/descriptors, ORB, SIFT, BFMatcher, ratio test, homography |
| 16 | [Background Subtraction, Tracking and QR](opencv/16-background-subtraction-tracking-and-qr.ipynb) | MOG2, motion boxes, Lucas-Kanade optical flow, QR detection/decoding |
| 17 | [Mini Projects 1](opencv/17-mini-projects-1-document-scanner-color-tracker-motion.ipynb) | Document scanner, colour tracker, motion detector |
| 18 | [Mini Projects 2](opencv/18-mini-projects-2-cartoonifier-face-blur-gesture.ipynb) | Cartoonifier, face blur/pixelation, gesture basics with hull defects |

---

## Mini Projects

| Project | Notebook | Pipeline |
|---------|----------|----------|
| Document Scanner | 17 | Edges → largest 4-corner contour → perspective warp → adaptive threshold |
| Colour Tracker | 17 | HSV mask → morphology → moments centroid → trajectory |
| Motion Detector | 17 | Frame differencing → threshold → motion-area alarm rule |
| Cartoonifier | 18 | Adaptive-threshold edges + bilateral smoothing + k-means colours |
| Face Blur | 18 | Haar detection → Gaussian blur or pixelation of the face region |
| Gesture Basics | 18 | Skin mask (YCrCb) → largest contour → convex-hull defects → finger estimate |

---

## How to Run

```bash
# 1 — Clone this repository, then enter this section
cd ai-engineering-notes/07-computer-vision

# 2 — Install dependencies
pip install -r requirements.txt

# 3 — Open any notebook
jupyter lab
```

Notes for running the notebooks:

- Images are displayed with Matplotlib, so the notebooks run on any machine, including headless servers. The classic window functions (`imshow`, `waitKey`, trackbars and live webcam capture) are explained in the notebooks with example code to run on your own machine.
- Sample images are in [`assets/`](assets/) and are referenced as `../assets/...` from the notebooks — do not move them separately.
- Haar cascade results are reported honestly: the cascades are trained on real photographs, so the synthetic test drawing in the assets may return zero detections. The code is identical for real photos.

---

## Key Skills Gained

- Thinking in pixels, channels and masks — the foundation of all classic computer vision
- Building complete pipelines: load → convert → clean → detect → measure
- Choosing the right tool per problem: threshold vs colour range, Haar vs features, differencing vs background subtraction
- Tuning the parameters that actually matter: kernel sizes, Canny and threshold values, `detectMultiScale` settings
- Knowing the limits of classic methods and when a learned model is the better tool

---

## Structure

```text
07-computer-vision/
├── opencv/          # 18 notebooks, numbered in learning order
├── assets/          # 9 generated sample images used by the notebooks
├── requirements.txt # opencv-python, numpy, matplotlib, jupyter, ipykernel
└── README.md
```
