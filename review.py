def review(df):
    
    print('Shape of the data frame:')
    print(df.shape)
    print()

    cols = df.columns.to_list()
    print('Columns in the data frame:')
    for col in cols:
        print(col, end=', ')
    print('\n')
    
    print('Data types of columns:')
    print(df.dtypes)
        
    

