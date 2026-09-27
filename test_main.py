from main import same_object, find_range

def test_known_range():
    """Эталонный ответ задачи."""
    assert find_range() == (5, 256)

def test_boundaries():
    """Границы кэша: -5, 256 - ещё в кэше; -6, 257 - уже нет."""
    assert same_object(-5) is True
    assert same_object(256) is True
    assert same_object(-6) is False
    assert same_object(257) is False