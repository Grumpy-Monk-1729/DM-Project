
all_filenames = ['new input/QSO.csv','new input/Galaxy.csv','new input/Star.csv']
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "SDSS_combined.csv", index=False, encoding='utf-8-sig')
df = pd.read_csv('SDSS_combined.csv')
#Handling missing values
df = df.dropna()
sdss_df_fe = df
sdss_df_fe = sdss_df

# encode class labels to integers
le = LabelEncoder()
y_encoded = le.fit_transform(sdss_df_fe['class'])
sdss_df_fe['class'] = y_encoded

