import pandas as pd

df = pd.read_csv('../data/traffic_data.csv')

print("Website Traffic Data:\\n")
print(df)

# Average page views
avg_views = df['PageViews'].mean()
print("\\nAverage Page Views:", avg_views)

# Average session duration
avg_duration = df['SessionDuration'].mean()
print("Average Session Duration:", avg_duration)

# Users who dropped off
print("\\nUsers who dropped off:")
print(df[df['DropOff'] == 'Yes'])

print("\\nTraffic Analysis Completed!")