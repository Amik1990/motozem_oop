from pages import MotozemDobraPage


def test_lokace_dobra(load_motozem_dobra: MotozemDobraPage):
    load_motozem_dobra.lokace_dobra_google_maps_open()
