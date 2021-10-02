# python-samp
>  Python library for interfacing with San Andreas Multiplayer using memory

![GitHub repo size](https://img.shields.io/github/repo-size/rmdlv/python-samp?style=flat-square)
![GitHub issues by-label](https://img.shields.io/github/issues/rmdlv/python-samp/bug?style=flat-square)

## Installation
You can install the latest version with the command:
```shell
pip install -U https://github.com/rmdlv/python-samp/archive/refs/heads/main.zip
```

## High-level example
```python
from python_samp import SAMP, API

samp = SAMP()
api = API(samp)

username = api.get_username()
api.send_chat(f"My name is {username}")
samp.close()
```

## Low-level example
```python
from python_samp import SAMP

samp = SAMP()

username = samp.process.read_string(samp.module + 0x219A6F)
data = f"My name is {username}"
address = samp.process.allocate(len(data))
samp.process.write_string(address, data)
samp.process.start_thread(samp.module + 0x57F0, address)
samp.process.free(address)
samp.close()
```

## Miscellaneous example
```python
from python_samp import SAMP, Misc

samp = SAMP()
misc = Misc(samp)

misc.coordmaster(316.0837, -1376.215, 31.92003)
samp.close()
```

## Contributing
Pull requests are supported! Before creating a pull request, read [CONTRIBUTING.md](https://github.com/rmdlv/python-samp/blob/main/CONTRIBUTING.md). We are pleased to see your contribution to the development of the library. Ask questions in the Issues section and in [**Telegram chat**](https://t.me/python_samp)!

## License
Copyright © 2021 [rmdlv](https://github.com/rmdlv).\
This project has a [MIT](https://github.com/rmdlv/python-samp/blob/main/LICENSE) license.