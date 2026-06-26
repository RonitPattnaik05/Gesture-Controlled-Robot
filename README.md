# Pi Gesture Recognition System 👋

A real-time hand gesture recognition system built for Raspberry Pi using Python, OpenCV, and TensorFlow. This project captures hand gestures via camera, processes them, and classifies them using a trained deep learning model.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features) 
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Training Your Own Model](#training-your-own-model)
- [Demo](#demo)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This system detects and classifies hand gestures in real-time using your Raspberry Pi camera. It's optimized to run on Pi 4/5 hardware with reasonable FPS. The pipeline includes data collection, model training, and live inference scripts.

**Use cases**: Smart home control, presentation navigation, robotics control, accessibility tools.

## ✨ Features

- **Real-time inference**: Processes Pi camera feed at 15-20 FPS
- **Custom gesture support**: Train on your own gesture dataset
- **Lightweight model**: Uses MobileNetV2 backbone for Pi compatibility  
- **Modular code**: Separate scripts for dataset creation, training, and inference
- **GPIO integration**: Trigger actions on gesture detection
- **Low latency**: <100ms inference time on Pi 4

## 📁 Project Structure

```
├── dtset.py           # Script to collect and build gesture dataset
├── model_train.py     # Trains CNN model on collected dataset
├── pi_gesture.py      # Main inference script for Raspberry Pi
├── README.md          # You are here
└── models/            # Saved .h5 models after training
```

## 🔧 Requirements

**Hardware**
- Raspberry Pi 4 Model B or Pi 5 (2GB+ RAM recommended)
- Pi Camera Module or USB webcam
- MicroSD card 16GB+

**Software**
```
python >= 3.9
opencv-python
tensorflow >= 2.10
mediapipe
numpy
RPi.GPIO
```

## ⚡ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/pi-gesture.git
   cd pi-gesture
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   For Pi-specific OpenCV:
   ```bash
   sudo apt-get install libatlas-base-dev libjasper-dev
   ```

4. **Enable camera interface**
   ```bash
   sudo raspi-config
   # Interface Options > Camera > Enable
   ```

## 🚀 Usage

**1. Collect dataset**
```bash
python dtset.py --gesture rock --samples 200
```
Press `s` to save a frame, `q` to quit. Repeat for each gesture class.

**2. Train model**
```bash
python model_train.py --epochs 50 --batch_size 32
```
Model saves to `models/gesture_model.h5` after training.

**3. Run live detection**
```bash
python pi_gesture.py --model models/gesture_model.h5
```
Press `q` to exit. Detected gestures print to console and can trigger GPIO pins.

## 🧠 Training Your Own Model

1. Collect at least 150-200 images per gesture class using `dtset.py`
2. Ensure good lighting and varied backgrounds for robustness
3. Run `model_train.py` and monitor accuracy/loss
4. Aim for >90% validation accuracy before deploying

Default classes: `palm`, `fist`, `peace`, `thumbs_up`, `ok`. Edit `GESTURE_CLASSES` in `model_train.py` to customize.

## 🎬 Demo

| Gesture | Action |
| --- | --- |
| Palm | Turn on LED |
| Fist | Turn off LED |
| Peace | Take screenshot |
| Thumbs Up | Volume up |

## 🛠 Troubleshooting

| Issue | Fix |
| --- | --- |
| Camera not detected | Run `libcamera-hello` to test. Check ribbon cable |
| Low FPS | Reduce frame size in `pi_gesture.py` to 320x240 |
| ImportError: TensorFlow | Use `pip install tensorflow-lite-runtime` for Pi |
| GPIO warnings | Run script with `sudo` or add user to gpio group |

## 🤝 Contributing

Pull requests welcome! For major changes, open an issue first to discuss what you'd like to change. Please make sure to test on actual Pi hardware.

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

---

**Made with ❤️ for Raspberry Pi tinkerers** 

Questions? Open an issue or reach out on Threads @yourhandle
