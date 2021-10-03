from python_samp import SAMP, API, Misc

samp = SAMP()
api = API(samp)
misc = Misc(samp)


def test_get_local_scoreboard_data():
    scoreboard = api.get_local_scoreboard_data()
    assert scoreboard.name == "Python_Samp"


def test_get_jetpack():
    misc.get_jetpack()
