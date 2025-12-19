from pages.base_page import BasePage
from playwright.sync_api import expect # Ponecháme, pokud bys chtěl dělat specifické expecty, ale pro visible stačí BasePage

class LoginPage(BasePage):

    def load(self):
        self.navigate("https://www.motozem.cz/login/")
        self.accept_cookies()

    def invalid_login(self, email, password):
        # Použití self.fill z BasePage pro logování a zjednodušení selektoru (ID stačí)
        self.fill("#sUserLogin", email, name="Email")
        self.fill("#sUserPassword", password, name="Heslo")

        # Použití self.click z BasePage
        self.click(self.page.get_by_role("button", name="Přihlásit se"), name="Tlačítko Přihlásit")

        # Použití self.expect_visible z BasePage pro logování výsledku
        error_message = self.page.get_by_text("Zřejmě jste zadali špatné jmé")
        self.expect_visible(error_message, name="Chybová hláška přihlášení")