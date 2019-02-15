from .node import Node
from .web_classes import WebClasses


class WebElement(Node):

    def __init__(self, element_type):
        super().__init__()
        self.element_type = element_type
        self.content = ""
        self.classnames = WebClasses()
        self.child_nodes = list()

    def get_element_properties(self):
        classnames = self.classnames
        class_property = classnames.create_classnames_property()
        s = "".join
        if class_property is not "":
            class_property = " " + class_property
        return s(class_property)

    def set_classnames(self, classnames: WebClasses):
        self.classnames = classnames

    def insert_node(self, node: Node):
        if self.child_nodes is not None:
            self.child_nodes.append(node)

    def create_element(self):
        head_lb = "<%s" % self.element_type
        head_property = self.get_element_properties()
        head_rb = ">"
        head = head_lb + head_property + head_rb
        tail = "</%s>" % self.element_type
        content = ""
        child_nodes = self.child_nodes
        for c_node in child_nodes:
            content += c_node.create_element()
        element = head + content + tail
        return element
