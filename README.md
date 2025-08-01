# 🦖 Dino Game Hand Control – CV Powered

Control the Chrome Dino Game with your hand gestures using **OpenCV**, **MediaPipe**, and **PyAutoGUI** — no keyboard needed!

## ✋ What It Does

- 👋 Open hand → Idle  
- ✊ Closed fist → Dino Jumps!

Your webcam detects hand state in real-time and simulates a spacebar keypress using Python.

---

##  Tech Stack

- `OpenCV` – webcam video stream
- `MediaPipe` – real-time hand tracking (21 landmarks)
- `PyAutoGUI` – simulate keyboard events

---

##  How to Use

### 1. Install Requirements

```bash
pip install mediapipe opencv-python pyautogui
