
def test_informace_is_present(load_header_page):
    load_header_page.informace_menu_is_visible_when_hover_over()

def test_informace_menu_content_is_present(load_header_page):
    load_header_page.informace_menu_content()

def test_prodejny_menu_is_visible(load_header_page):
    load_header_page.prodejny_menu_is_visible_when_hover_over()

def test_prodejny_menu_content_is_visible(load_header_page):
    load_header_page.prodejny_menu_content()

