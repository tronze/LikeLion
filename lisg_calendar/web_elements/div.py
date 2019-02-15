from .web_element import WebElement


class DivElement(WebElement):

    DIV = "div"

    def __init__(self):
        super().__init__(element_type=self.DIV)
