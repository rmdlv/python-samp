from python_samp import __version__, SAMP, API


def test_version():
    assert __version__ == "0.1.0"


def test_username():
    samp = SAMP()
    api = API(samp)
    data = api.getUsername()
    assert data == "Python_Samp"
