# ------------------------------------------------------------------
# 課題6-5：単体テスト対象のクラス
# ------------------------------------------------------------------
class Human:
    def __init__(self, name):
        self.name = name
    
    def call(self):
        str = 'My name is ' + self.name
        return str