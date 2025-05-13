# region_locator.py

import streamlit as st
import pandas as pd
import folium
import pickle
import numpy as np
from streamlit_folium import st_folium

# Load Pickle File
with open('healthcare_facilities_clustered_kmeans_4.pkl', 'rb') as f:
    df = pickle.load(f)

# Streamlit UI
st.title('🗺️ Region Locator by Coordinates')

# Input fields with proper precision and validation
latitude = st.number_input('📍 Enter Latitude:', min_value=-90.0, max_value=90.0, format="%.6f", step=0.000001)
longitude = st.number_input('📍 Enter Longitude:', min_value=-180.0, max_value=180.0, format="%.6f", step=0.000001)

if st.button("Find Region"):
    if latitude != 0.0 or longitude != 0.0:
        try:
            # Compute distances
            df['distance'] = np.sqrt((df['LATITUDE'] - latitude)**2 + (df['LONGITUDE'] - longitude)**2)
            nearest = df.loc[df['distance'].idxmin()]
            min_distance = nearest['distance']

            # Define threshold (adjust if needed, e.g., ~1 degree = ~111 km)
            distance_threshold = 0.5  

            if min_distance > distance_threshold:
                st.warning("🚫 Location not in specified regions.")
            else:
                region = nearest['Region_Name_KMeans']
                st.success(f'✅ Nearest Region: **{region}**')

                # Show map
                m = folium.Map(location=[latitude, longitude], zoom_start=7)
                folium.Marker(
                    [latitude, longitude],
                    tooltip=f"Entered Location: {region}",
                    popup=region,
                    icon=folium.Icon(color='blue', icon='info-sign')
                ).add_to(m)
                st_folium(m, width=700, height=500)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter valid (non-zero) coordinates.")
