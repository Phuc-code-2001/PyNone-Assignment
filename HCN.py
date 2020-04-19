
class rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def get_chu_vi(self):
        return 2*(self.width + self.height)

    def get_dien_tich(self):
        return self.width*self.height

class square(rectangle):
    def __init__(self, width = 0):
        super().__init__(width= width, height= width)

    def get_chu_vi(self):
        return super().get_chu_vi()

    def get_dien_tich(self):
        return super().get_dien_tich()

a = square(5)

print(a.get_dien_tich())