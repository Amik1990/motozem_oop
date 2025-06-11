from pages.base_page import BasePage
from playwright.sync_api import expect
import re

class MotozemDobraPage(BasePage):

    def load(self):
        self.page.goto("https://www.motozem.cz/motozem-dobra/")
        button = self.page.get_by_role("link", name="OK", exact=True)
        self.click(button)


    def lokace_dobra_google_maps_open(self):
        motoshop_dobra_banner = self.page.get_by_role("heading", name="Motoshop Dobrá")
        souradnice_dobra = self.page.get_by_text("18.416489")

        expect(motoshop_dobra_banner).to_be_visible()
        expect(souradnice_dobra).to_be_visible()

        # kdyz kliknu na Ukazat na mape, tak se zobrazi samostatne okno, proto pouziju with
        with self.page.expect_popup() as new_window:
            self.page.get_by_role("link", name="Ukázat na mapě").click(timeout=5000)
        google_maps = new_window.value

# Pouziju try, kdyby se nahodou nezobrazilo cookies window.
        try:
            accept_button = google_maps.get_by_role("button", name="Přijmout vše")
            if accept_button.is_visible(timeout=3000):
                accept_button.click()
        except:
            pass


        expect(google_maps).to_have_url(re.compile(r"https://www\.google\.[a-z.]+/maps.*"))
        google_maps_dobra = google_maps.get_by_role("heading", name="MotoZem - Dobrá", exact=True)
        expect(google_maps_dobra).to_be_visible()