from pages.base_page import BasePage
from playwright.sync_api import expect
import pytest

class LoginPage(BasePage):

    def load(self):
        self.page.goto("https://www.motozem.cz/login/")
        button = self.page.get_by_role("link", name="OK", exact=True)
        self.click(button)


    def invalid_login(self, email, password):
        prihlasit_se = self.page.get_by_role("button", name="Přihlásit se")
        self.page.locator("section").filter(has_text="Přihlášení uživatele pomocí e").locator("#sUserLogin").fill(email)
        self.page.locator("section").filter(has_text="Přihlášení uživatele pomocí e").locator("#sUserPassword").fill(password)
        prihlasit_se.click()
        expect(self.page.get_by_text("Zřejmě jste zadali špatné jmé")).to_be_visible()