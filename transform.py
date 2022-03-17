import pandas as pd
import json
from json import JSONDecodeError
from sqlalchemy.exc import SQLAlchemyError


def normalize(path, level=1):
    try:
        data = json.load(open(path))
    except JSONDecodeError as e:
        file_name = path.split('/')
        print('ERROR', e)
        print('DESCRIPTION: Cannot process '+file_name[-1]+' File is either empty or not in correct JSON format')
        return None
    else:
        data = pd.json_normalize(data, max_level=level)
        return data


def to_csv(*args):
    data = pd.DataFrame()
    for i in args:
        if i is not None:
            data = data.append(i)
    data.reset_index(inplace=True, drop=True)
    data.to_csv('json_to_csv.csv', index=False)


def to_db(con, *args):
    data = pd.DataFrame()
    for i in args:
        data = data.append(i)
    data.reset_index(inplace=True, drop=True)
    data = data.applymap(json.dumps)
    try:
        data.to_sql(name='loan_application', con=con, if_exists='append', index=False)
        print('Saved to database')
    except SQLAlchemyError as e:
        print(e)
