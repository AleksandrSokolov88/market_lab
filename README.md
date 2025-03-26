Добрый день!
Так как база данных на сайте не очищается и нет возможности проверить ту же самую тест дату, 
я сделал несколько костылей, чтобы email немного менялся для позитивных тестов. Посмотреть можно в
ulits


Успел автоматизировать только проверку корректных email


1

pytest  --alluredir=reports/allure-results


2

tools\allure_2_32\bin\allure generate reports/allure-results -o reports/allure-report --clean

3

allure open reports/allure-report
