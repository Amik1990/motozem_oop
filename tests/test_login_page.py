import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "email, password", [("zubnicentrum@gmail.com", "zubnikaz5"), ("neplatny@email.cz", "spatneheslo123"), ("admin@motozem.cz", "123456")]
)
def test_invalid_login(load_login_page: LoginPage, email, password):
    """
    Testuje neúspěšné přihlášení s několika pevně danými kombinacemi.
    """
    load_login_page.invalid_login(email, password)


def test_invalid_login_random_data(load_login_page: LoginPage, fake):
    """
    Testuje neúspěšné přihlášení s NÁHODNĚ vygenerovanými daty (Faker).
    Tím ověříme robustnost formuláře pro různé formáty e-mailů a hesel.
    """
    # Vygenerujeme náhodná data
    for i in range(5):
        random_email = fake.email()
        random_password = fake.password(length=12)
        print(f"Pokus {i+1}: {random_email} / {random_password}")

        # Provedeme test
        load_login_page.invalid_login(random_email, random_password)
