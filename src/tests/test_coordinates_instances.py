import pytest

from objects import Area, BattleField, UObject, WrongInstance


def test_battle_field_4_4_is_16_areas(battle_field_4_4: BattleField) -> None:
    assert isinstance(battle_field_4_4, BattleField) is True
    assert len(battle_field_4_4.get_all_areas()) == 4
    assert len(battle_field_4_4.get_all_areas()[0]) == 4
    assert len(battle_field_4_4.get_all_areas()[1]) == 4
    assert len(battle_field_4_4.get_all_areas()[2]) == 4
    assert len(battle_field_4_4.get_all_areas()[3]) == 4


def test_check_areas_empty(battle_field_4_4: BattleField) -> None:
    areas = battle_field_4_4.get_all_areas()

    for y_areas in areas:
        for area in y_areas:
            assert area.all_objects_in() == []


def test_add_u_obj_to_area_once(battle_field_4_4: BattleField, u_object: UObject) -> None:
    first_area: Area = battle_field_4_4.get_all_areas()[0][0]
    first_area.add_object(u_object)

    assert u_object in first_area.all_objects_in()
    assert len(first_area.all_objects_in()) == 1


def test_add_u_obj_to_area_twice(battle_field_4_4: BattleField, u_object: UObject) -> None:
    first_area: Area = battle_field_4_4.get_all_areas()[0][0]
    first_area.add_object(u_object)
    first_area.add_object(u_object)

    assert u_object in first_area.all_objects_in()
    assert len(first_area.all_objects_in()) == 1


def test_add_u_obj_cant_add_bad_obj(battle_field_4_4: BattleField) -> None:
    first_area: Area = battle_field_4_4.get_all_areas()[0][0]
    wrong_u_object = 1
    with pytest.raises(WrongInstance):
        first_area.add_object(wrong_u_object)

    assert wrong_u_object not in first_area.all_objects_in()
    assert len(first_area.all_objects_in()) == 0
