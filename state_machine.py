from __future__ import annotations


class State:

    def __init__(self, label):
        self._label = label
        self._backward = None
        self._forward = None
        self._can_switch_to = None
        self._state_machine = None

    def update(self, func, *args, **kwargs):
        func(*args, **kwargs)

    @property
    def label(self):
        return self._label

    @property
    def forward(self):
        return self._forward

    @forward.setter
    def forward(self, state: State):
        self._forward = state

    @property
    def backward(self):
        return self._backward

    @backward.setter
    def backward(self, state: State):
        self._backward = state

    @property
    def can_switch_to(self) -> tuple:
        return self._can_switch_to

    @can_switch_to.setter
    def can_switch_to(self, states: tuple):
        self._can_switch_to = states

    @property
    def state_machine(self):
        return self._state_machine

    @state_machine.setter
    def state_machine(self, state_machine: StateMachine):
        self._state_machine = state_machine


class StateMachine:

    def __init__(self):
        self._act_state = None
        self._states = {}

    @property
    def state(self):
        return self._act_state

    def add_state(self, state: State, is_initial=False):
        self._states[state.label] = state
        if is_initial:
            self._act_state = state

    def switch_to(self, label: str) -> bool:
        if label in [s.label for s in self._act_state.can_switch_to]:
            self._act_state.pause()
            self._act_state = self._states.get(label)
            self._act_state.resume()
            return True
        return False

    def switch_forward(self):
        if self._act_state.forward:
            self.switch_to(self._act_state.forward.label)

    def switch_backward(self):
        if self._act_state.backward:
            self.switch_to(self._act_state.backward.label)

    def start(self):
        for s in self._states:
            s.start()

    def stop(self):
        for s in self._states:
            s.stop()

    def update(self, *args, **kwargs):
        if self._act_state:
            self._act_state.update(*args, **kwargs)

