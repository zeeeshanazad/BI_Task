import dotenv
import os
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import transform
import argparse


def connect_db():
    dotenv.load_dotenv()
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://" + db_user + ":" + db_password + "@" + db_host + ":" + db_port + "/" + db_name)
        con = engine.connect()
        return con
    except SQLAlchemyError as e:
        print('Can not connect to the database due to error: ', e)
        return None


def parse_args():
    parser = argparse.ArgumentParser(description='For index images analysis')
    parser.add_argument('save', dest='save', type=str, help='save', default='to_db')
    parser.add_argument('level', dest='level', type=str, help='level', default='1')
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    # args = parse_args()
    # save_to = 'to_db'  # args.__getattribute__('save') if args.__contains__('save') else 'to_db'
    # normalize_level = 1  # args.__getattribute__('level') if args.__contains__('normalize_level') else 1

    print('Starting...')
    save_to = 'to_db'
    normalize_level = 1

    data1 = transform.normalize('./datasets/845b7324-9b19-4d8b-ad12-9fc93793946b.json', level=normalize_level)
    data2 = transform.normalize('./datasets/c1fb85c6-1803-4a83-8de8-6fec7b324a04.json', level=normalize_level)

    if save_to == 'to_db':
        print('Connecting to database')
        con = connect_db()
        if con:
            print('Saving to database')
            transform.to_db(con, data1, data2)
    elif save_to == 'to_csv':
        transform.to_csv(data1, data2)
    else:
        print('Argument value is invalid')

    print('done')
