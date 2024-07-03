import pytest
# from pages.login_page import LoginPage -- уже не надо, т.к. это перекрывает фикстура из conftest.py (внутри неё мы создаём объекты и т.о. в тесте уже не создаём)
# from pages.dashboard_page import DashboardPage -- уже не надо, т.к. это перекрывает фикстура из conftest.py (внутри неё мы создаём объекты и т.о. в тесте уже не создаём)

def test_login_failure(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'

@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])

def test_login_success(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username, password)
    
    dashboard_page.assert_welcome_message(f"Welcome {username}")

# https://zimaev.github.io/pom/index.html