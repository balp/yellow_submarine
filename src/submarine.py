class Submarine:
    def __init__(self):
        self._position = 0
        self._aim = 0
        self._depth = 0
    @property
    def depth(self):
        return self._depth

    @property
    def position(self):
        return self._position

    @property
    def aim(self):
        return self._aim

    def execute(self, command: str):
        parsed = command.split()
        command_word = parsed[0]
        command_arg = int(parsed[1])

        if command_word == "forward":
            self._position += command_arg
            self._depth += command_arg * self._aim
        elif command_word == "up":
            self._aim -= command_arg
        else:
            self._aim += command_arg
