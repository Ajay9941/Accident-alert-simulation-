import streamlit as st
import random
import time
import datetime
import pandas as pd

st.set_page_config(page_title="ResQ.AI - Accident Detection Demo", layout="centered")

# ---- 1. Header ----
st.title("🚨 ResQ.AI - Accident Detection & Hospital Alert System")
st.subheader("Simulating a real-time emergency response AI agent")

# ---- 2. Simulated Accident Trigger ----
st.markdown("### 🚗 Simulate Accident")
trigger = st.button("Trigger Accident")

# ---- Vehicle Number Generator ----
def generate_vehicle_number():
    state_code = "TN"
    district_code = random.randint(1, 99)
    series = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    number = random.randint(1000, 9999)
    return f"{state_code}-{district_code:02d}-{series}-{number}"

if trigger:
    with st.spinner("🚨 Detecting accident..."):
        time.sleep(1.5)

    # ---- 3. Randomly Generate Geo-Location, Severity, and Vehicle ----
    location = {
        "latitude": round(random.uniform(12.90, 13.10), 5),
        "longitude": round(random.uniform(80.20, 80.30), 5)
    }
    severity_level = random.choice(["Low", "Medium", "High"])
    vehicle_number = generate_vehicle_number()

    # ---- 4. Display Accident Info ----
    st.success("✅ Accident Detected!")
    st.write(f"*🕒 Time:* {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(f"*📍 Location:* Lat {location['latitude']} | Long {location['longitude']}")
    st.write(f"*🚗 Vehicle Number:* {vehicle_number}")
    st.write(f"*⚠️ Severity:* {severity_level}")

    # ---- 5. Optional Voice Verification Placeholder ----
    st.markdown("### 🗣️ Voice Verification (Simulated)")
    if severity_level == "High":
        st.warning("Driver unresponsive. Marking case as CRITICAL.")
    else:
        st.info("Driver confirmed responsive. Proceed with caution.")

    # ---- 6. Hospital Alert Simulation ----
    st.markdown("### 🏥 Alert Sent To:")
    hospitals = ["Apollo Hospitals", "MIOT International", "Fortis Malar", "SRMC Emergency"]
    selected_hospital = random.choice(hospitals)
    st.success(f"📨 Alert sent to *{selected_hospital}* with real-time accident details.")

    # ---- 7. Dashboard Log ----
    st.markdown("### 📊 Incident Dashboard")
    incident_data = pd.DataFrame({
        "Time": [datetime.datetime.now().strftime('%H:%M:%S')],
        "Vehicle Number": [vehicle_number],
        "Location": [f"{location['latitude']}, {location['longitude']}"],
        "Severity": [severity_level],
        "Hospital Notified": [selected_hospital]
    })
    st.dataframe(incident_data)

else:
    st.info("Click the button above to simulate an accident.")
