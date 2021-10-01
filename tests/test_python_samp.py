from python_samp import SAMP, API


def test_username():
    samp = SAMP()
    api = API(samp)
    username = api.get_username()
    assert username == "Python_Samp"
