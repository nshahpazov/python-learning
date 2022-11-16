class Base:
    def foo(self):
        return self.bar()


old_bc = __build_class__


def bc(fun, name, base=None, **kwargs):
    print("Building:")
    if base is Base:
        print("Check if this is base class")
    if base is not None:
        return old_bc(fun, name, base, **kwargs)
    return old_bc(fun, name, **kwargs)


import builtins

builtins.__build_class__ = bc