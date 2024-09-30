def review(df):
    print('DATA REVIEW')
    print('-' * 50)
    
    print('Shape of the data frame:')
    print(df.shape)
    print()

    cols = df.columns.to_list()
    print('Columns in the data frame:')
    for col in cols:
        print(col, end=', ')
    print()
    
    print('Data types of columns:')
    print(df.dtypes)
    print()
        
    

