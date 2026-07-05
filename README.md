# 👁️ God's Eye
### Semi-Autonomous Intelligent Drone Surveillance System

<p align="center">
  <img src="block diagram/Drone (1).png" width="700">
</p>

---

## 📖 Overview

God's Eye is a semi-autonomous aerial surveillance system designed to intelligently detect, track, and monitor human targets using Computer Vision, Embedded Systems, and secure optical communication.

Unlike conventional surveillance drones that rely solely on wireless communication, God's Eye integrates **laser-based communication** between the drone and the ground station, significantly improving communication security by minimizing the possibility of signal interception.

The project combines software, electronics, mechanical design, and computer vision into a complete surveillance platform capable of real-time target detection, tracking, and secure ground communication.

---

# 🎯 Objectives

The project was designed to:

- Detect human targets in real time
- Automatically track detected subjects
- Securely communicate between drone and ground station
- Provide a scalable embedded surveillance platform
- Reduce dependence on conventional RF communication
- Demonstrate integration between AI, Embedded Systems and Robotics

---

# ✨ Key Features

- 🎥 Real-time Human Detection
- 👤 YOLO-based Object Detection
- 📡 Secure Laser Communication
- 🎯 Automatic Target Tracking
- 🔄 Pan-Tilt Camera Tracking System
- 🛰️ GPS Integration
- 🧭 Magnetometer-based Orientation
- ⚙️ Arduino Stepper Motor Control
- 🖨️ Custom Designed 3D Printed Tracking Mechanism
- 📷 Raspberry Pi Edge Processing
- 🔐 Optical Communication for Enhanced Security

---

# 🏗️ System Architecture

```
                   Camera Feed
                        │
                        ▼
                Raspberry Pi
                        │
         Human Detection (YOLO)
                        │
                        ▼
            Tracking Coordinates
                        │
                        ▼
             Arduino Controller
                        │
         Stepper Motor Tracking
                        │
                        ▼
          Laser Communication Link
                        │
                        ▼
               Ground Station
                        │
            Human Intervention
```

---

# 🛰️ System Components

## Drone Side

- Raspberry Pi
- Camera Module
- YOLO Human Detection
- Laser Communication Module
- GPS Module
- Magnetometer
- Embedded Power System

---

## Ground Station

- Arduino Controller
- Stepper Motors
- Laser Receiver
- Tracking Camera
- Human Monitoring Interface

---

# 🧠 How It Works

1. The Raspberry Pi continuously captures live video.

2. The onboard Computer Vision system detects human subjects.

3. Tracking coordinates are generated.

4. Coordinates are transmitted using a secure laser communication channel.

5. The ground station receives tracking information.

6. Arduino controls the pan-tilt mechanism using stepper motors.

7. The camera automatically follows the detected subject.

8. If an unknown or suspicious individual is detected, the operator can manually intervene, making the system semi-autonomous.

---

# 🔒 Why Laser Communication?

Traditional RF communication can be intercepted or jammed.

God's Eye explores laser-based communication because it offers:

- Line-of-sight communication
- Reduced interception risk
- Lower probability of signal interference
- Enhanced communication security
- Point-to-point data transmission

This makes the surveillance system significantly more secure than conventional RF-only solutions.

---

# 🧠 Computer Vision Pipeline

```
Camera Feed
      │
      ▼
Frame Processing
      │
      ▼
YOLO Human Detection
      │
      ▼
Target Localization
      │
      ▼
Coordinate Generation
      │
      ▼
Laser Transmission
```

---

# ⚙️ Embedded Control Pipeline

```
Coordinates
      │
      ▼
Arduino
      │
      ▼
Motor Control Logic
      │
      ▼
Stepper Motors
      │
      ▼
Camera Tracking
```

---

# 🛠️ Technologies Used

## Programming

- Python
- Arduino C++

---

## Computer Vision

- OpenCV
- YOLO

---

## Embedded Systems

- Arduino
- Raspberry Pi
- ESP32

---

## Hardware

- Stepper Motors
- GPS Module
- Magnetometer
- Laser Transmitter
- Laser Receiver
- Camera Module

---

## Design

- Fusion 360
- 3D Printing

---

# 📂 Repository Structure

```
God-s-Eye/

│
├── block diagram/
│   ├── Drone Architecture
│   └── Ground Station Architecture
│
├── codes/
│   ├── Motion Detection
│   ├── Laser Detection
│   ├── Motor Control
│   ├── GPS & Magnetometer
│   └── RF Experiments
│
└── README.md
```

---

# 💡 Engineering Highlights

This project integrates multiple engineering disciplines into a single surveillance platform.

Major engineering challenges addressed include:

- Real-time target tracking
- Secure optical communication
- Embedded motor synchronization
- Mechanical tracking system design
- GPS positioning
- Direction estimation using magnetometer
- Camera stabilization
- Hardware-software integration

---

# 🖨️ Mechanical Design

The tracking mechanism was:

- Designed from scratch in Fusion 360
- Optimized for dual-axis tracking
- Manufactured using 3D printing
- Integrated with Arduino-controlled stepper motors

The custom pan-tilt assembly enables smooth camera tracking while maintaining stability during operation.

---

# 📈 Development Process

Rather than developing a single implementation, the repository contains numerous experimental iterations covering:

- Motion detection algorithms
- Laser detection improvements
- Motor control optimization
- GPS experiments
- Magnetometer calibration
- Communication testing
- Tracking refinements

These iterations document the engineering process followed during system development.

---

# 🚀 Future Improvements

- Face Recognition Integration
- Autonomous Drone Navigation
- Multi-Target Tracking
- AI Threat Classification
- Night Vision Support
- Thermal Camera Integration
- Encrypted Optical Communication
- Edge AI Optimization
- Swarm Drone Communication
- Live Monitoring Dashboard

---

# 🌍 Potential Applications

- Border Surveillance
- Industrial Security
- Disaster Response
- Wildlife Monitoring
- Search & Rescue
- Military Reconnaissance
- Smart Surveillance Systems

---

# 📌 Project Highlights

✅ Semi-Autonomous Surveillance

✅ Computer Vision Tracking

✅ Secure Laser Communication

✅ Arduino Motor Control

✅ Raspberry Pi Edge Computing

✅ GPS & Magnetometer Integration

✅ Custom 3D Printed Hardware

✅ Embedded Systems Development

---

# 👨‍💻 Author

**Pulipaka Sudarshan Pavan Kumar**

Software Engineer | Computer Vision | Embedded AI | Intelligent Systems

GitHub: https://github.com/Sudarshan-Pavan

LinkedIn: *(Add your LinkedIn URL)*

---

## ⭐ If you found this project interesting, consider giving it a star!
