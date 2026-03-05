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

#overall analysis
elif user_menu == 'Overall Analysis':
    editions = df[df['Year'] != 1906]['Year'].nunique()
    cities    = df['City'].nunique()
    sports    = df['Sport'].nunique()
    events    = df['Event'].nunique()
    athletes  = df['Name'].nunique()
    nations   = df['region'].nunique()

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Editions", editions)
    with col2: st.metric("Hosts",    cities)
    with col3: st.metric("Sports",   sports)
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Events",   events)
    with col2: st.metric("Nations",  nations)
    with col3: st.metric("Athletes", athletes)

    # Line charts
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x='Year', y='regions',
                  title='Participating Nations over the Years')
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Year', y='Events',
                  title='Events over the Years')
    st.plotly_chart(fig)

    # Heatmap — no. of events per sport per year
    st.subheader("No. of Events over time (Every Sport)")
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year','Sport','Event'])
    pivot = x.pivot_table(index='Sport', columns='Year',
                          values='Event', aggfunc='count').fillna(0)
    sns.heatmap(pivot.astype(int), ax=ax)
    st.pyplot(fig)

    # Most successful athletes
    st.subheader("Most Successful Athletes")
    sport_list = ['Overall'] + sorted(df['Sport'].unique().tolist())
    selected_sport = st.selectbox("Select a Sport", sport_list)
    x = helper.most_successful(df, selected_sport)
    st.dataframe(x)

#contry wise analysis
elif user_menu == 'Country-wise Analysis':
    country_list = sorted(df['region'].dropna().unique().tolist())
    selected_country = st.sidebar.selectbox("Select a Country", country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x='Year', y='Medal',
                  title=f"{selected_country} Medal Tally over the Years")
    st.plotly_chart(fig)

    st.subheader(f"{selected_country} excels in the following sports")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20,20))
    sns.heatmap(pt, ax=ax)
    st.pyplot(fig)

    st.subheader(f"Top 10 Athletes of {selected_country}")
    top10_df = helper.most_successful_country_wise(df, selected_country)
    st.dataframe(top10_df)

#athlete wise analysis
elif user_menu == 'Athlete-wise Analysis':

    # Men vs Women participation
    st.title("Men vs Women Participation over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    st.plotly_chart(fig)

    # Age distribution
    athlete_df = df.drop_duplicates(subset=['Name','region'])
    fig, ax = plt.subplots(figsize=(10,5))
    age_data = [
        athlete_df['Age'].dropna(),
        athlete_df[athlete_df['Medal']=='Gold']['Age'].dropna(),
        athlete_df[athlete_df['Medal']=='Silver']['Age'].dropna(),
        athlete_df[athlete_df['Medal']=='Bronze']['Age'].dropna(),
    ]
    labels = ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist']
    for d, l in zip(age_data, labels):
        ax.hist(d, bins=20, alpha=0.5, label=l)
    ax.legend()
    st.title("Distribution of Age")
    st.pyplot(fig)

    # Height vs Weight scatter
    st.title("Height vs Weight")
    sport_list = ['Overall'] + sorted(df['Sport'].unique().tolist())
    selected_sport = st.selectbox("Select a Sport", sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)
    fig = px.scatter(temp_df, x='Weight', y='Height',
                     color='Medal', symbol='Sex',
                     hover_name='Name', opacity=0.5)
    st.plotly_chart(fig)
