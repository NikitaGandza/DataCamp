from pprint import pprint
import pandas as pd 

# List of words to pair with products
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop', 'sale', 'cheap' ]
keywords_list = []

#loop though the list to create combinations
for product in products:
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, product + ' ' + word])
#pprint for more accurate list
pprint(keywords_list)

# Create a DataFrame from list, 1st DataFrame
keywords_df = pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it (first 5 rows)
print(keywords_df.head())

# rename colums by index
keywords_df = keywords_df.rename(columns = {0 : 'Ad Group' , 1 : 'Keyword'})

#Addind new columns
keywords_df['Campaign'] = 'SEM_Sofas'
keywords_df['Criterion Type'] = 'Exact'
#print(keywords_df)

#copying the list, 2nd DataFrame
keywords_phrase = keywords_df.copy()
#changing value of Criterion Type from Exact to phrase
keywords_phrase['Criterion Type'] = 'Phrase'
#append both 
keywords_df_final = keywords_df.append(keywords_phrase)
print(keywords_df_final)

#extract csv
keywords_df_final.to_csv('keywords.csv', index=False)

summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)