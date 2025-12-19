from playwright.sync_api import Page  # Import typu Page pro nápovědu
from utils.logger_config import get_logger  # Import našeho loggeru

LOG = get_logger("FixtureUtils")  # Inicializace loggeru


def setup_page(PageClass, page: Page):
    """
    Univerzální logika pro přípravu jakékoliv stránky.
    Oddělená od conftest.py pro lepší přehlednost.
    """
    class_name = PageClass.__name__  # Dynamické získání názvu třídy
    LOG.info(f"--- SETUP: Inicializace {class_name} ---")  # Logování startu

    try:
        instance = PageClass(page)  # Vytvoření instance (např. HomePage(page))
        instance.load()  # Zavolání metody load() stránky
        LOG.success(f"FIXTURE: {class_name} připravena.")  # Logování úspěchu
        return instance  # Vrácení připraveného objektu

    except Exception as e:
        # Centrální ošetření chyb pro všechny fixtury
        LOG.error(f"SELHÁNÍ SETUPU: Stránka {class_name} se nenačetla.")
        LOG.error(f"Detail: {str(e)}")

        # Automatický screenshot při selhání jakékoliv fixtury
        screenshot_path = f"screenshots/setup_fail_{class_name}.png"
        page.screenshot(path=screenshot_path)

        raise e  # Vyhození chyby dál