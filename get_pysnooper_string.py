import pysnooper


def example_func():
    ws = MyWritableStream()
    with pysnooper.snoop(output=ws):
        num1 = 1
        num2 = 2
        result = num1 + num2
    print(ws.dump_message)  # ws.dump_message で文字列として取得できる


class MyWritableStream(pysnooper.utils.WritableStream):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dump_message = ''

    def write(self, s: str) -> None:
        self.dump_message += s


if __name__ == '__main__':
    example_func()
