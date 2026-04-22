import pandas as pd
import matplotlib.pyplot as plt
client_df = pd.read_csv("data/client_data.csv")
price_df = pd.read_csv("data/price_data.csv")
client_df.head()
price_df.head()
client_df.info()
price_df.info()
#The dataset contains numerical and categorical variables. Some columns like dates are stored as object type and need conversion.
# Convert date columns to datetime
date_cols = ['date_activ', 'date_end', 'date_modif_prod', 'date_renewal']

for col in date_cols:
    client_df[col] = pd.to_datetime(client_df[col])

price_df['price_date'] = pd.to_datetime(price_df['price_date'])
#descriptive statistics for numerical columns
client_df.describe()
price_df.describe() 
client_df.nunique()
price_df.nunique()
#Descriptive statistics show the spread and distribution of numerical data. Unique values help identify categorical and continuous variables
#checking for missing values
client_df.isnull().sum()
price_df.isnull().sum()
#Missing values are checked to understand data quality and will be handled later if needed.
client_df.hist(figsize=(15,10))
plt.show()
client_df['churn'].value_counts().plot(kind='bar')
plt.title("Churn Distribution")
plt.show()
price_df[['price_off_peak_var', 'price_peak_var']].hist(figsize=(10,5))
plt.show()
client_df.groupby('churn')['cons_12m'].mean()

