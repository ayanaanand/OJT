import pandas as pd


df = pd.read_csv('air-pollution.csv')

print("Columns in the DataFrame:", df.columns)


filtered_df = df[df['Entity'] == 'Afghanistan']


column_of_interest = 'Nitrogen oxide (NOx)'


if column_of_interest in filtered_df.columns:
    filtered_df['median'] = filtered_df[column_of_interest].median()
    filtered_df['mean'] = filtered_df[column_of_interest].mean()
    filtered_df['std'] = filtered_df[column_of_interest].std()
else:
    print(f"Column '{column_of_interest}' does not exist in the DataFrame.")


filtered_df = filtered_df.drop_duplicates()


filtered_df = filtered_df.fillna(0)

filtered_df.to_csv('filtered_output.csv', index=False)

print(filtered_df)
