import pandas as pd
df = pd.read_csv('./ratings_train.csv')
df_test = pd.read_csv('./ratings_test.csv')
header_list = ['id', 'event', 'rating', 'time']

df.to_csv('./train.csv', header=header_list, index=False)
df_test.to_csv('./test.csv', header=header_list, index=False)

