# python-samp
>  Python library for interfacing with San Andreas Multiplayer using memory

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

username = api.getUsername()
api.sendChat(username)
```