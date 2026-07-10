
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

from signal_model import TrafficSignal

from traffic_logic import TrafficController
from database import (
    create_table,
    save_report,
    get_reports
)
# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Smart Traffic System",
    page_icon="🚦",
    layout="wide"
)
create_table()
# ---------------------------------------------------
# Session State Initialization
# ---------------------------------------------------
if "north_signal" not in st.session_state:
    st.session_state.north_signal = "🟢 Green"

if "south_signal" not in st.session_state:
    st.session_state.south_signal = "🔴 Red"

if "east_signal" not in st.session_state:
    st.session_state.east_signal = "🔴 Red"

if "west_signal" not in st.session_state:
    st.session_state.west_signal = "🔴 Red"

if "north" not in st.session_state:

    st.session_state.north = TrafficSignal(
        "North",
        25,
        40,
        "Green"
    )

if "south" not in st.session_state:

    st.session_state.south = TrafficSignal(
        "South",
        10,
        20,
        "Red"
    )

if "east" not in st.session_state:

    st.session_state.east = TrafficSignal(
        "East",
        18,
        20,
        "Red"
    )

if "west" not in st.session_state:

    st.session_state.west = TrafficSignal(
        "West",
        30,
        20,
        "Red"
    )

north = st.session_state.north
south = st.session_state.south
east = st.session_state.east
west = st.session_state.west

if "controller" not in st.session_state:

    st.session_state.controller = TrafficController(
        north,
        south,
        east,
        west
    )

controller = st.session_state.controller

if north.vehicles >= south.vehicles and \
   north.vehicles >= east.vehicles and \
   north.vehicles >= west.vehicles:

    busiest = "North"

elif south.vehicles >= north.vehicles and \
     south.vehicles >= east.vehicles and \
     south.vehicles >= west.vehicles:

    busiest = "South"

elif east.vehicles >= north.vehicles and \
     east.vehicles >= south.vehicles and \
     east.vehicles >= west.vehicles:

    busiest = "East"

else:
    busiest = "West"

# Traffic system running state
if "running" not in st.session_state:
    st.session_state.running = False

if "emergency_count" not in st.session_state:
    st.session_state.emergency_count = 0

# Timer
north_timer = 40
south_timer = 15
east_timer = 5
west_timer = 50

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("🚦 Smart Traffic Management System")
st.write("AI Based Traffic Signal Control Dashboard")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🚦 Traffic Control Panel")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Traffic Control",
        "Reports",
        "Settings"
    ]
)

# ===================================================
# Dashboard
# ===================================================

