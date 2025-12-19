import sys                                  # Import modulu pro standardní vstup/výstup
from loguru import logger                   # Import pokročilé logovací knihovny

# --- Konfigurace Logování ---

logger.remove()                             # Odstranění defaultní konfigurace loggeru

# Přidání konfigurace pro logování do konzole (stderr)
logger.add(
    sys.stderr,                             # Cíl: Standardní chybový výstup (terminál)
    level="INFO",                           # Logovací úroveň pro konzoli (zobrazuje se INFO a vyšší)
    format="<green>{time:HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>", # Formát s barvami
    colorize=True                           # Zapnutí barevného výstupu
)

# Přidání konfigurace pro logování do souboru (pro detailní audit)
logger.add(
    "test_execution.log",                   # Název souboru
    level="DEBUG",                          # Logovací úroveň pro soubor (nejnižší, zaznamená vše)
    rotation="5 MB",                        # Soubor se otočí po 5 MB
    compression="zip",                      # Staré soubory budou zkomprimovány
    enqueue=True,                           # Zajistí thread-safe logování, důležité pro paralelní testy
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}"
)

def get_logger(name):
    """Vrátí logger s kontextovým jménem (např. název třídy/modulu)."""
    return logger.bind(name=name)           # Používá bind pro přidání kontextové proměnné 'name'