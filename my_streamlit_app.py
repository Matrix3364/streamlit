import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')
st.write('I enjoy to discover stremalit possibilities')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

#st.line_chart(df_weather['MAX_TEMPERATURE_C'])

#import seaborn as sns
#viz_correlation = sns.heatmap(df_weather.corr(numeric_only=True), 
#								center=0,
#								cmap = sns.color_palette("vlag", as_cmap=True)
#								)

#st.pyplot(viz_correlation.figure)

#import streamlit as st

#st.title('Hello Wilders, welcome to my application!')
#name = st.text_input("Please give me your name :")
#name_length = len(name)
#st.write("Your name has ",name_length,"characters")

import seaborn as sns
import matplotlib.pyplot as plt


#fig, ax = plt.subplots(figsize = (10,5))
##selection_continent = st.multiselect('Sélectionnez les continents', df_cars['continent'].unique())

plt.title("corrélation entre hp et mpg")
viz_scatter= sns.scatterplot(x = df_cars["hp"],
                                 y = df_cars["mpg"],
                                 hue = df_cars["continent"])

st.pyplot(viz_scatter.figure, clear_figure=True)

plt.title("distribution du weightlbs par région")
viz_boxplot = sns.boxplot(df_cars, x="weightlbs",
                        hue = "continent")
                              
st.pyplot(viz_boxplot.figure)



