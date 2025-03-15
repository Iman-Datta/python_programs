class Mark:
    def __init__(self, physics: int, chemistry: int, maths: int):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def display_mark(self):
        print(f"Physics: {self.physics}, Chemistry: {self.chemistry}, Maths: {self.maths}")

    def total(self) -> int:
        return self.physics + self.chemistry + self.maths
    
    def average(self) -> int:
        return self.total() / 3
