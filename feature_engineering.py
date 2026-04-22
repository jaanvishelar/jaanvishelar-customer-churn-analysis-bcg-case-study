import os
print("Current working directory:", os.getcwd())

import pandas as pd

df = pd.read_csv("data/clean_data_after_eda.csv")

df['date_activ'] = pd.to_datetime(df['date_activ'])
df['date_end'] = pd.to_datetime(df['date_end'])

df['contract_duration'] = (df['date_end'] - df['date_activ']).dt.days

df['price_sensitivity'] = (
    df['forecast_price_energy_peak'] -
    df['forecast_price_energy_off_peak']
)

df['cons_change'] = df['cons_last_month'] - (df['cons_12m'] / 12)

df.to_csv("final_model_data.csv", index=False)

print("Final dataset created")