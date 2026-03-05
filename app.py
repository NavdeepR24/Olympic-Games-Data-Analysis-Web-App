import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import preprocess, helper

#load data
df=pd.read_csv('data/athlete_events.csv')
region_df=pd.read_csv('data/noc_regions.csv')
df=preprocess.preprocess(df, region_df)

# Sidebar
st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/5/5c/Olympic_rings_without_rims.svg')
st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio('Select an Option', [
    'Medal Tally',
    'Overall Analysis',
    'Country-wise Analysis',
    'Athlete-wise Analysis'
])

#medal tally
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years = ['Overall'] + sorted(df['Year'].unique().tolist())
    countries = ['Overall'] + sorted(df['region'].dropna().unique().tolist())

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", countries)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    st.title(f"Medal Tally — {selected_year} | {selected_country}")
    st.dataframe(medal_tally)