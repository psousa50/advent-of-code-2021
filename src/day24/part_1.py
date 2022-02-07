from dataclasses import dataclass, field
from email.policy import default
from tabnanny import check
from typing import Optional
from unicodedata import numeric

from src.global_helpers import execute, read_input


@dataclass(frozen=True)
class Instruction:
    op_code: str
    op1: str
    op2: Optional[str | int]
    length: int = field(init=False, default=0)

    def __post_init__(self):
        object.__setattr__(self, "length", 2 if self.op2 is None else 3)

    def __repr__(self):
        return f"{self.op_code} {self.op1} {self.op2}"


def build_dict():
    return dict()


vars = ["w", "x", "y", "z"]


@dataclass()
class Alu:
    program: list[Instruction]
    inputs: list[int] = field(default_factory=list)
    ip: int = field(default=0)
    input_pointer: int = field(default=0)
    vars: dict[str, int] = field(default_factory=build_dict)

    def __post_init__(self):
        self.reset()

    def reset(self):
        self.vars["w"] = 0
        self.vars["x"] = 0
        self.vars["y"] = 0
        self.vars["z"] = 0
        self.ip = 0
        self.input_pointer = 0

    def __getitem__(self, var: str):
        return self.vars[var]

    def __setitem__(self, var: str, value):
        self.vars[var] = value

    def input(self):
        v = self.inputs[self.input_pointer]
        self.input_pointer += 1
        return v

    def value(self, op: str | int | None):
        return op if isinstance(op, int) else self.vars[op] if op is not None else 0

    def execute(self, i: Instruction):
        match i.op_code:
            case "inp":
                self.vars[i.op1] = self.input()
            case "add":
                self.vars[i.op1] += self.value(i.op2)
            case "mul":
                self.vars[i.op1] *= self.value(i.op2)
            case "div":
                self.vars[i.op1] //= self.value(i.op2)
            case "mod":
                self.vars[i.op1] %= self.value(i.op2)
            case "eql":
                self.vars[i.op1] = 1 if self.vars[i.op1] == self.value(i.op2) else 0

    def run(self, inputs: list[int]):
        self.reset()
        self.inputs = inputs
        for i in self.program:
            self.execute(i)
            # print(i, self["w"], self["x"], self["y"], self["z"])


def check_number(alu: Alu, number: int):
    inputs = [int(n) for n in list(f"{number:014}")]
    valid = False
    if not 0 in inputs:
        alu.run(inputs)
        valid = alu["z"] == 0
    return valid


def main():
    lines = read_input(24, 1)

    instructions: list[Instruction] = []
    for line in lines:
        [op_code, op1, op2] = (line + " *").split(" ")[0:3]

        if not op2 in vars:
            op2 = None if op2 == "*" else int(op2)

        instruction = Instruction(op_code, op1, op2)

        instructions.append(instruction)

    for block in range(14):

        i = block * 18
        alu = Alu(instructions[i : i + 18])

        print(f"Block: {block + 1}:")
        for n in range(1, 10):
            alu.run([n])
            print(n, alu["z"])

    # c = 0
    # number = 11111111111111
    # while True:
    #     inputs = [int(n) for n in list(f"{number:014}")]
    #     if not 0 in inputs:
    #         alu.run(inputs)
    #         print(number, alu["z"])
    #     number += 1
    #     c += 1
    #     if c > 10000:
    #         break

    # numbers = [
    #     11111111111111,
    #     22222222222222,
    #     33333333333333,
    #     44444444444444,
    #     55555555555555,
    #     66666666666666,
    #     77777777777777,
    #     88888888888888,
    #     99999999999999,
    # ]
    # number = 11111111111111
    # for number in numbers:
    #     check_number(alu, number)

    #     print(number, alu["z"])

    return 0


if __name__ == "__main__":
    execute(main)
