import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize('username, password', [    # В одном тесте мы проверили 2 логина/пароля!
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f"Welcome {username}")

# https://zimaev.github.io/pom/index.html