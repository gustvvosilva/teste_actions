import pytest
import meu_codigo

def test_soma():
    assert meu_codigo.soma(2, 3) == 5

def test_subtracao():
    assert meu_codigo.subtracao(10, 5) == 5

def test_multiplicacao():
    assert meu_codigo.multiplicacao(4, 3) == 12

def test_divisao():
    assert meu_codigo.divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        meu_codigo.divisao(5, 0)
