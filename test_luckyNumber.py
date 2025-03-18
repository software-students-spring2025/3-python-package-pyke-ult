"""test file"""

import random
import luckyNumber



def test_ask_color(monkeypatch):
    """test for ask_color with mock input"""
    monkeypatch.setattr('builtins.input', lambda _: " Blue ")
    assert luckyNumber.ask_color() == "Blue"





def test_generate_lucky_number():
    """"test for generate_lucky_number"""
    for _ in range(100):
        lucky_number = luckyNumber.generate_lucky_number()
        assert 1 <= lucky_number <= 9





def test_generate_lucky_number_boundaries():
    """test generate_luck_number boundaries (edge case)"""
    random.seed(0)
    assert 1 <= luckyNumber.generate_lucky_number() <= 9
