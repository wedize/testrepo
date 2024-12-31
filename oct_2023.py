import pandas as pd
from datetime import datetime, timedelta

# Set the start date and time
start_date = datetime(2023, 10, 1, 0, 0, 0)

# Generate timestamps for the entire month of October 2023
timestamps = [start_date + timedelta(hours=i) for i in range(24 * 31)]

# Format the timestamps as strings in the desired format
formatted_timestamps = [timestamp.strftime("%m/%d/%y %H:%M") + ";0;0;0;0;0;0" for timestamp in timestamps]

# Create a DataFrame with the timestamps
df = pd.DataFrame({"Timestamp": formatted_timestamps})

# Save the DataFrame to a CSV file
df.to_csv("october_timestamps.csv", index=False)
