import pandas as pd

def explora_df_abtesting (df, control_col):
    for categoric in df['control_col'].unique():
        df_filter= df[df['control_col']== categoric]
        print(f'Main statistics for the categorical column {categoric.upper()}')
        display(df_filter.describe(include='O').T)
        print(f'Main statistics for the numerical columns {categoric.upper()}')
        display(df_filter.describe().T)
        print('_________________________________________________________')