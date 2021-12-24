# ------------------------------------------------------------------
# 課題6-5：単体テスト用の関数
# ------------------------------------------------------------------
from main import Human

def test_init():
    human = Human('Tanaka')
    assert human.name == 'Tanaka'
    
def test_type_call():
    human = Human('Yamada')
    assert type(human.call()) == str
    
def test_var_call():
    human = Human('Sato')
    assert human.call() == 'My name is Sato'