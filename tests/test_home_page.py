from pages.home_page import HomePage
from playwright.sync_api import expect, Page

# def test_load_home_page(load_home_page):
#     load_home_page.load()

def test_banner_motozem_is_visible(load_home_page):
    load_home_page.is_banner_visible()

def test_poradime_vam_menu_is_visible(load_home_page):
    load_home_page.poradime_vam_menu_is_visible()

def test_poradime_vam_menu_content_is_present(load_home_page):
    load_home_page.poradime_vam_menu_content_is_present()

def test_state_flag_is_visible(load_home_page):
    load_home_page.state_flag_is_visible()

def test_state_flags_are_visible_when_hover_over(load_home_page):
    load_home_page.state_flags_are_visible_when_hover_over()

def test_muj_ucet_is_visible(load_home_page):
    load_home_page.muj_ucet_is_visible()

def test_ucet_menu_is_visible_when_hoover_over_muj_ucet(load_home_page):
    load_home_page.ucet_menu_is_visible_when_hoover_over_muj_ucet()

def test_prihlaseni_uzivatele_is_visible(load_home_page):
    load_home_page.prihlaseni_uzivatele_is_visible()