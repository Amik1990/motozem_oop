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
        with self.page.expect_popup() as page1_info:
            self.page.get_by_role("link", name="Ukázat na mapě").click(timeout=5000)
        page1 = page1_info.value
        page1.get_by_role("button", name="Přijmout vše").click(timeout=5000)

        expect(page1).to_have_url(re.compile(r"https://www\.google\.[a-z.]+/maps.*"))
        google_maps_dobra = page1.get_by_role("heading", name="MotoZem - Dobrá", exact=True)
        expect(google_maps_dobra).to_be_visible()