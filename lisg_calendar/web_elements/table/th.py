from ..web_element import WebElement


class ThElement(WebElement):

    TH = 'th'

    def __init__(self):
        super().__init__(element_type=self.TH)
