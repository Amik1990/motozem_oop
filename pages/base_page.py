from playwright.sync_api import Page, expect
from playwright.sync_api import Locator
import re
from utils.logger_config import get_logger

class BasePage:
    """
    Základní třída pro všechny Page Objecty.
    Obsahuje společné metody pro interakci s prohlížečem a logování.
    """
    
    def __init__(self, page: Page):
        self.page = page
        self.LOG = get_logger(self.__class__.__name__)

    def navigate(self, url: str) -> None:
        """Navigace na danou URL s logováním."""
        self.LOG.info(f"Navigace na URL: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def accept_cookies(self) -> None:
        """Pokusí se potvrdit cookies lištu, pokud je viditelná."""
        button = self.page.get_by_role("link", name="OK", exact=True)
        if button.is_visible():
            self.click(button, name="OK cookie button")

    def click(self, element, name: str = "element") -> None:
        """
        Kliknutí na element (podporuje string i Locator).
        
        Args:
            element: Selektor (str) nebo Locator objekt.
            name: Název prvku pro logování.
        """
        self.LOG.info(f"Kliknutí na: {name}")
        if hasattr(element, "click") and not isinstance(element, str):
            element.click()
        else:
            self.page.click(element)

    def click_and_wait_for_response(self, element: Locator, url_pattern: str, name: str = "element") -> None:
        """
        Klikne na prvek a počká na síťovou odpověď (API request).
        
        Args:
            element: Tlačítko, na které se kliká.
            url_pattern: Regulární výraz nebo část URL, na kterou se čeká.
            name: Název pro logování.
        """
        self.LOG.info(f"Klikám na '{name}' a čekám na odpověď obsahující '{url_pattern}'")
        
        # Lambda funkce ověří, že URL obsahuje náš pattern a status je 200 (OK)
        # Používáme re.search pro flexibilitu (pokud je url_pattern regex)
        def predicate(response):
            url_match = re.search(url_pattern, response.url) or (url_pattern in response.url)
            return url_match and response.status == 200

        try:
            with self.page.expect_response(predicate, timeout=10000) as response_info:
                self.click(element, name)
            self.LOG.success(f"Odpověď pro '{url_pattern}' úspěšně zachycena.")
        except Exception as e:
            self.LOG.error(f"Časový limit vypršel při čekání na odpověď '{url_pattern}' po kliknutí na '{name}'.")
            raise e

    def fill(self, selector: Locator | str, value: str, name: str = "input field") -> None:
        """
        Vyplnění input pole.
        Podporuje jak string selektor, tak Locator objekt.
        """
        self.LOG.info(f"Vyplňování {name} (Selektor: {selector}) s hodnotou: '***'")
        
        if hasattr(selector, "fill") and not isinstance(selector, str):
            selector.fill(value)
        else:
            self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        """Získání textu z elementu."""
        text = self.page.inner_text(selector)
        self.LOG.debug(f"Získaný text ze selektoru {selector}: '{text[:50]}...'")
        return text

    def hover(self, element: Locator, name: str = "element") -> None:
        """Najetí myší na element."""
        self.LOG.info(f"Ověřuji, zda je viditelný {name}")
        element.hover()

    def expect_visible(self, element: Locator, name: str = "element", timeout: int = 5000) -> None:
        """
        Ověří, že je prvek viditelný.
        
        Args:
            element: Locator prvku.
            name: Název prvku pro logování.
            timeout: Maximální čas čekání v ms.
        """
        self.LOG.info(f"Ověřuji, zda prvek je viditelný: {name}")
        try:
            expect(element).to_be_visible(timeout=timeout)
            self.LOG.success(f"Prvek '{name}' je viditelný")
        except Exception as e:
            self.LOG.error(f"Prvek '{name}' není viditelný! (Timeout: {timeout}ms)")
            raise e

    def to_have_text(self, element: Locator, expected_text: str, name: str = "element") -> None:
        """
        Ověří, že prvek obsahuje konkrétní text.
        """
        self.LOG.info(f"Ověřuji, zda má '{name}'  text: '{expected_text} ")
        try:
            expect(element).to_have_text(expected_text)
            actual_text = element.inner_text()
            self.LOG.success(f"Prvek '{name}' obsahuje text: '{actual_text}', očekáváme: '{expected_text}'")
        except Exception as e:
            actual_text = element.inner_text()
            self.LOG.error(f"Chyba: '{name}' má text '{actual_text}', ale čekali jsme '{expected_text}'")
            raise e

    def to_have_attribute(self, element: Locator, attribute_name: str, expected_value: str, name: str = "element") -> None:
        """
        Ověří, že prvek má daný atribut s konkrétní hodnotou.
        """
        self.LOG.info(f"Ověřuji, zda má '{name}' atribut '{attribute_name}' s hodnotou: '{expected_value}'")
        try:
            expect(element).to_have_attribute(attribute_name, expected_value)
            actual_value = element.get_attribute(attribute_name)
            self.LOG.success(f"Prvek '{name}' má atribut '{attribute_name}' s hodnotou '{actual_value}' (očekáváno: '{expected_value}')")
        except Exception as e:
            actual_value = element.get_attribute(attribute_name)
            self.LOG.error(f"Chyba: Prvek '{name}' má atribut '{attribute_name}' s hodnotou '{actual_value}', ale čekali jsme '{expected_value}'")
            raise e

    def to_have_value(self, element: Locator, expected_value: str, name: str = "element") -> None:
        """
        Ověří, že prvek (typicky input) má danou hodnotu (atribut value).
        """
        self.LOG.info(f"Ověřuji, zda má '{name}' hodnotu: '{expected_value}'")
        try:
            expect(element).to_have_value(expected_value)
            actual_value = element.input_value()
            self.LOG.success(f"Prvek '{name}' má hodnotu '{actual_value}' (očekáváno: '{expected_value}')")
        except Exception as e:
            try:
                actual_value = element.input_value()
                self.LOG.error(f"Chyba: Prvek '{name}' má hodnotu '{actual_value}', ale čekali jsme '{expected_value}'")
            except:
                self.LOG.error(f"Chyba: Prvek '{name}' nemá očekávanou hodnotu '{expected_value}' a nepodařilo se získat jeho aktuální hodnotu.")
            raise e
