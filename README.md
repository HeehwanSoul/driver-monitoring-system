# Driver Monitoring System (DMS)

Real-time driver monitoring prototype using Python and OpenCV for face and eye detection and drowsiness estimation.

## Current Status
- [x] Real-time webcam capture
- [ ] Face detection
- [ ] Eye detection / blink rate
- [ ] Drowsiness score + alert

## Tech Stack
- Python, OpenCV, NumPy

## Setup
```bash
pip install -r requirements.txt
python src/main.py
```

## Roadmap
- [x] Real-time webcam capture
- [x] Face detection (Haar)
- [ ] Eye tracking
- [ ] EAR-based drowsiness score
- [ ] Demo GIF + report

## Project Structure

```
driver-monitoring-system/
│
├── src/
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Performance (Target)

- FPS: 15+ on laptop webcam
- Latency: < 100 ms
- Platform: Windows (tested)

## Motivation

This project was developed to explore in-cabin safety systems and driver monitoring technologies in the context of ADAS.  
It aims to combine applied mathematics, computer vision, and real-time system design.

## Future Improvements

- Integration of deep learning-based face detection
- Robust performance under low-light conditions
- Embedded system deployment (e.g., Raspberry Pi)

## Author

**Heehwan Soul**  
Applied Mathematics Student  
GitHub: https://github.com/HeehwanSoul

