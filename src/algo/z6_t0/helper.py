from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    a_up, b_down = (f1.numer, f1.denom)
    c_up, d_down = (f2.numer, f2.denom)
    if(f1.denom == f2.denom):
        result_up = (a_up+c_up)
        result_down = b_down
        return Fraction(result_up, result_down)
    else:
        result_up = ((a_up * d_down) + (b_down * c_up))
        result_down = (b_down * d_down)
        return Fraction(result_up, result_down)
