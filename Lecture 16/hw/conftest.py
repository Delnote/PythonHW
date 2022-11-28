import pytest

from loggers import *
from _pytest.fixtures import fixture
from selenium import webdriver
from constants import *


@pytest.fixture(autouse=True, scope="function")
def setup_function(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(URL)
    request.cls.driver.maximize_window()
    yield request.cls.driver
    request.cls.driver.close()


@fixture(scope='function', autouse=True)
def get_test_name(request):
    logger.info('{} starts!'.format(request.node.name))

    def get_test_name_finished():
        logger.info('{} finished!'.format(request.node.name))
    request.addfinalizer(get_test_name_finished)
    return request.fixturename
