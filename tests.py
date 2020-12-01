from app import is_alive_host


def test_live():
    assert is_alive_host('semrush.com')


def test_down():
    assert not is_alive_host('invalid.domain.son')


def test_invalid_url():
    assert not is_alive_host('')


def test_404():
    assert not is_alive_host('app.drom.ru')
