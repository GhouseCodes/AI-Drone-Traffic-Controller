import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="AI Drone Traffic Controller", layout="wide")

st.title("🛰️ AI Drone Traffic Controller (AIDTC)")
st.markdown("""
**An AI-powered system to manage drone airspace safely and efficiently.**
""")

# Parameters
NUM_DRONES = st.sidebar.slider("Number of Drones", 3, 15, 8)
COLLISION_DISTANCE = st.sidebar.slider("Safe Distance (meters)", 10, 100, 30)
SPEED = st.sidebar.slider("Drone Speed", 1, 10, 4)
REFRESH = st.sidebar.slider("Simulation Speed (sec)", 0.1, 1.0, 0.3)

# Initialize positions and directions
if "positions" not in st.session_state:
    st.session_state.positions = np.random.rand(NUM_DRONES, 2) * 100  # 100x100 area
    st.session_state.directions = np.random.rand(NUM_DRONES, 2) * 2 - 1  # random directions

def update_positions():
    # Move drones
    st.session_state.positions += st.session_state.directions * SPEED * 0.5

    # Keep drones inside bounds
    st.session_state.positions = np.clip(st.session_state.positions, 0, 100)

    # Detect and handle collisions
    for i in range(NUM_DRONES):
        for j in range(i + 1, NUM_DRONES):
            dist = np.linalg.norm(st.session_state.positions[i] - st.session_state.positions[j])
            if dist < COLLISION_DISTANCE:
                # Collision predicted — change direction (simple avoidance)
                st.session_state.directions[i] *= -1
                st.session_state.directions[j] *= -1
                st.session_state.positions[i] += st.session_state.directions[i] * 2
                st.session_state.positions[j] += st.session_state.directions[j] * 2

# Simulation
placeholder = st.empty()
st.sidebar.markdown("### 🧠 AI Collision Detection Running...")

run = st.sidebar.button("Start Simulation")
stop = st.sidebar.button("Stop")

if run:
    st.session_state.running = True
if stop:
    st.session_state.running = False

if "running" not in st.session_state:
    st.session_state.running = False

while st.session_state.running:
    update_positions()
    
    # Plot
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(st.session_state.positions[:, 0], st.session_state.positions[:, 1], color="skyblue", s=100, label="Drones")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.set_title("Live Drone Airspace Monitoring")
    ax.grid(True)
    
    # Show safe zones
    for i in range(NUM_DRONES):
        circle = plt.Circle(st.session_state.positions[i], COLLISION_DISTANCE, color='red', fill=False, linestyle='--', alpha=0.3)
        ax.add_patch(circle)
    
    placeholder.pyplot(fig)
    time.sleep(REFRESH)

st.success("✅ Simulation ready! Press **Start Simulation** in sidebar to begin.")
