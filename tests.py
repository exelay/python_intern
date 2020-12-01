from app import is_alive_host


def test_live():
    """Check response if host is alive."""
    assert is_alive_host('semrush.com')


def test_down():
    """Checks response if the host is down."""
    assert not is_alive_host('invalid.domain.son')


def test_invalid_url():
    """Checks response if the hostname is empty."""
    assert not is_alive_host('')


def test_404():
    """Checks response if the host return 404 status."""
    assert not is_alive_host('app.drom.ru')
