from pages.header_page import HeaderPage
from pages.home_page import HomePage
from playwright.sync_api import expect, Page

def test_lokace_dobra(load_motozem_dobra):
    load_motozem_dobra.lokace_dobra_google_maps_open()


