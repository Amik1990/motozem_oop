from multiprocessing.util import get_logger
from tkinter.font import names

from playwright.sync_api import Page, expect
from playwright.sync_api import Locator
import re
from utils.logger_config import get_logger

class BasePage:
    def __init__(self, page):
        self.page = page
        self.LOG = get_logger(self.__class__.__name__)

    def navigate(self, url):
        """Navigace na danou URL s logováním."""
        self.LOG.info(f"Navigace na URL: {url}")  # Logování akce
        self.page.goto(url)  # Playwright akce
        self.page.wait_for_load_state("networkidle")  # Počkat, až se síť uklidní

    def click(self, element, name="element"):
        """Kliknutí na element (podporuje string i Locator."""
        self.LOG.info(f"Kliknutí na: {name}")
        # Kontrola: Pokud je element Locator, voláme .click() přímo na něm
        # Pokud je to string, použijeme self.page.click()
        if hasattr(element, "click") and not isinstance(element, str):
            element.click()  # Toto funguje pro get_by_role, get_by_label atd.
        else:
            self.page.click(element)  # Toto funguje pro stringové selektory

    def fill(self, selector, value, name="input field"):
        """Vyplnění input pole."""
        self.LOG.info(f"Vyplňování {name} (Selektor: {selector}) s hodnotou: '***'")  # Maskování citlivých dat
        self.page.fill(selector, value)  # Playwright akce

    def get_text(self, selector):
        """Získání textu z elementu."""
        text = self.page.inner_text(selector)  # Playwright akce
        self.LOG.debug(f"Získaný text ze selektoru {selector}: '{text[:50]}...'")
        return text

    def hover(self, element: Locator, name: str = "element"):
        self.LOG.info(f"Ověřuji, zda je viditelný {name}")
        element.hover()

    def expect_visible(self, element: Locator, name: str = "element"):
        """Ověří, že je prvek viditelný, s logováním výsledku."""
        self.LOG.info(f"Ověřuji, zda je viditelný: {name}")   # Logování pokusu o validaci
        try:
            expect(element).to_be_visible()
            self.LOG.success(f"Prvek '{name}' je viditelný")  # Logování úspěchu
        except Exception as e:
            self.LOG.error(f"Prvek '{name}' není viditelný!") # Logování chyby
            raise e      # Vyhození výjimky dál pro Pytest

    def to_have_text(self, element: Locator, expected_text: str,  name: str = "element"):
        """Ověří, že prvek obsahuje konkrétní text."""
        self.LOG.info(f"Ověřuji, zda má '{name}'  text: '{expected_text} ")
        try:
            expect(element).to_have_text()
            self.LOG.success(f"Prvek '{name}' obsahuje text: '{expected_text}")  # Logování úspěchu
        except Exception as e:
            actual_text = element.inner_text()     # Získání aktuálního textu pro lepší debug
            self.LOG.error(f"Chyba: '{name}' má text '{actual_text}', ale čekali jsme '{expected_text}'")  # Logování chyby
            raise e  # Vyhození výjimky dál pro Pytest

    def to_have_attribute(self, element: Locator, expected_text: str, attribute: str = "element"):

        self.LOG.info(f"Ověřuji, zda má '{attribute}'  atribut: '{expected_text}")
        try:
            expect(element).to_have_attribute()
            self.LOG.success(f"Prvek '{attribute}' obsahuje text: '{expected_text}")
        except Exception as e:
            actual_text = element.inner_text()
            self.LOG.error(f"Chyba: '{attribute}' obsahuje text '{actual_text}', ale čekali jsme: '{expected_text}'")



