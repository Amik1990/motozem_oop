# 📘 Motozem OOP Test Automation - Průvodce projektem

Tento dokument slouží jako kompletní průvodce architekturou a fungováním automatizovaných testů pro projekt Motozem. Projekt využívá moderní technologie jako **Python, Playwright, Pytest, Allure a Jenkins**.

---

## 🏗️ Struktura Projektu

Projekt je organizován podle návrhového vzoru **Page Object Model (POM)**, který odděluje logiku testů od logiky ovládání stránky.

### 📂 Kořenová složka (`motozem_oop/`)
Hlavní řídící centrum projektu.

*   **📄 `.env`**
    *   **Co to je:** Konfigurační soubor s proměnnými prostředí.
    *   **Obsah:** `BASE_URL`, `BROWSER_HEADLESS` (true/false), `TIMEOUT`.
    *   **Účel:** Umožňuje měnit nastavení (např. přepnout na testovací prostředí) bez zásahu do kódu.
*   **📄 `Jenkinsfile`**
    *   **Co to je:** Definice CI/CD pipeline pro Jenkins (Pipeline as Code).
    *   **Účel:** Říká Jenkinsu, jak má stáhnout kód, nainstalovat závislosti, spustit testy a vygenerovat report.
*   **📄 `pyproject.toml`**
    *   **Co to je:** Moderní konfigurace pro Python nástroje.
    *   **Účel:** Nastavuje `pytest` (např. paralelní běh `-n auto`, Allure reporty). Nahrazuje starší `pytest.ini`.
*   **📄 `requirements.txt`**
    *   **Co to je:** Seznam závislostí.
    *   **Účel:** Používá se pro instalaci knihoven (`pip install -r requirements.txt`).
*   **📄 `report.bat`**
    *   **Co to je:** Spouštěcí skript pro Windows.
    *   **Účel:** Jedním kliknutím vygeneruje a otevře Allure report v prohlížeči.

---

### 📂 `pages/` (Page Objects)
Zde je definována logika ovládání webových stránek. Každá stránka má svou třídu.

*   **📄 `base_page.py`** (Rodičovská třída)
    *   Obsahuje společné metody pro všechny stránky: `click`, `fill`, `expect_visible`, `to_have_text`.
    *   Zajišťuje **logování** a **error handling** (např. výpis chyby do logu před pádem testu).
*   **📄 `home_page.py`, `login_page.py`, ...**
    *   Dědí z `BasePage`.
    *   Obsahují metody specifické pro danou stránku (např. `login()`, `add_to_cart()`).
    *   Používají konfiguraci z `utils/config.py`.

---

### 📂 `tests/` (Testy)
Zde jsou samotné testovací scénáře.

*   **📄 `conftest.py`**
    *   Obsahuje **Fixtures** (příprava před testem).
    *   Nastavuje prohlížeč (headless/headed) podle configu.
    *   Inicializuje Page Objecty a předává je do testů.
*   **📄 `test_*.py`** (např. `test_login.py`)
    *   Samotné testy.
    *   Volají metody z Page Objectů a ověřují výsledky (Assertions).

---

### 📂 `utils/` (Pomocné nástroje)
Nástroje pro podporu testování.

*   **📄 `config.py`**
    *   Načítá proměnné z `.env` souboru.
    *   Poskytuje je zbytku aplikace jako statické proměnné (např. `config.BASE_URL`).
*   **📄 `logger_config.py`**
    *   Nastavuje knihovnu `loguru`.
    *   Určuje formát logů a cestu k souboru (`logs/test_execution.log`).
*   **📄 `fixture_utils.py`**
    *   Pomocná funkce `setup_page`.
    *   Řeší navigaci na stránku a **automatické screenshoty** při selhání v `setup` fázi.

---

## 🔄 Tok Dat (Jak to funguje)

1.  **Spuštění:** Uživatel (nebo Jenkins) spustí `pytest`.
2.  **Konfigurace:** Pytest načte `pyproject.toml` (nastaví paralelní běh).
3.  **Setup:**
    *   Načte se `conftest.py`.
    *   `utils/config.py` načte hodnoty z `.env`.
    *   Spustí se prohlížeč.
4.  **Test:**
    *   Test si vyžádá stránku (např. `login_page`).
    *   `fixture_utils` vytvoří instanci stránky.
5.  **Akce:**
    *   Test volá metodu stránky (`login_page.login()`).
    *   Stránka volá `BasePage.fill()`.
    *   `BasePage` provede akci a zapíše ji do `logs/test_execution.log`.
6.  **Výsledek:**
    *   Data o průběhu se ukládají do `allure-results/`.
    *   Po skončení se vygeneruje HTML report.

---

## 🚀 Jak spustit projekt

### Lokálně (Příkazová řádka)
```bash
# Spuštění všech testů (paralelně)
pytest

# Spuštění konkrétního testu
pytest -k "login"

# Zobrazení reportu
report.bat
```

### CI/CD (Jenkins)
Projekt obsahuje `Jenkinsfile` pro automatické spouštění.
*   Pipeline se spustí automaticky při `git push` (pokud je nastaven Webhook nebo Polling).
*   Automaticky nainstaluje prostředí, spustí testy a vygeneruje Allure report.
