import pandas as pd

df = pd.read_csv("SDG_0111_SEX_AGE_RT_A.csv.gz")

# russia_df = df[df['ref_area'] == 'RUS']
#
# min_data = russia_df['obs_value'].min()
# min_time = russia_df.loc[russia_df['obs_value'].idxmin(), 'time']
# print(f'A year with minimal poverty {min_time} equal {min_data}')
#
# max_data = russia_df['obs_value'].max()
# max_time = russia_df.loc[russia_df['obs_value'].idxmax(), 'time']
# print(f'A year with maximum poverty {max_time} equal {max_data}')
#
# mean = df['obs_value'].mean()
# print(f'World poverty average {mean}')