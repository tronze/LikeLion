class WebClasses:

    def __init__(self) -> None:
        super().__init__()
        self.classnames = []

    def get_classnames(self):
        classnames = self.classnames
        return classnames

    def add_classname(self, classname):
        classnames = self.get_classnames()
        if classname is not None and classname is not "" and self.classname_exist(classname) is False:
            classnames.append(classname)

    def remove_classname(self, classname):
        classnames = self.get_classnames()
        if self.classname_exist(classname):
            classnames.remove(classname)

    def classname_exist(self, classname):
        classnames = self.get_classnames()
        return classname in classnames

    def create_classnames_property(self):
        classnames = self.get_classnames()
        if len(classnames) is 0:
            return ""
        prefix = "class=\""
        postfix = "\""
        class_properties = ""
        for classname in classnames:
            if class_properties is "":
                class_properties = classname
            else:
                class_properties += " " + classname
        return prefix + class_properties + postfix
