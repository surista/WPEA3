import pytest
from week_4 import Room, House, NotEnoughSpaceError, Neighborhood


def test_empty_house():
    h = House()
    assert h.size() == 0
    assert h.available_space == 100


def test_zero_size_house_add_room():
    h = House(0)
    assert h.available_space == 0
    bedroom = Room('bedroom', 10)

    with pytest.raises(NotEnoughSpaceError):
        h.add_rooms(bedroom)


def test_small_house_add_equal_then_more():
    h = House(15)
    assert h.available_space == 15
    bedroom = Room('bedroom', 15)
    h.add_rooms(bedroom)
    assert h.size() == 15
    assert h.available_space == 15

    tiny_room = Room('very small closet', 0.01)
    with pytest.raises(NotEnoughSpaceError):
        h.add_rooms(tiny_room)


def test_small_house():
    h = House()
    bedroom = Room('bedroom', 10)
    kitchen = Room('kitchen', 9)
    bathroom = Room('bathroom', 3)
    h.add_rooms(bedroom, kitchen, bathroom)

    assert h.size() == 22
    assert len(h.rooms) == 3
    assert str(h) == '''House:
bedroom, 10m
kitchen, 9m
bathroom, 3m'''


def test_palace():
    h = House(1000)

    for i in range(10):
        h.add_rooms(Room(f'bedroom {i}', 15))

    for i in range(5):
        h.add_rooms(Room(f'bathroom {i}', 3))

    for i in range(3):
        h.add_rooms(Room(f'kitchen {i}', 3))

    assert h.size() == 174
    assert len(h.rooms) == 18


def test_one_neighborhood():
    Neighborhood.total_size = 0
    n = Neighborhood()

    houses = []
    for i in range(3):
        h = House()
        bedroom = Room('bedroom', 10)
        kitchen = Room('kitchen', 9)
        bathroom = Room('bathroom', 3)
        h.add_rooms(bedroom, kitchen, bathroom)
        houses.append(h)

    n.add_houses(*houses)
    assert n.size() == Neighborhood.total_size


def test_two_neighborhoods():
    Neighborhood.total_size = 0
    n1 = Neighborhood()
    n2 = Neighborhood()

    houses = []
    for i in range(3):
        h = House()
        bedroom = Room('bedroom', 10)
        kitchen = Room('kitchen', 9)
        bathroom = Room('bathroom', 3)
        h.add_rooms(bedroom, kitchen, bathroom)
        houses.append(h)

    n1.add_houses(*houses)
    n2.add_houses(*houses)

    assert n1.size() + n2.size() == Neighborhood.total_size