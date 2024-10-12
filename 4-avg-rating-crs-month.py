import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

reviews_df = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])

# Getting average per month per course
reviews_df["Month"] = reviews_df["Timestamp"].dt.strftime("%Y-%m")
month_avg_crs = reviews_df.groupby(['Month', 'Course Name'])["Rating"].mean(numeric_only=True).unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Month by Course',
        align: 'center'
    },
    subtitle: {
        text: '',
        align: 'left'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'bot',
        x: 120,
        y: 170,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        // Highlight the last years where moose hunting quickly deminishes
        title: {
            text: 'Year'
        },
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766,
                29278,
                27487,
                26007
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048,
                52804,
                49317,
                52490
            ]
    }]
}
"""

def app():
    wp = jp.QuasarPage()  # Web page object
    
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_avg_crs.index)
    
    hc_data = [{"name":v1, "data":[v2 for v2 in month_avg_crs[v1]]} for v1 in month_avg_crs.columns]
    hc.options.series = hc_data
    return wp

jp.justpy(app)