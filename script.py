import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Cars Datasets 2025.csv',encoding='latin1')


df.fillna(0,inplace=True)

df.rename(columns={
    'Performance(0 - 100 )KM/H' : 'Acceleration'
},inplace=True)




df['Cars Prices'] = df['Cars Prices'].str.replace('$' , '' , regex=False).str.replace(',','',regex=False).str.strip()

df['Cars Prices'] = df['Cars Prices'].str.extract(r'(\d+)')
df['Cars Prices'] = pd.to_numeric(df['Cars Prices'].squeeze(),errors='coerce')



df['CC/Battery Capacity'] = df['CC/Battery Capacity'].str.replace('cc' , '', regex=False).str.replace(',','',regex=False).str.replace('kwh','',regex=False).str.strip()

df['CC/Battery Capacity'] = df['CC/Battery Capacity'].str.extract(r'(/d+)').astype(float)


df['HorsePower'] = df['HorsePower'].str.replace('hp','',regex=False).str.strip()
df['HorsePower'] = df['HorsePower'].str.extract(r'(\d+)').astype(int)



df['Torque'] = df['Torque'].str.replace('Nm','',regex=False).str.replace(',','',regex=False).str.strip()

df['Torque'] = df['Torque'].str.extract(r'(\d+)').astype(float)

df['Acceleration'] = df['Acceleration'].str.replace('sec','',regex=False).str.replace(' ','',regex=False).str.strip()
df['Acceleration'] = df['Acceleration'].str.extract(r'(\d+)').astype(float)


average_car_price_per_fuel_type = df.groupby('Fuel Types')['Cars Prices'].mean()

company_wise_average_horse_power = df.groupby('Company Names')['HorsePower'].mean().head(10)

top_5_fastest_cars_df = df.sort_values(by='Acceleration',ascending=True).head(5)
top_5_fastest_cars_names = top_5_fastest_cars_df['Cars Names']
top_5_fastest_cars_speed = top_5_fastest_cars_df['Acceleration']


numerical_columns = ['Acceleration','Cars Prices','CC/Battery Capacity','HorsePower','Torque']
df_numerical = df[numerical_columns]

correlation = df_numerical.corr()


print('Average car price per fuel type:-',average_car_price_per_fuel_type)
print('Company wise average horse power:-',company_wise_average_horse_power)
print('Top 5 fastest cars:-',top_5_fastest_cars_names)
print('Top 5 fastest cars df:-',top_5_fastest_cars_df)
print("Dataframe Final :-",df.head())

df.to_csv('Cars Dataset-Cleaned-Visualized.csv',index=False)

#Visualization
plt.figure()
sns.histplot(data=df,x='Cars Prices',bins=10,kde=True)



plt.figure()
sns.scatterplot(data=df,x='HorsePower',y='Cars Prices',palette='deep')

plt.figure()
sns.scatterplot(data=df,x='Acceleration',y='Cars Prices',palette='muted')
plt.title('Acceleration vs Cars Prices')


plt.figure()
sns.barplot(x=average_car_price_per_fuel_type.values,y=average_car_price_per_fuel_type.index,palette='viridis')
plt.title('Average car price vs fuel type')
plt.savefig('screenshots/Average car price v fuel type.png')

plt.figure()
sns.barplot(x=company_wise_average_horse_power.values,y=company_wise_average_horse_power.index,palette='deep')
plt.title('Company wise average horse power (10)')
plt.savefig('screenshots/company wise average horse power (10).png')

plt.figure()
sns.barplot(x=top_5_fastest_cars_speed,y=top_5_fastest_cars_names,palette='rainbow')
plt.title('Top 5 Fastest Cars')
plt.savefig('screenshots/top 5 fastest cars.png')

plt.figure()
sns.heatmap(correlation,annot=True)
plt.title('Numerical Columns Correlations')
plt.savefig('screenshots/numerical columns correlation.png')


plt.show()