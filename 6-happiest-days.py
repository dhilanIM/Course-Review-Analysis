import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

reviews_df = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])

# Happiest day
reviews_df["Weekday"] = reviews_df["Timestamp"].dt.strftime("%A")
reviews_df["Daynumber"] = reviews_df["Timestamp"].dt.strftime("%w")

happy = reviews_df.groupby(["Weekday","Daynumber"]).mean(numeric_only=True)
happy = happy.sort_values("Daynumber")



chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Aggregated Average Ratings by Day of the Week',
        align: 'center'
    },
    subtitle: {
        text: '',
        align: 'left'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day of the week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""
def app():
    wp = jp.QuasarPage()  # Web page object
    
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(happy.index.get_level_values(0))
    hc.options.series[0].data = list(happy["Rating"])    
    return wp

jp.justpy(app)