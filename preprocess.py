import pandas as pd
import warnings

def preprocess(df, regions):
    #to ignore warning
    warnings.filterwarnings('ignore')
    #merge with region data
    df=df.merge(regions, on='NOC', how='left')

    df=df.rename(columns={'notes': 'Notes'})

    df=df.drop('Games', axis=1)

    #fixing missing regions manually
    df.loc[df['NOC']=='SGP', 'region']='Singapore'
    df.loc[df['NOC'] == 'ROT', 'region'] = 'Refugee Olympic Team'
    df.loc[df['NOC'] == 'UNK', 'region'] = 'Unknown'
    df.loc[df['NOC'] == 'TUV', 'region'] = 'Tuvalu'

    #fixing data types
    df['Year']=df['Year'].astype(int)

    #droping duplicate values
    df=df.drop_duplicates()

    #filling missing values with median per sport
    df['Age']=pd.to_numeric(df['Age'], errors='coerce')
    df['Age']=df.groupby('Sport')['Age'].transform(lambda x: x.fillna(x.median()))

    #same for height and weight
    for col in ['Height', 'Weight']:
        df[col]=pd.to_numeric(df[col], errors='coerce')
        df[col]=df.groupby(['Sport', 'Sex'])[col].transform(lambda x: x.fillna(x.median()))

        #grouping by only sport
        df[col] = df.groupby('Sport')[col].transform(lambda x: x.fillna(x.median()))

        #filling remaining NaN with global median
        df[col].fillna(df[col].median())

    #to remove remaining missing values
    df=df.dropna(subset=['Height','Weight'])

    #filling NaN value with 'No Medal' in medal column
    df=df.fillna('No Medal')

    #one hot encoding
    #only create columns for actual medal
    df['Gold']=(df['Medal']=='Gold').astype(int)
    df['Silver']=(df['Medal']=='Silver').astype(int)
    df['Bronze']=(df['Medal']=='Bronze').astype(int)

    #adding a 'total_medal' helping column
    df['total_medal']=df['Gold']+df['Silver']+df['Bronze']

    #adding an 'Edition' column useful for dropdown columns
    df['Edition']=df['Year'].astype(str)+' '+df['Season']

    #sorting dataframe based on year
    df=df.sort_values('Year')
    df=df.reset_index(drop=True)

    return df