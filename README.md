# python-samp
>  Python library for interfacing with San Andreas Multiplayer using memory

![GitHub repo size](https://img.shields.io/github/repo-size/rmdlv/python-samp?style=flat-square)
![GitHub issues by-label](https://img.shields.io/github/issues/rmdlv/python-samp/bug?style=flat-square)

## Installation
You can install the latest version with the command:
```shell
pip install -U https://github.com/rmdlv/python-samp/archive/refs/heads/main.zip
```

## Example
```python
from python_samp import SAMP, API

samp = SAMP()
api = API(samp)

username = api.get_username()
api.send_chat(f"My name is {username}")
samp.close()
```

## Contributing
Pull requests are supported! Before creating a pull request, read [CONTRIBUTING.md](https://github.com/rmdlv/python-samp/blob/main/CONTRIBUTING.md). We are pleased to see your contribution to the development of the library. Ask questions in the Issues section and in [**Telegram chat**](https://t.me/python_samp)!

## License
Copyright © 2021 [rmdlv](https://github.com/rmdlv).\
This project has a [MIT](https://github.com/rmdlv/python-samp/blob/main/LICENSE) license.