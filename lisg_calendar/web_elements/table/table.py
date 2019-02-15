from ..content import Content
from .th import ThElement
from .thead import TheadElement
from .tr import TrElement
from ..web_classes import WebClasses
from ..web_element import WebElement


class TableElement(WebElement):

    TABLE = 'table'

    def __init__(self):
        super().__init__(element_type=self.TABLE)

    def create_columns(self, columns: list, classnames: WebClasses = WebClasses()):
        classnames = classnames
        thead = TheadElement()
        tr = TrElement()
        for column in columns:
            th = ThElement()
            th.insert_node(Content(column))
            th.set_classnames(classnames)
            tr.insert_node(th)
        thead.insert_node(tr)
        self.insert_node(thead)
