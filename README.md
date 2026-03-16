# GPS-Based Fuel Deviation Detection System for Mining Vehicles

An end-to-end IoT solution for mining vehicle monitoring using GPS data, edge processing, a backend ingestion pipeline, and a live Mapbox dashboard.

This system detects:
- Route deviation
- Idle behavior
- high fuel consumption detection

It is designed as a practical mining operations monitoring system where GPS devices connected to a Raspberry Pi send location data, edge logic identifies inefficiencies, and a web dashboard visualizes live movement and alerts.

---

## Key Features

- Raspberry Pi interfacing with multiple GPS modules
- GPS data parsing:
  - Latitude
  - Longitude
  - Speed
  - Timestamp
- Edge-level detection logic for:
  - Route deviation
  - Idle behavior
  - Fuel anomaly detection
- Backend API for GPS ingestion
- MongoDB-based data storage
- Real-time dashboard using React + Mapbox
- Socket.IO live updates
- Replay mode for vehicle path visualization
- Alerts panel for active mining vehicle events

---

## System Architecture
End-to-End Flow
GPS modules connected to the Raspberry Pi provide real-time vehicle coordinates.
The edge Python application reads the GPS data.
Edge logic detects:
Route deviation
Idle behavior
Fuel anomaly
The processed payload is sent to the backend API.
The backend stores records in MongoDB.
The backend broadcasts updates using Socket.IO.
The frontend dashboard displays:
Live truck locations
Expected route / haul road
Alerts
Replay of movement history

## Installation and Setup

This project is organized into three separate repositories:

- **Backend repository**
- **Frontend repository**
- **Raspberry Pi / Edge repository**

Clone each repository separately and set them up as follows.

### 1. Backend Setup

Clone the backend repository:

```bash
git clone https://github.com/your-username/your-backend-repo.git
cd your-backend-repo
