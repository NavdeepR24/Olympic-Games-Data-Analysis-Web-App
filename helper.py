import numpy as np

#for medal tally
def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(
        subset=['Team','NOC','Year','City','Sport','Event','Medal']
    )
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    elif year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    elif year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    else:
        temp_df = medal_df[
            (medal_df['Year'] == int(year)) &
            (medal_df['region'] == country)
        ]
    if flag == 1:
        x = temp_df.groupby('Year').sum()[
            ['Gold','Silver','Bronze']
        ].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[
            ['Gold','Silver','Bronze']
        ].sort_values('Gold', ascending=False).reset_index()
    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x

#overall analysis
def data_over_time(df, col):
    nations_over_time=(
        df.drop_duplicates(['Year', col])
        .groupby('Year')[col].count()
        .reset_index()
        .rename(columns={col: col+'s'})
    )
    return nations_over_time

def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    return (temp_df['Name']
            .value_counts()
            .reset_index()
            .head(15)
            .merge(df[['Name','Sport','region']].drop_duplicates(),
                   on='Name', how='left')
            .rename(columns={'count': 'Medals'}))

#country wise analysis
def yearwise_medal_tally(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(
        subset=['Team','NOC','Year','City','Sport','Event','Medal']
    )
    new_df = temp_df[temp_df['region'] == country]
    return new_df.groupby('Year').count()['Medal'].reset_index()

def country_event_heatmap(df, country):
    temp_df = df.drop_duplicates(
        subset=['Team','NOC','Year','City','Sport','Event','Medal']
    )
    new_df = temp_df[temp_df['region'] == country]
    return new_df.pivot_table(
        index='Sport', columns='Year',
        values='Medal', aggfunc='count'
    ).fillna(0)

def most_successful_country_wise(df, country):
    temp_df = df[df['region'] == country]
    return (temp_df['Name']
            .value_counts()
            .reset_index()
            .head(10)
            .merge(df[['Name','Sport']].drop_duplicates(),
                   on='Name', how='left')
            .rename(columns={'count': 'Medals'}))

#athlete wise analysis
def weight_v_height(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'Sport'])
    if sport != 'Overall':
        athlete_df = athlete_df[athlete_df['Sport'] == sport]
    return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name','Year','Sex'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year')['Name'].count().reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year')['Name'].count().reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x':'Male','Name_y':'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final

