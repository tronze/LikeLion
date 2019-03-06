from .web_element import WebElement


class H1Element(WebElement):

    H1 = "h1"

    def __init__(self):
        super().__init__(element_type=self.H1)
