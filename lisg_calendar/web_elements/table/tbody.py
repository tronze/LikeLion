from ..web_element import WebElement


class TbodyElement(WebElement):

    TBODY = 'tbody'

    def __init__(self):
        super().__init__(element_type=self.TBODY)
