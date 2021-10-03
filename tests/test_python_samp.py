from python_samp import SAMP, API, Misc

samp = SAMP()
api = API(samp)
misc = Misc(samp)


def test_get_local_scoreboard_data():
    data = api.get_local_scoreboard_data()
    username = data.name
    assert username == "Python_Samp"


def test_get_jetpack():
    misc.get_jetpack()
