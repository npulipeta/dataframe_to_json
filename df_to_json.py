import pandas as pd

data = pd.read_csv('input.csv')
data.rename(columns={"Person Id":"person_id", "Floor Access DateTime":"date_time",
                     "Floor Level":"floor_level", "Building":"building"},inplace=True)
data.person_id = data.person_id.astype(str)
data.date_time = pd.to_datetime(data.date_time)
data.to_json('output.json', orient='records', lines=True, date_format='iso')