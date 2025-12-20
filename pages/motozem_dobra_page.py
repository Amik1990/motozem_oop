from pages.base_page import BasePage
from playwright.sync_api import expect
import re

class MotozemDobraPage(BasePage):

    def load(self):  # pouzije se pak v fixture_utils.py v setup_page casti try  instance.load
     self.navigate("https://www.motozem.cz/motozem-dobra/")
     self.accept_cookies()
     # Ověření, že se stránka skutečně načetla (vidím nadpis)
     self.expect_visible(self.page.get_by_role("heading", name="Motoshop Dobrá"), name="Nadpis Motoshop Dobrá")

    def lokace_dobra_google_maps_open(self):
        motoshop_dobra_banner = self.page.get_by_role("heading", name="Motoshop Dobrá")
        souradnice_dobra = self.page.get_by_text("18.416489")

        self.expect_visible(motoshop_dobra_banner, name="Motoshop Dobra banner")
        self.expect_visible(souradnice_dobra, name="Souřadnice")


        # kdyz kliknu na Ukazat na mape, tak se zobrazi samostatne okno, proto pouziju "with"
        with self.page.expect_popup() as new_window:
            self.click(self.page.get_by_role("link", name="Ukázat na mapě"), name="Odkaz Ukázat na mapě")
        
        google_maps = new_window.value     # .value: Je vlastnost tohoto objektu, která obsahuje skutečný objekt stránky (Page) toho nového okna.
        google_maps.wait_for_load_state()

        # Pouziju try, kdyby se nahodou nezobrazilo cookies window.
        try:
            accept_button = google_maps.get_by_role("button", name="Přijmout vše")
            # Ověříme viditelnost (pokud není vidět, spadne do except)
            self.expect_visible(accept_button, name="Tlačítko Přijmout vše", timeout=5000)
            # Klikneme přímo na element v novém okně
            self.click(accept_button, name="Tlačítko Přijmout vše")

        except:
            self.LOG.info("Cookies lišta na Google Maps nebyla nalezena nebo už zmizela.")
            pass

        expect(google_maps).to_have_url(re.compile(r"https://www\.google\.[a-z.]+/maps.*"))
        google_maps_dobra = google_maps.get_by_role("heading", name="MotoZem - Dobrá", exact=True)
        self.expect_visible(google_maps_dobra, "Google Maps", timeout=5000)
