import pytest
import calc

def test_soma():
    assert calc.soma(2, 3) == 5

def test_subtracao():
    assert calc.subtracao(10, 5) == 5

def test_multiplicacao():
    assert calc.multiplicacao(4, 3) == 12

def test_divisao():
    assert calc.divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        calc.divisao(5, 0)
