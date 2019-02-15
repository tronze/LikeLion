from ..web_element import WebElement


class TheadElement(WebElement):

    THEAD = 'thead'

    def __init__(self):
        super().__init__(element_type=self.THEAD)
