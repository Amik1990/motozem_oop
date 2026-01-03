from pages.base_page import BasePage
from utils.config import config


class LoginPage(BasePage):
    """
    Třída reprezentující přihlašovací stránku Motozem.
    """

    def load(self) -> None:
        """
        Načte přihlašovací stránku a potvrdí cookies.
        """
        self.navigate(f"{config.BASE_URL}/login/")
        self.accept_cookies()

    def invalid_login(self, email: str, password: str) -> None:
        """
        Provede pokus o přihlášení s neplatnými údaji a ověří chybovou hlášku.

        Args:
            email: E-mailová adresa uživatele.
            password: Heslo uživatele.
        """
        prihlasit_se = self.page.get_by_role("button", name="Přihlásit se")
        email_input = self.page.locator("section").filter(has_text="Přihlášení uživatele pomocí e").locator("#sUserLogin")
        password_input = self.page.locator("section").filter(has_text="Přihlášení uživatele pomocí e").locator("#sUserPassword")
        error_message = self.page.get_by_text("Zřejmě jste zadali špatné jmé")

        self.fill(email_input, email, name="E-mail input")
        self.fill(password_input, password, name="Password input")
        self.click_and_wait_for_response(
            prihlasit_se, r"(?i)login|prihlaseni", name="Tlačítko Přihlásit se"
        )  # (?i) bude brát v potaz velká i malá písmena
        self.expect_visible(error_message, name="Chybová hláška neplatného přihlášení")
