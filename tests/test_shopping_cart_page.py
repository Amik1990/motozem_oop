from pages import ShoppingCartPage


def test_add_to_shopping_cart(load_shopping_cart_page: ShoppingCartPage):
    load_shopping_cart_page.add_to_shopping_cart()


def test_change_amount_in_shopping_cart(load_shopping_cart_page):
    load_shopping_cart_page.change_amount_in_shopping_cart()