if menu == "Dashboard":

    st.header("🚦 Live Traffic Dashboard")

    import time

    if st.session_state.running:

        controller.countdown()

        time.sleep(1)

        st.rerun()
    

    st.markdown("---")

    title_col1, title_col2 = st.columns([3, 1])

    with title_col1:
        st.subheader("🚦 Smart Traffic Control Center")

    with title_col2:
        st.metric("Active Signal", north.direction)

    st.markdown("---")
   
    # ---------------- First Row ----------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⬆ North")

        st.metric(
            label="🚗 Vehicles",
            value=north.vehicles
        )
        if st.session_state.north_signal == "🟢 Green":
            # st.success(st.session_state.north_signal)
            if north.color == "Green":
                st.success("🟢 Green")
            elif north.color == "Yellow":
                st.warning("🟡 Yellow")
            else:
                st.error("🔴 Red")
        else:
            st.error(st.session_state.north_signal)

       
        st.write(
            f"Timer : {north.timer} sec"
        )

    with col2:
        st.subheader("⬇ South")
        st.metric(
            label="🚗 Vehicles",
            value=south.vehicles
        )

        if st.session_state.south_signal == "🟢 Green":
            # st.success(st.session_state.south_signal)
            if south.color == "Green":
                st.success("🟢 Green")
            elif south.color == "Yellow":
                st.warning("🟡 Yellow")
            else:
                st.error("🔴 Red")
        else:
            # st.error(st.session_state.south_signal)
            if south.color == "Green":
                st.success("🟢 Green")
            elif south.color == "Yellow":
                st.warning("🟡 Yellow")
            else:
                st.error("🔴 Red")

        st.write(f"Timer : {south.timer} sec")

    # ---------------- Second Row ----------------

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("➡ East")
        st.metric(
            label="🚗 Vehicles",
            value=east.vehicles
        )

        if st.session_state.east_signal == "🟢 Green":
            st.success(st.session_state.east_signal)
        else:
            
            if east.color == "Green":
                st.success("🟢 Green")
            elif east.color == "Yellow":
                st.warning("🟡 Yellow")
            else:
                st.error("🔴 Red")

        st.write(f"Timer : {east.timer} sec")

    with col4:
        st.subheader("⬅ West")
        st.metric(
            label="🚗 Vehicles",
            value=west.vehicles
        )

        if st.session_state.west_signal == "🟢 Green":
            st.success(st.session_state.west_signal)
        else:
            # st.error(st.session_state.west_signal)
            if west.color == "Green":
                st.success("🟢 Green")
            elif west.color == "Yellow":
                st.warning("🟡 Yellow")
            else:
                st.error("🔴 Red")

        st.write(f"Timer : {west.timer} sec")

    # ---------------------------------------------------
    # Manual Control
    # ---------------------------------------------------

    st.divider()

    st.subheader("Manual Signal Control")

    st.divider()

    st.subheader("🚦 Traffic Status")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
        "Current Signal",
        controller.get_current_signal().direction
        )
    

    with c2:
        active_timer = (
            north.timer if north.color == "Green"
            else south.timer if south.color == "Green"
            else east.timer if east.color == "Green"
            else west.timer
        )

        st.metric(
           "Remaining Time",
           f"{active_timer} sec"
        )

    with c3:
        st.metric(
           "Total Vehicles",
           north.vehicles +
           south.vehicles +
           east.vehicles +
           west.vehicles
        )
    

    if north.vehicles >= south.vehicles and \
       north.vehicles >= east.vehicles and \
       north.vehicles >= west.vehicles:

        busiest = "North"

    elif south.vehicles >= north.vehicles and \
         south.vehicles >= east.vehicles and \
         south.vehicles >= west.vehicles:

        busiest = "South"

    elif east.vehicles >= north.vehicles and \
         east.vehicles >= south.vehicles and \
         east.vehicles >= west.vehicles:

        busiest = "East"

    else:
        busiest = "West"

    st.info(
        f"🤖 AI Recommendation: Give Green Signal to {busiest}"
    )

    if busiest == "North":
        north.set_green()
        south.set_red()
        east.set_red()
        west.set_red()

        north.reset_timer(
            north.calculate_dynamic_timer()
        )

    elif busiest == "South":
        north.set_red()
        south.set_green()
        east.set_red()
        west.set_red()

        south.reset_timer(
            south.calculate_dynamic_timer()
        )

    elif busiest == "East":
        north.set_red()
        south.set_red()
        east.set_green()
        west.set_red()

        east.reset_timer(
        east.calculate_dynamic_timer()
        )

    else:
        north.set_red()
        south.set_red()
        east.set_red()
        west.set_green()

        west.reset_timer(
            west.calculate_dynamic_timer()
        )

    

    st.divider()

    # start, stop, auto, reset = st.columns(4)
    start, stop, auto, emergency, reset = st.columns(5)

    with start:
        if st.button("▶ Start"):
            st.session_state.running = True
        

    with stop:
        if st.button("⏸ Stop"):
            st.session_state.running = False
        

    with auto:
        if st.button("🤖 Auto Detect"):
            north.vehicles = random.randint(5, 60)
            south.vehicles = random.randint(5, 60)
            east.vehicles = random.randint(5, 60)
            west.vehicles = random.randint(5, 60)

            st.rerun()

    with emergency:

        emergency_direction = st.selectbox(
            "Emergency Road",
            [
                "North",
                "South",
                "East",
                "West"
            ]
        )

        if st.button("🚑 Emergency"):

            st.session_state.emergency_count += 1

            save_report(
                emergency_direction,
                (
                    north.vehicles if emergency_direction == "North"
                    else south.vehicles if emergency_direction == "South"
                    else east.vehicles if emergency_direction == "East"
                    else west.vehicles
                ),
                1
            )

            north.set_red()
            south.set_red()
            east.set_red()
            west.set_red()

            if emergency_direction == "North":
                north.set_green()
                north.reset_timer(60)

            elif emergency_direction == "South":
                south.set_green()
                south.reset_timer(60)

            elif emergency_direction == "East":
                east.set_green()
                east.reset_timer(60)

            else:
                west.set_green()
                west.reset_timer(60)

            st.rerun()
    
   
   

    with reset:
        st.button("🔄 Reset")




    b1, b2, b3, b4 = st.columns(4)

    with b1:
        if st.button("North Green"):
            north.set_green()
            south.set_red()
            east.set_red()
            west.set_red()

            north.reset_timer(40)
            south.reset_timer(20)
            east.reset_timer(20)
            west.reset_timer(20)

            st.rerun()

    with b2:
        if st.button("South Green"):
            north.set_red()
            south.set_green()
            east.set_red()
            west.set_red()

            north.reset_timer(20)
            south.reset_timer(40)
            east.reset_timer(20)
            west.reset_timer(20)

            st.rerun()

    with b3:
        if st.button("East Green"):
            north.set_red()
            south.set_red()
            east.set_green()
            west.set_red()

            north.reset_timer(20)
            south.reset_timer(20)
            east.reset_timer(40)
            west.reset_timer(20)

            st.rerun()

    with b4:
        if st.button("West Green"):
            north.set_red()
            south.set_red()
            east.set_red()
            west.set_green()

            north.reset_timer(20)
            south.reset_timer(20)
            east.reset_timer(20)
            west.reset_timer(40)

            st.rerun()

    
