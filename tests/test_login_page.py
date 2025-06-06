from pages.header_page import HeaderPage
from pages.home_page import HomePage
from playwright.sync_api import expect, Page
import pytest


@pytest.mark.parametrize("email, password", [
    ("zubnicentrum@gmail.com", "zubnikaz5"),
    ("espresso@seznam.cz", "lavazza"),
    ("emailbezzavinace", "boeing"),
])
def test_invalid_login(load_login_page, email, password):
    load_login_page.invalid_login(email, password)
