import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

# 2 фикстуры выше просто создают объект и т.о. его можно уже не создавать в самом тесте (как по мне не очень ок, лучше прямо вибеть, что ты объект создал)