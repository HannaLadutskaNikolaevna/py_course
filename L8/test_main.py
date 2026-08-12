from main import hpwmanyletters


def test_no_letters():
    assert hpwmanyletters("") == "no data"


def test_less_than_3_letters():
    assert hpwmanyletters("NO") == "less three letters!"


def test_more_than_or_3_letters():
    assert hpwmanyletters("lol :)") == ["lol", ":)"]