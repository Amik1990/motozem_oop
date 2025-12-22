from pages.base_page import BasePage
from playwright.sync_api import expect
import re
from utils.config import config

class MotozemDobraPage(BasePage):
    """
    Třída reprezentující stránku pobočky Motozem Dobrá.
    """

    def load(self) -> None:
        """
        Načte stránku pobočky Dobrá a potvrdí cookies.
        """
        self.navigate(f"{config.BASE_URL}/motozem-dobra/")
        self.accept_cookies()
        self.expect_visible(self.page.get_by_role("heading", name="Motoshop Dobrá"), name="Nadpis Motoshop Dobrá")

    def lokace_dobra_google_maps_open(self) -> None:
        """
        Ověří zobrazení mapy Google Maps pro pobočku Dobrá v novém okně.
        """
        motoshop_dobra_banner = self.page.get_by_role("heading", name="Motoshop Dobrá")
        souradnice_dobra = self.page.get_by_text("18.416489")

        self.expect_visible(motoshop_dobra_banner, name="Motoshop Dobra banner")
        self.expect_visible(souradnice_dobra, name="Souřadnice")

        with self.page.expect_popup() as new_window:
            self.click(self.page.get_by_role("link", name="Ukázat na mapě"), name="Odkaz Ukázat na mapě")
        
        google_maps = new_window.value
        google_maps.wait_for_load_state()

        try:
            accept_button = google_maps.get_by_role("button", name="Přijmout vše")
            self.expect_visible(accept_button, name="Tlačítko Přijmout vše", timeout=5000)
            accept_button.click()
        except:
            self.LOG.info("Cookies lišta na Google Maps nebyla nalezena nebo už zmizela.")
            pass

        expect(google_maps).to_have_url(re.compile(r"https://www\.google\.[a-z.]+/maps.*"))
        google_maps_dobra = google_maps.get_by_role("heading", name="MotoZem - Dobrá", exact=True)
        self.expect_visible(google_maps_dobra, name="Nadpis 'MotoZem - Dobrá' na mapě")
