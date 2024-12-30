# © 2024 Srikar Kalle
# Author: Srikar Kalle  
# Student ID: C00313529  
# Date: December 13, 2024  
# Project: Earthquake Insights Analysis

from shiny import App, ui, render 
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

if not os.path.exists("plots"):
    os.makedirs("plots")

df = pd.read_csv('quakes-cleaned.csv')
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df['hour'] = df['time'].dt.hour
df['date'] = df['time'].dt.date

regionCounts = df['place'].value_counts().head(25)
largestEarthquake = df.loc[df['mag'].idxmax()]

timeOfDay = pd.cut(
    df['hour'],
    bins=[0, 6, 12, 18, 24],
    labels=['Night', 'Morning', 'Afternoon', 'Evening']
)
timeCounts = timeOfDay.value_counts()

dailyCounts = df.groupby('date').size().reset_index(name='count')

regionMag = (
    df.groupby('place')['mag']
    .mean()
    .sort_values(ascending=False)
    .head(35)
    .reset_index()
)

coordinates = df[['place', 'latitude', 'longitude']].drop_duplicates(subset='place')
regionMag = regionMag.merge(coordinates, on='place', how='left')

def save_plot(fig, filename):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"plots/{filename}_{timestamp}.jpeg"
        fig.write_image(filepath)
        return filepath
    except Exception as e:
        print(f"Error saving plot {filename}: {e}")
        return None

app_ui = ui.page_fluid(
    ui.h2("Earthquake Insights Dashboard by Srikar Kalle (C00313529)"),
    ui.navset_tab(
        ui.nav_panel("Top 25 Regions with Most Seismic Activity",
                     ui.row(
                         ui.column(6, ui.output_image("plot1")),
                         ui.column(6, ui.p("This plot shows the top 25 regions with the highest frequency of seismic activity. "
                                          "The color scale represents the intensity of seismic events, with darker colors indicating higher frequencies. "
                                          "Regions with more frequent earthquakes are displayed at the top, helping to identify earthquake-prone areas."))
                     )),
        ui.nav_panel("Earthquake Activity by Time of Day",
                     ui.row(
                         ui.column(6, ui.output_image("plot2")),
                         ui.column(6, ui.p("This chart illustrates earthquake occurrences based on different times of the day. "
                                          "The data is categorized into four segments: Night, Morning, Afternoon, and Evening. "
                                          "It helps to uncover if there are patterns related to the time of day when earthquakes are most likely to occur."))
                     )),
        ui.nav_panel("Daily Earthquake Activity",
                     ui.row(
                         ui.column(6, ui.output_image("plot3")),
                         ui.column(6, ui.p("This line chart shows the daily frequency of earthquakes, allowing you to track trends over time. "
                                          "By examining the fluctuations in daily seismic activity, we can identify periods of unusual or heightened activity."))
                     )),
        ui.nav_panel("Top 35 Regions by Average Magnitude",
                     ui.row(
                         ui.column(6, ui.output_image("plot4")),
                         ui.column(6, ui.p("This scatter plot displays the top 35 regions based on the average earthquake magnitude. "
                                          "The size of each marker reflects the magnitude of the earthquakes, while the color intensity indicates the magnitude's level. "
                                          "This plot is helpful for identifying regions where strong earthquakes are most frequent."))
                     )),
        ui.nav_panel("Earthquake Activity Heatmap (by Week)",
                     ui.row(
                         ui.column(6, ui.output_image("plot5")),
                         ui.column(6, ui.p("This heatmap provides a visual representation of earthquake occurrences by week. "
                                          "Each cell shows the number of earthquakes occurring during that week, with colors representing intensity. "
                                          "It offers a quick overview of seismic activity patterns over the weeks."))
                     )),
    )
)

def server(input, output, session):
    @output
    @render.image
    def plot1():
        fig = px.bar(regionCounts, 
                     x=regionCounts.index, 
                     y=regionCounts.values,  
                     title="Top 25 Regions with Most Seismic Activity", 
                     labels={"x": "Region", "y": "Frequency"},
                     color=regionCounts.values,
                     color_continuous_scale=["#E6E6FA", "#D3D3D3", "#9370DB", "#8A2BE2", "#4B0082"])
        fig.update_layout(plot_bgcolor="#f0f0f0", paper_bgcolor="#ffffff")
        image_path = save_plot(fig, "top_25_regions")
        return {"src": image_path, "alt": "Top 25 Regions with Most Seismic Activity"} if image_path else {"src": "", "alt": "Error"}

    @output
    @render.image
    def plot2():
        fig = px.bar(timeCounts, x=timeCounts.index, y=timeCounts.values, title="Earthquake Activity by Time of Day",
                     color=timeCounts.index,
                     color_discrete_sequence=["#FF9933", "#FFFFFF", "#138808", "#000080"])
        fig.update_layout(plot_bgcolor="#f0f0f0", paper_bgcolor="#ffffff")
        image_path = save_plot(fig, "time_of_day")
        return {"src": image_path, "alt": "Earthquake Activity by Time of Day"} if image_path else {"src": "", "alt": "Error"}

    @output
    @render.image
    def plot3():
        fig = px.line(
            dailyCounts,
            x='date',
            y='count',
            title="Daily Earthquake Activity",
            labels={"date": "Date", "count": "Frequency"},
            line_shape='spline',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(
            title_x=0.5,
            autosize=True,
            plot_bgcolor="#f7f5e6",
            paper_bgcolor="#ffffff",
        )
        image_path = save_plot(fig, "daily_activity")
        return {"src": image_path, "alt": "Daily Earthquake Activity"} if image_path else {"src": "", "alt": "Error"}

    @output
    @render.image
    def plot4():
        fig = px.scatter_geo(
            regionMag,
            lat='latitude',
            lon='longitude',
            size='mag',
            color='mag',
            hover_name='place',
            title="Top 35 Regions by Average Earthquake Magnitude",
            color_continuous_scale="Plasma",
            labels={"mag": "Average Magnitude"}
        )
        fig.update_layout(
            title_x=0.5,
            width=1000,
            height=600,
            plot_bgcolor="#f1f1f1",
            paper_bgcolor="#ffffff",
        )
        image_path = save_plot(fig, "average_magnitude")
        return {"src": image_path, "alt": "Top 35 Regions by Average Magnitude"} if image_path else {"src": "", "alt": "Error"}

    @output
    @render.image
    def plot5():
        df['time'] = pd.to_datetime(df['time'], errors='coerce')
        df['date'] = df['time'].dt.date
        daily_activity = df['date'].value_counts().sort_index()

        daily_activity.index = pd.to_datetime(daily_activity.index)
        daily_activity = daily_activity.reset_index()
        daily_activity.columns = ['date', 'count']

        daily_activity['week'] = daily_activity['date'].dt.isocalendar().week

        heatmap_data = daily_activity.pivot_table(index='week', columns=daily_activity['date'].dt.day, values='count', aggfunc='sum')

        fig = px.imshow(
            heatmap_data,
            title="Earthquake Activity Heatmap (by Week)",
            labels={'x': 'Day of Month', 'y': 'Week Number'},
            color_continuous_scale='Viridis'
        )

        fig.update_layout(title_x=0.5, width=1000, height=600)
        image_path = save_plot(fig, "earthquake_heatmap")
        return {"src": image_path, "alt": "Earthquake Activity Heatmap (by Week)"} if image_path else {"src": "", "alt": "Error"}

app = App(app_ui, server)
