from ..web_element import WebElement


class TdElement(WebElement):

    TD = 'td'

    def __init__(self):
        super().__init__(element_type=self.TD)
