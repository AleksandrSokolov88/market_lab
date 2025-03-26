import os
import pytest
from utils.change_test_email_in_all_yaml import change_data_positive_email

ALLURE_RESULTS = "reports/allure-results"


@pytest.fixture(scope="session", autouse=True)
def clean_allure_results_folder():
    if os.path.exists(ALLURE_RESULTS):
        for file_name in os.listdir(ALLURE_RESULTS):
            file_path = os.path.join(ALLURE_RESULTS, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    yield


@pytest.fixture(scope="session",autouse=True)
def change_email_for_test_positive():
    change_data_positive_email()
