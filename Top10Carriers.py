from statsbombpy import sb
import pandas as pd
import csv
import collections
counter = collections.defaultdict(int)

matches_ids = sb.matches(43, 106)['match_id']
carries_df = pd.DataFrame()

for i in range(64):
    events = sb.events(matches_ids[i])
    carries = events[events['type'] == 'Carry']

    carries['Xloc'] = carries['location'].str[0]
    carries['Xloc+10'] = carries['Xloc'] + 10

    carries['Yloc'] = carries['location'].str[1]

    carries['Xendloc'] = carries['carry_end_location'].str[0]

    carries['Yendloc'] = carries['carry_end_location'].str[1]
    # carries = carries[carries['Xendloc'] > carries['Xloc']]  # Simplified Progressive Carry (increase in the X)

    carries = carries[carries['Xendloc'] > carries['Xloc+10']]  # Progressive Carry with at least 10 meters forward

    # carries = carries[carries['Xendloc'] > 80]    #Into the final third

    carries = carries[carries['Xloc'] < 60]       #From own half

    # Into the opposition box
    # carries = carries[(carries['Yendloc'] > 18) & (carries['Yendloc'] < 62) & (carries['Xendloc'] > 102)]

    carries_df = carries_df._append(carries)

print(carries_df.groupby(['player'])['player'].count().sort_values().tail(10))
carries_df.groupby(['player'])['player'].count().sort_values().tail(10).to_csv('Top10CarriersOwnHalf.csv')
