import pytest
from hw2 import TableData


@pytest.fixture
def file_path():
    yield 'example.sqlite'


def test_data_base(file_path):
    presidents = TableData(database_name=file_path, table_name='presidents')
    assert len(presidents) is 3
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    print(len(presidents))
    assert 'Yeltsin' in presidents
    for president in presidents:
        print(president['name'])