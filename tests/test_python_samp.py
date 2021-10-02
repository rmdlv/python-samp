from python_samp import SAMP, API, Misc

samp = SAMP()
api = API(samp)
misc = Misc(samp)


def test_get_username():
    username = api.get_username()
    assert username == "Python_Samp"


def test_get_jetpack():
    misc.get_jetpack()
