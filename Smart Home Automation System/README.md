# 🏠 Smart Home Automation System

## 📘 Project Overview

This is an intermediate-level Object-Oriented Programming (OOP) project designed to be completed within **one hour**. The goal is to practice the **principle of composition** in OOP by simulating a basic smart home automation system.

---

## 🧠 Scenario

You're tasked with building a simple smart home system that can control various household appliances using a central controller. The system should allow grouped actions like turning off all devices or activating "Night Mode".

---

## 🧱 Core Components

- **Devices**:
  - `Light`: Should support `turn_on()` and `turn_off()`.
  - `Thermostat`: Should support `set_temperature()` and `turn_off()`.
  - `SecurityCamera`: Should support `start_recording()` and `stop_recording()`.

- **SmartHomeController**:
  - This class is **composed of** the above device classes.
  - It should provide:
    - `turn_off_all_devices()`
    - `activate_night_mode()`: Turns off lights, lowers thermostat, starts camera recording

Each device should maintain its own **state**, and the controller should **delegate** actions using **composition** rather than inheritance.

---

## 🚀 Optional Extensions

If you have time left:
- Add a `Room` class composed of multiple devices.
- Include a simple `Scheduler` class to simulate time-based operations.
- Track command history to allow undoing last actions.

---

## ✅ Objective

- Apply **OOP composition** principles
- Practice clean and modular design
- Reinforce class relationships and delegation

---

## 💡 Tip

Focus on **composition over inheritance**. Your `SmartHomeController` should not inherit from the devices—it should **contain** them.

