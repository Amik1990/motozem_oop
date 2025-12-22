from typing import Dict
import pytest
import re
from playwright.sync_api import BrowserType, sync_playwright, Page, expect
from utils import get_logger
from utils.config import config  # Import configu

from pages import (
    HeaderPage,
    LoginPage,
    MotozemDobraPage,
    HomePage,
    ShoppingCartPage
)

from utils.fixture_utils import setup_page # Import naší nové pomocné funkce

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """
    Tato fixture nastavuje parametry pro spuštění prohlížeče.
    Hodnota headless se bere z konfigurace (.env).
    """
    return {
        **browser_type_launch_args,
        "headless": config.BROWSER_HEADLESS,  # Použití hodnoty z configu
        "slow_mo": 500      # Volitelné: zpomalí test, abych viděl, co se děje
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Tato fixture umožní nastavit parametry pro prohlížeč.
    Pokud spustíš PWDEBUG=1, Playwright si headless mód pořeší sám.
    """
    return {
        **browser_context_args,
        "viewport": None, # Nastavení velikosti okna
    }

@pytest.fixture()
def load_home_page(page: Page):    # načtění stránky motozem
    return setup_page(HomePage, page)

@pytest.fixture()
def load_header_page(page: Page):    # načtění stránky motozem
    return setup_page(HeaderPage, page)

@pytest.fixture()
def load_login_page(page: Page):    # načtění stránky motozem
    return setup_page(LoginPage, page)

@pytest.fixture()
def load_shopping_cart_page(page: Page):    # načtění stránky motozem
    return setup_page(ShoppingCartPage, page)

@pytest.fixture()
def load_motozem_dobra(page: Page):
    return setup_page(MotozemDobraPage, page)

# @pytest.fixture()
# def add_to_shopping_cart(page, load_home_page):
#     page.get_by_role("banner").get_by_role("textbox").fill("revit tornado 3")
#     revit_tornado = page.get_by_role("link", name="Výprodej -2 062 Kč Bunda na motorku Revit Tornado 3 černá výprodej 6 187 Kč 8")
#     lupa = page.get_by_role("button", name="Hledat")
#     medium_size = page.locator("label:nth-child(2)").first
#     koupit_button = page.get_by_role("button", name="Koupit")
#     pocet_v_kosiku = page.locator("a").filter(has_text=re.compile(r"^2$"))
#
#     lupa.click()
#     expect(revit_tornado).to_be_visible()
#     revit_tornado.click()
#     medium_size.click()
#     koupit_button.click()
#     expect(pocet_v_kosiku).to_have_text("2")

#Vytvořili jsme conftest.py s funkci viz níže, aby se ignorovaly případné chyby https během testování
#@pytest.fixture(scope="session")
#def browser_context_args(browser_context_args):
 #   return {
 #       **browser_context_args,
 #       "ignore_https_errors": True
  #  }


#Kód níže nám slouží ke změně rozlišení v prováděných testech
# @pytest.fixture(scope="session")
# # def browser_context_args(browser_context_args):
# #     return {
# #         **browser_context_args,
# #         "viewport": {
# #             "width": 800,
# #             "height": 455,
# #         }
# #     }


# Pokud chci, aby se mi test zobrazil v rozlišení podle konkrétního zařízení, tak napíšu, viz níže:
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     return {
#         **browser_context_args,
#         **iphone_11,
#     }


# kód níže použiju, když chci změnit jazyk webové stránky
from playwright.sync_api import BrowserType
from typing import Dict


# @pytest.fixture(scope="session")
# def context(
#         browser_type: BrowserType,
#         browser_type_launch_args: Dict,
#         browser_context_args: Dict,
#         ):
#     context = browser_type.launch_persistent_context(
#         "./foobar",
#         **{
#             **browser_type_launch_args,
#             **browser_context_args,
#             "locale": "de-DE",
#             })
#     yield context
#     context.close()