elif menu == "Traffic Control":
    st.header("Traffic Control")
    st.info("Coming in Phase 2")


elif menu == "Reports":

    st.header("📊 Traffic Reports")

    total_vehicles = (
        north.vehicles +
        south.vehicles +
        east.vehicles +
        west.vehicles
    )

    st.metric(
        "🚗 Total Vehicles",
        total_vehicles
    )

    st.metric(
        "🚦 Current Green Signal",
        controller.get_current_signal().direction
    )

    st.metric(
        "🔥 Most Congested Road",
        busiest
    )

    st.metric(
        "🚑 Emergency Events",
        st.session_state.emergency_count
    )
    average_wait = (
        north.timer +
        south.timer +
        east.timer +
        west.timer
    ) / 4

    st.metric(
        "⏱ Average Waiting Time",
        f"{average_wait:.1f} sec"
    )

  

    st.divider()

    st.subheader("🗄 Stored Database Records")

    reports = get_reports()

    df = pd.DataFrame(
        reports,
        columns=[
            "ID",
            "Direction",
            "Vehicles",
            "Emergency"
        ]
    )

    df["Emergency"] = df["Emergency"].replace(
        {
            0: "No",
            1: "Yes"
        }
    )

    st.dataframe(df)

    st.divider()

    st.subheader("📊 Vehicle Count by Direction")

    directions = [
        "North",
        "South",
        "East",
        "West"
    ]

    vehicle_counts = [
        north.vehicles,
        south.vehicles,
        east.vehicles,
        west.vehicles
    ]

    fig, ax = plt.subplots()

    ax.bar(
        directions,
        vehicle_counts
    )

    ax.set_xlabel("Direction")
    ax.set_ylabel("Vehicles")
    ax.set_title("Vehicle Count by Direction")

    st.pyplot(fig)

    st.divider()

    st.subheader("🚑 Emergency Analytics")

    labels = [
        "Emergency",
        "Normal"
    ]

    values = [
        st.session_state.emergency_count,
        len(reports) - st.session_state.emergency_count
    ]

    fig2, ax2 = plt.subplots()

    ax2.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax2.set_title("Emergency vs Normal Traffic")

    st.pyplot(fig2)


    


elif menu == "Settings":
    st.header("Settings")
    st.info("Coming in Phase 2")


