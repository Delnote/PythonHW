import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.table_name = table_name
        self.cursor = self.fetch_data_table(database_name)

    def __len__(self):
        self.cursor.execute('select count(*) from {}'.format(self.table_name))
        return self.cursor.fetchone()[0]

    def __getitem__(self, president_name):
        self.cursor.execute('SELECT * from {} where name=\'{}\''.format(self.table_name, president_name))
        return self.cursor.fetchone()

    def __iter__(self):
        data = self.cursor.execute('SELECT * from {}'.format(self.table_name))
        return iter(data.fetchone())

    @classmethod
    def fetch_data_table(cls, database_name):
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        return cursor
