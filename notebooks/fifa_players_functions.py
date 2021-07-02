# Purpose:
# House common functions

def create_fifa_players_dataframe(dataset_location):
    import pandas as pd

    return pd.read_csv(dataset_location, encoding='UTF-8')

def drop_columns_from_dataframe(data, columns):
    data_copy = data.copy()
    # display(data.head(10))
    for column in data.columns:
        if column in columns:
            del data[column]

    return data

def create_dataset_by_pos(data, position, ex_columns, show):
    # import pandas as pd
    if(position == 'GK') :
        filtered_data = data.loc[data['Position'] == position]
    else:  filtered_data = data.loc[data['Position'] != position]
    # display(goal_keepers_data)
    filtered_data = drop_columns_from_dataframe(filtered_data, ex_columns)
    # goal_keepers_data = goal_keepers_data[0:0]
    if show:
        print(filtered_data)
    
    return filtered_data

def create_schema_off_dataset(data, file_name):
    import json
    import pandas
    schema = pandas.io.json.build_table_schema(data, index=False, primary_key=None, version=True)
    # print(schema)
    with open(file_name, 'w') as file:
        file.write(json.dumps(schema))
    
def encode_field(data, column):
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    data_copy = data.copy()
    data_copy[column] = le.fit_transform(data[column])
    # display(data_copy)
    return data_copy

cols_to_drop_for_keepers = ['Photo', 'Flag',
    'International Reputation', 'Weak Foot', 'Skill Moves',
     'Body Type', 'Real Face',  'Jersey Number',
    'Joined', 'Loaned From', 'Contract Valid Until',
     'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys',
       'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl',
       'Acceleration', 'SprintSpeed',
     'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
     'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM',
     'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB',
     'LCB', 'CB', 'RCB', 'RB', 
     'Club Logo', 'Release Clause', 'Special', 'Preferred Foot',
     'Marking', 'StandingTackle', 'SlidingTackle']

cols_to_drop_for_players = ['Photo', 'Flag',
    'International Reputation', 'Weak Foot', 'Jersey Number',
    'Joined', 'Loaned From', 'Contract Valid Until', 'Body Type', 'Real Face', 'Skill Moves',
     'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
     'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM',
     'RM', 'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB',
     'LCB', 'CB', 'RCB', 'RB', 
     'Photo', 'Flag', 'Club Logo', 'Release Clause', 'Special', 'Preferred Foot', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes']

# from pathlib import Path
# # dataset location:
# dataset_location = Path('../resources','fifa_world_players_alt.csv')
# raw_data = create_fifa_players_dataframe(dataset_location)

# # raw_data.columns = raw_data.columns.str.replace(' ', '')
# raw_data = encode_field(raw_data, 'Work Rate')
# display(raw_data)
# # raw_data.duplicated
# df_count = raw_data.groupby(raw_data.columns.tolist(),as_index=False).size()
# df_count.prraw_data.groupby(raw_data.columns.tolist(),as_index=False).size() > 0 : print(f"{count} duplicates found.")
# else: print(f"No duplicates found.")


# players_data = create_dataset_by_pos(raw_data, ' ', cols_to_drop_for_players, 0)
# # drop null fields
# if(players_data.isna().sum().sum()):
#     players_data.dropna(inplace=True)
# # drop the index column
# players_data.drop(players_data.columns[0], axis=1, inplace=True)
# display(players_data.info())

# %time players_data['BasicSkills'] = players_data.apply(score_basic_skills, axis = 1)
# %time players_data['DefensiveScore'] = players_data.apply(score_defending_skills, axis = 1)
# %time players_data['ShootingScore'] = players_data.apply(score_shooting_skills, axis = 1)
# %time players_data['MentalStrength'] = players_data.apply(score_mental_strength, axis = 1)
# %time players_data['PassingSkills'] = players_data.apply(score_passing_skills, axis = 1)
# %time players_data['PhysicalStrength'] = players_data.apply(score_basic_skills, axis = 1)
# %time players_data['MobilityScore'] = players_data.apply(score_mobility_skills, axis = 1)

# file_name = 'players_schema.txt'
# create_schema_off_dataset(players_data, Path('../resources/',file_name))
# file_name = 'players.csv'
# players_data.to_csv(Path('../resources/', file_name),line_terminator='\n', index=False , encoding = 'UTF-8')

# goal_keepers_data = create_dataset_by_pos(raw_data, 'GK', cols_to_drop_for_keepers, 0)
# # display(goal_keepers_data.columns)
# # display(goal_keepers_dataframe.info())
# # drop null values
# if(goal_keepers_data.isna().sum().sum()):
#    goal_keepers_data.dropna(inplace=True)

# goal_keepers_data.drop(goal_keepers_data.columns[0], axis=1, inplace=True)
# # display(goal_keepers_data.info())
# # values for creating sql schema
# file_name = 'goal_keepers_schema.txt'
# create_schema_off_dataset(goal_keepers_data, Path('../resources/', file_name))
# file_name = 'goal_keepers.csv'
# goal_keepers_data.to_csv(Path('../resources/', file_name), line_terminator='\n', index=False, encoding = 'UTF-8')

def create_fifa_players_dataset(data_in, file_loc, schema_file, csv_file, show=False):
    from pathlib import Path
    
    # check and drop nulls
    count_na = data_in.isna().sum().sum()
    # print(count_na)
    if count_na > 0:
        data_in = data_in.dropna()

    # https://stackoverflow.com/questions/48366506/calculate-new-column-as-the-mean-of-other-columns-pandas/48366525
    col = []
    col = data_in.loc[:, 'Overall':'Potential']

    data_in['Rating'] = (col.mean(axis=1))

    data_in = data_in.infer_objects()
    # store values for creating sql schema
    data_in = drop_columns_from_dataframe(data_in, ['Overall', 'Potential'])
    # file_name = schema_file
    create_schema_off_dataset(data_in, Path(file_loc, schema_file))
    # file_name = csv_file
    data_in.to_csv(Path(file_loc, csv_file), index = False, line_terminator='\n')


    if show:
        print(col.mean(axis=1))
        print(data_in.info())
        print(data_in.describe(exclude =[object, int]))

    return data_in


