# AI-Drone-Traffic-Controller (AIDTC)
AI-powered system for autonomous drone traffic management and collision avoidance.

## 🚀 Project Overview
AI Drone Traffic Controller (AIDTC) is an **AI-powered airspace management system** designed to ensure **safe, efficient, and autonomous drone operations**.  
It predicts potential collisions, reroutes drones dynamically, and visualizes live drone traffic in real time.

## 🎯 Objectives
- Monitor multiple drones simultaneously in shared airspace.  
- Predict and prevent potential mid-air collisions.  
- Optimize flight paths dynamically for efficiency.  
- Provide a real-time visual dashboard for situational awareness.  
- Enable scalable and safe integration of drones into urban airspace

## ⚙️ Features
- Real-time drone tracking and visualization  
- AI-based collision detection and avoidance  
- Dynamic route optimization for autonomous UAVs  
- Configurable safety thresholds  
- Simulation dashboard via Streamlit  

## 🧠 Methodology
1. **Data Simulation:** Generate drone telemetry (position, velocity, altitude).  
2. **Collision Prediction:** Compute distances; predict potential collisions.  
3. **Route Optimization:** Adjust drone paths dynamically using AI logic.  
4. **Visualization:** Display drone positions, safe zones, and alerts on a dashboard.  
5. **Scalability:** Future-ready for large fleets and urban airspace integration.

## 💻 Tech Stack
- **Backend:** Python, FastAPI  
- **AI/ML:** NumPy, Scikit-learn, TensorFlow (for future versions)  
- **Visualization:** Streamlit, Matplotlib, Plotly  
- **Database:** MongoDB / TimescaleDB (optional for real data)  
- **Simulation:** Drone telemetry in 2D/3D space  

## 📂 Files in Repository
- `app.py` – Streamlit demo for live simulation 
- `requirements.txt` – Python dependencies  
- `README.md` – Project documentation  

---

## ⚡ How to Run
1. Clone the repository:
```bash
git clone https://github.com/<your-username>/AI-Drone-Traffic-Controller.git
