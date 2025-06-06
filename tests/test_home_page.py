from pages.home_page import HomePage
from playwright.sync_api import expect, Page

def test_load_home_page(load_home_page):
    load_home_page.load()

def test_banner_motozem_is_visible(load_home_page):
    load_home_page.is_banner_visible()

def test_poradime_vam_menu_is_visible(load_main_page):
    load_main_page.poradime_vam_menu_is_visible()

def test_poradime_vam_menu_content_is_present(load_home_page):
    load_home_page.poradime_vam_menu_content_is_present()

def test_state_flag_is_visible(load_home_page):
    load_home_page.state_flag_is_visible()

def test_state_flags_are_visible_when_hover_over(load_home_page):
    load_home_page.state_flags_are_visible_when_hover_over()