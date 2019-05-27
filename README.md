# PySnooper を標準出力ではなく、Python 文字列として取得する方法

- python: 3.7.2
- PySnooper: 0.0.39


# やってみる

PySnooper はインストール済みと仮定します。

1. `git clone git@github.com:furuuchitakahiro/get-PySnooper-string.git`
2. `cd get-PySnooper-string`
3. `python get_pysnooper_string.py`

**結果**

```
New var:....... ws = <__main__.MyWritableStream object at 0x7fcadd2944e0>
09:51:49.678454 line         7         num1 = 1
New var:....... num1 = 1
09:51:49.681886 line         8         num2 = 2
New var:....... num2 = 2
09:51:49.681952 line         9         result = num1 + num2
```
