from state_machine import StateMachine, State


class DoorStatus:
    DOOR_OPEN = 0
    DOOR_CLOSED = 1


class Door:
    def __init__(self, label):
        self._label = label
        self._status = DoorStatus.DOOR_CLOSED

    def close_door(self):
        self._status = DoorStatus.DOOR_CLOSED

    def open_door(self):
        self._status = DoorStatus.DOOR_OPEN


class CompressorStatus:
    COMPRESSOR_OFF = 0
    COMPRESSOR_ON = 1


class CompressorDirection:
    COMPRESSOR_BLOW = 0
    COMPRESSOR_SUCK = 1


class Compressor:

    def __init__(self, label):
        self._label = label
        self._status = CompressorStatus.COMPRESSOR_OFF
        self._direction = CompressorDirection.COMPRESSOR_SUCK


class Gas:
    O2 = 0
    N2 = 1


class GasSensor:

    def __init__(self):
        self._pressure = 90


class Idle(State):

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    pass
