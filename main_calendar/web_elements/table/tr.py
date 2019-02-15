from ..web_element import WebElement


class TrElement(WebElement):

    TR = 'tr'

    def __init__(self):
        super().__init__(element_type=self.TR)
