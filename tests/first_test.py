from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multuply_calc_corr(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calc_corr(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_substraction_calc_corr(self):
        assert self.calc.substraction(self, 3, 2) == 1

    def test_adding_calc_corr(self):
        assert self.calc.adding(self, 4, 2) == 6
