from src.phone import Phone

test_item = Phone("Samsung S24 Ultra", 150_000, 10, 5)


def test__repr__():
    assert repr(test_item) == "Phone('Samsung S24 Ultra', 150000, 10, 5)"
