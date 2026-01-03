@echo off
REM --- CO JE TENTO SOUBOR? ---
REM Toto je "zkratka" pro Windows.
REM Místo abyste museli otevírat terminál a psát příkaz "allure serve allure-results",
REM stačí na tento soubor dvakrát kliknout myší.
REM
REM Co to udělá:
REM 1. Vezme výsledky testů ze složky 'allure-results'.
REM 2. Vygeneruje z nich hezkou webovou stránku (report).
REM 3. Automaticky ji otevře ve vašem prohlížeči.

echo Generuji Allure report...
allure serve allure-results
pause