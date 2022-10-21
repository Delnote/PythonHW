import sqlite3


class TableData:

    def __new__(cls, database_name, table_name):
        return cls.fetch_data_table(database_name, table_name)

    @classmethod
    def fetch_data_table(cls, database_name, table_name):
        values = {}
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * from {}'.format(table_name))
        output = cursor.fetchall()
        for row in output:
            values[row[0]] = row
        return values
