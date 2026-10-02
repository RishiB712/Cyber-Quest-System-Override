from project import create_bar, calculate_value, check_battle_status
def test_create_bar():
    assert create_bar(50, 100)=="[██████████----------] 50/100"
    assert create_bar(100, 100)=="[████████████████████] 100/100"
    assert create_bar(-10, 100)=="[--------------------] 0/100"
    assert create_bar(60, 50)=="[████████████████████] 60/50"
def test_calculate_value():
    for _ in range(20):
        assert 10<=calculate_value('strike')<=15
        assert 5<=calculate_value('hack')<=25
        assert 15<=calculate_value('patch')<=20
        assert 10<=calculate_value('boss_attack')<=18
        assert 40<=calculate_value('ultimate')<=50
    assert calculate_value('invalid_move')==0
def test_check_battle_status():
    assert check_battle_status(100, 150)=="continue"
    assert check_battle_status(0, 150)=="lose"
    assert check_battle_status(50, 0)=="win"
    assert check_battle_status(0, 0)=="lose"
