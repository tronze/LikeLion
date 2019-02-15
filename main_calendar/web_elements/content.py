from .node import Node


class Content(Node):

    def __init__(self, content):
        super().__init__()
        self.content = content

    def create_element(self):
        return self.content
