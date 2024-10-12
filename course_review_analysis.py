import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

reviews_df = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])

# Getting average per day
reviews_df["Day"] = reviews_df["Timestamp"].dt.date
day_avg = reviews_df.groupby(["Day"]).mean(numeric_only=True)

# Ploting days vs avg
plt.figure(figsize=(15,3))
plt.plot(day_avg.index, day_avg["Rating"])
plt.show()

# Getting average per week
reviews_df["Week"] = reviews_df["Timestamp"].dt.strftime("%Y-%U")
week_avg = reviews_df.groupby(["Week"]).mean(numeric_only=True)

# Ploting weeks vs avg
plt.figure(figsize=(15,3))
plt.plot(week_avg.index, week_avg["Rating"])
plt.show()

# Getting average per month
reviews_df["Month"] = reviews_df["Timestamp"].dt.strftime("%Y-%m")
month_avg = reviews_df.groupby(["Month"]).mean(numeric_only=True)

# Ploting months vs avg
plt.figure(figsize=(15,3))
plt.plot(month_avg.index, month_avg["Rating"])
plt.show()

# Getting average per month per course
month_avg_crs = reviews_df.groupby(['Month', 'Course Name'])["Rating"].mean(numeric_only=True).unstack()
month_avg_crs.plot(figsize=(15,3))

# Happiest day
reviews_df["Weekday"] = reviews_df["Timestamp"].dt.strftime("%A")
reviews_df["Daynumber"] = reviews_df["Timestamp"].dt.strftime("%w")

happy = reviews_df.groupby(["Weekday","Daynumber"]).mean(numeric_only=True)
happy = happy.sort_values("Daynumber")

plt.figure(figsize=(15,3))
plt.plot(happy.index.get_level_values(0), happy["Rating"])
plt.show()

# Pie chart: Number of rating  by course
pie_df = reviews_df.groupby(["Course Name"]).count()
plt.pie(pie_df,labels=pie_df.index)