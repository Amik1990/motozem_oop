from playwright.sync_api import Page, expect
from playwright.sync_api import Locator
import re

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, element):
        element.click()

    def hover(self, element: Locator):
        element.hover()

    def expect_visible(self, element):
        expect(element).to_be_visible()

    def to_have_text(self, element):
        expect(element).to_have_text()

    def to_have_attribute(self, element):
        expect(element).to_have_attribute()

    def fill(self, element: Locator):
        element.fill("")