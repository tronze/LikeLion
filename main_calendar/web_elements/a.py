from .web_element import WebElement


class AElement(WebElement):

    A = "a"

    def __init__(self):
        super().__init__(element_type=self.A)
        self.url = ""

    def set_href(self, url: str):
        self.url = url

    def create_element(self):
        head_lb = "<%s" % self.element_type
        head_property = self.get_element_properties()
        if len(self.url) > 0:
            head_property += " href='%s'" % self.url
        head_rb = ">"
        head = head_lb + head_property + head_rb
        tail = "</%s>" % self.element_type
        content = ""
        child_nodes = self.child_nodes
        for c_node in child_nodes:
            content += c_node.create_element()
        element = head + content + tail
        return element


