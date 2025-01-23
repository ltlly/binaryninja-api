
from . import MediumLevelILInstruction, LowLevelILInstruction, HighLevelILInstruction


class ILSourceLocation:
    def __init__(self, address=None, sourceOperand=None):
        self.address = address
        self.sourceOperand = sourceOperand
        self.valid = False

    @classmethod
    def from_address_operand(cls, address, operand):
        instance = cls(address, operand)
        instance.valid = True
        return instance

    @classmethod
    def from_instruction(
        cls,
        instr: MediumLevelILInstruction
        | LowLevelILInstruction
        | HighLevelILInstruction,
    ) -> "ILSourceLocation":
        instance = cls(instr.address, instr.source_operand)
        instance.valid = True
        return instance
