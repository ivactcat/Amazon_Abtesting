import pandas as pd 

def eda_preli (df):

    """
    Performs a quick preliminary exploratory data analysis (EDA) on a DataFrame.
    
    Arguments:
    df -- pandas DataFrame to analyze

    This function:
    - Displays a random sample of 5 rows
    - Prints the number of rows and columns
    - Shows the DataFrame's structure and data types
    """
    display(df.sample(5))
    print('____________________')
    print('DIMENSIONS')
    print(f'fThe data set has  {df.shape[0]} rows and {df.shape[1]} columns')
    print('_____________________')
    print('INFO')
    df.info()
    print('______________________')
    

    def lower(df,col):
    
        df[col]=df[col].str.lower()