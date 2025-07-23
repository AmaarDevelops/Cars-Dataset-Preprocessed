🚗 Cars Dataset Analysis and Visualization (2025)
This project involves cleaning, analyzing, and visualizing a dataset of various car models and their specifications. It offers valuable insights into car prices, performance metrics like acceleration, horsepower, and torque, categorized by fuel types and companies.

📁 Dataset Used
File Name: Cars Datasets 2025.csv

Source: Custom/Provided CSV dataset with car specifications such as price, acceleration, horsepower, torque, fuel type, and more.

🛠️ Features and Workflow
1. Data Cleaning
   
Removed special characters ($, ,, cc, hp, Nm, kWh, etc.)
Converted strings to numeric types
Filled missing values with 0
Renamed columns for clarity (Performance(0 - 100 )KM/H → Acceleration)

3. Feature Engineering

Extracted and converted:
Car Prices from string to numeric
Horsepower, Torque, and Battery/CC into usable numerical formats
Acceleration cleaned and transformed

3. Statistical Analysis

Calculated:
Average car price by fuel type
Average horsepower by company
Top 5 fastest cars by acceleration

5. Visualizations
Generated multiple insightful visualizations using matplotlib and seaborn, including:
Histogram of car prices
Horsepower vs Car Prices (scatter plot)
Acceleration vs Car Prices (scatter plot)
Average car price per fuel type (bar chart)
Top 10 companies by average horsepower (bar chart)
Top 5 fastest cars (bar chart)

🧠 Heatmap showing correlation between numerical features
All plots are saved under the screenshots/ directory.

📂 Output
Cars Dataset-Cleaned-Visualized.csv: Cleaned and processed version of the original dataset.

📁 Screenshots Folder:
Average car price v fuel type.png
company wise average horse power (10).png
top 5 fastest cars.png
numerical columns correlation.png

🧰 Tech Stack
Python
Pandas
NumPy
Matplotlib
Seaborn

💡 Key Insights
Fuel Type Matters: Average car price varies significantly across fuel types.
Speed ≠ Cost: Some of the fastest cars aren’t always the most expensive.
Correlation Analysis: Positive correlation between horsepower, torque, and price.

Author :- [Amaar Ali]
