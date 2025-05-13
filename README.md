# Health-care-region-locator

Health-care-region-locator
A location-enabled healthcare web application developed using Streamlit that tracks and stores user locations, processes the data, and visualizes it for potential healthcare analysis. The project uses Python’s pickle module to serialize and save data locally, ensuring efficient reloading during runtime.

How It Works

The different set of healthcare locations are used which are in California.
Then they are divided into four regions by using K-means Clustering.
This clustered data is stored in a .pkl file.
A simple user interface is created so that they can give the loaction input and get the region of that location.
