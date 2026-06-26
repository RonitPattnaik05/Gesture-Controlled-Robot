File: gesture_bt_predict.py 
#!/usr/bin/env python3 
import time 
import serial 
import joblib 
import numpy as np 
import pandas as pd 
from collections import deque 
 
PORT = "/dev/rfcomm0" 
BAUD = 115200 
 
MODEL_FILE = "gesture_model.pkl" 
SCALER_FILE = "scaler.pkl" 
 
FEATURES = [ 
    "flex1","flex2", 
    "ax","ay","az", 
    "gx","gy","gz" 
 
 
] 
 
WINDOW_SIZE = 5 
CONFIDENCE_THRESHOLD = 0.55 
 
print("Starting Gesture Recognition...") 
 
model = joblib.load(MODEL_FILE) 
scaler = joblib.load(SCALER_FILE) 
 
ser = serial.Serial(PORT, BAUD, timeout=1) 
buffer = deque(maxlen=WINDOW_SIZE) 
last_pred = None 
 
while True: 
    try: 
        line = ser.readline().decode(errors="ignore").strip() 
        if not line: 
            continue 
 
        values = line.split(",") 
 
 
        if len(values) != 8: 
            continue 
 
        frame = pd.DataFrame([values], columns=FEATURES, dtype=float) 
        frame_scaled = scaler.transform(frame) 
 
        probs = model.predict_proba(frame_scaled)[0] 
        confidence = np.max(probs) 
 
        if confidence < CONFIDENCE_THRESHOLD: 
            continue 
 
        pred = model.classes_[np.argmax(probs)] 
        buffer.append(pred) 
 
        final_pred = max(set(buffer), key=buffer.count) 
        if final_pred != last_pred: 
            print("Predicted Gesture:", final_pred) 
            last_pred = final_pred 
 
    except KeyboardInterrupt: 
 
 
        ser.close() 
        print("\nStopped") 
        break