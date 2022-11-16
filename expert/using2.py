from meta_classes import Base2


class Derived(Base2):
    def bar(self):
        return "bar"


d = Derived()
# d.bar()
