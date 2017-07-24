from pymongo import Connection


def get_db_connection():
    connection = Connection('localhost', 27017)
    db = connection["BIOMARKERS"]
    return db