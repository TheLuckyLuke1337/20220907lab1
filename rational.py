from dataclasses import dataclass

@dataclass
class Rational:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator
