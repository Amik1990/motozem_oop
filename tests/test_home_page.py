from pages.home_page import HomePage
from playwright.sync_api import expect, Page

def test_load_home_page(load_motozem):
    load_motozem.load()


def test_banner_motozem_is_visible(load_motozem):
    load_motozem.is_banner_visible()

def test_poradime_vam_menu_is_visible(load_motozem):
    load_motozem.poradime_vam_menu_is_visible()

def test_poradime_vam_menu_content_is_present(load_motozem):
    load_motozem.poradime_vam_menu_content_is_present()
