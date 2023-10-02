from statsbombpy import sb
import pandas as pd

matches_ids = sb.matches(43, 106)['match_id']
passes_df = pd.DataFrame()

for i in range(64):
    events = sb.events(matches_ids[i])

    passes = events[events['type'] == 'Pass']

    passes = passes[passes['pass_outcome'].isnull()]  # Completed Pass

    passes['Xloc'] = passes['location'].str[0]
    passes['Xloc+10'] = passes['Xloc'] + 10

    passes['Yloc'] = passes['location'].str[1]

    passes['Xendloc'] = passes['pass_end_location'].str[0]

    passes['Yendloc'] = passes['pass_end_location'].str[1]

    # Simplified Progressive Pass (increase in the X)
    # passes = passes[passes['Xendloc'] > passes['Xloc']]

    # Progressive Pass with at least 10 meters forward
    passes = passes[passes['Xendloc'] > passes['Xloc+10']]

    # Into the final third
    # passes = passes[passes['Xendloc'] > 80]

    # From own half
    # passes = passes[passes['Xloc'] < 60]

    # Into the opposition box
    # passes = passes[(passes['Yendloc'] > 18) & (passes['Yendloc'] < 62) & (passes['Xendloc'] > 102)]

    passes_df = passes_df._append(passes)

print(passes_df.groupby(['player'])['player'].count().sort_values().tail(10))
passes_df.groupby(['player'])['player'].count().sort_values().tail(10).to_csv('Top10PassersInBox.csv')
