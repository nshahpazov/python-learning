class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __str__(self):
        return "Polynomial@{:#x}: {}".format(id(self), self.coeffs)
