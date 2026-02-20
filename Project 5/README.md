# 😊 Real-Time Facial Emotion Detection

A real-time facial emotion recognition system built with Python, OpenCV, and a deep learning model (Keras/TensorFlow). The system captures live video from a webcam, detects faces using Haar Cascade classifiers, and predicts the emotional state of each detected face.

---

## 📸 Demo

> Detects faces in real-time and classifies emotions directly on the video feed.
![istockphoto-1496615445-612x612 jpg](https://github.com/user-attachments/assets/2d1a8053-2fbd-4f97-ad89-de7b59e258d0)

```

```

---

## 🧠 Detected Emotions

The model is trained to recognize the following 7 universal emotions:

| Label | Emotion   |
|-------|-----------|
| 0     | Angry     |
| 1     | Disgust   |
| 2     | Fear      |
| 3     | Happy     |
| 4     | Sad       |
| 5     | Surprise  |
| 6     | Neutral   |

---

## 🗂️ Project Structure

```
emotion-detection/
│
├── emotion_detection.py                  # Main script for real-time detection
├── emotion_model.hdf5                    # Pre-trained Keras CNN model
├── haarcascade_frontalface_default.xml   # OpenCV Haar Cascade for face detection
└── README.md
```

---

## ⚙️ Requirements

- Python 3.7+
- OpenCV
- TensorFlow / Keras
- NumPy

Install all dependencies with:

```bash
pip install opencv-python tensorflow numpy
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the detector

```bash
python emotion_detection.py
```

> Press **`q`** to quit the webcam window.

---

## 🔍 How It Works

1. **Face Detection** — OpenCV reads each frame from the webcam and applies the `haarcascade_frontalface_default.xml` classifier to locate faces in the frame.
2. **Preprocessing** — Each detected face region is cropped, converted to grayscale, resized to `48×48` pixels, and normalized.
3. **Emotion Prediction** — The preprocessed face is passed to a pre-trained CNN (`emotion_model.hdf5`) which outputs probability scores for each of the 7 emotion classes.
4. **Annotation** — The predicted emotion label and confidence are overlaid on the video frame using OpenCV drawing functions.

---

## 🏗️ Model Architecture

The emotion classifier is a Convolutional Neural Network (CNN) trained on the [FER-2013 dataset](https://www.kaggle.com/datasets/msambare/fer2013). The model was saved in Keras HDF5 format (`emotion_model.hdf5`).

- **Input:** 48×48 grayscale face image
- **Output:** Softmax probabilities over 7 emotion classes
- **Framework:** TensorFlow / Keras

---

## 📦 Dataset

The model was trained on the **FER-2013** (Facial Expression Recognition) dataset, which contains ~35,000 labeled 48×48 grayscale face images across 7 emotion categories.

- 📎 [FER-2013 on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)

---

## 🛠️ Customization

- **Use a different model:** Replace `emotion_model.hdf5` with your own Keras model and update the label dictionary in `emotion_detection.py`.
- **Use a video file instead of webcam:** Change `cv2.VideoCapture(0)` to `cv2.VideoCapture('your_video.mp4')`.
- **Adjust detection sensitivity:** Tune the `scaleFactor` and `minNeighbors` parameters in `detectMultiScale()`.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, improvements, or new features.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [OpenCV](https://opencv.org/) for the Haar Cascade face detector
- [FER-2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013) for training data
- [Keras / TensorFlow](https://keras.io/) for the deep learning framework
