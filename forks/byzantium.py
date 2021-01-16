from .spurious_dragon import SpuriousDragon
from opcodes.opcode import Opcode

class Byzantium(SpuriousDragon):
    STOP = Opcode('STOP', 0, 0x00)
    ADD = Opcode('ADD', 3, 0x01)
    MUL = Opcode('MUL', 5, 0x02)
    SUB = Opcode('SUB', 3, 0x03)
    DIV = Opcode('DIV', 5, 0x04)
    SDIV = Opcode('SDIV', 5, 0x05)
    MOD = Opcode('MOD', 5, 0x06)
    SMOD = Opcode('SMOD', 5, 0x07)
    ADDMOD = Opcode('ADDMOD', 8, 0x08)
    MULMOD = Opcode('MULMOD', 8, 0x09)
    EXP = Opcode('EXP', 10, 0x0a)
    SIGNEXTEND = Opcode('SIGNEXTEND', 5, 0x0b)
    LT = Opcode('LT', 3, 0x10)
    GT = Opcode('GT', 3, 0x11)
    SLT = Opcode('SLT', 3, 0x12)
    SGT = Opcode('SGT', 3, 0x13)
    EQ = Opcode('EQ', 3, 0x14)
    ISZERO = Opcode('ISZERO', 3, 0x15)
    AND = Opcode('AND', 3, 0x16)
    OR = Opcode('OR', 3, 0x17)
    XOR = Opcode('XOR', 3, 0x18)
    NOT = Opcode('NOT', 3, 0x19)
    BYTE = Opcode('BYTE', 3, 0x1a)
    SHA3 = Opcode('SHA3', 30, 0x20)
    ADDRESS = Opcode('ADDRESS', 2, 0x30)
    BALANCE = Opcode('BALANCE', 400, 0x31)
    ORIGIN = Opcode('ORIGIN', 2, 0x32)
    CALLER = Opcode('CALLER', 2, 0x33)
    CALLVALUE = Opcode('CALLVALUE', 2, 0x34)
    CALLDATALOAD = Opcode('CALLDATALOAD', 3, 0x35)
    CALLDATASIZE = Opcode('CALLDATASIZE', 2, 0x36)
    CALLDATACOPY = Opcode('CALLDATACOPY', 3, 0x37)
    CODESIZE = Opcode('CODESIZE', 2, 0x38)
    CODECOPY = Opcode('CODECOPY', 3, 0x39)
    GASPRICE = Opcode('GASPRICE', 2, 0x3a)
    EXTCODESIZE = Opcode('EXTCODESIZE', 700, 0x3b)
    EXTCODECOPY = Opcode('EXTCODECOPY', 700, 0x3c)
    BLOCKHASH = Opcode('BLOCKHASH', 20, 0x40)
    COINBASE = Opcode('COINBASE', 2, 0x41)
    TIMESTAMP = Opcode('TIMESTAMP', 2, 0x42)
    NUMBER = Opcode('NUMBER', 2, 0x43)
    DIFFICULTY = Opcode('DIFFICULTY', 2, 0x44)
    GASLIMIT = Opcode('GASLIMIT', 2, 0x45)
    POP = Opcode('POP', 2, 0x50)
    MLOAD = Opcode('MLOAD', 3, 0x51)
    MSTORE = Opcode('MSTORE', 3, 0x52)
    MSTORE8 = Opcode('MSTORE8', 3, 0x53)
    SLOAD = Opcode('SLOAD', 200, 0x54)
    SSTORE = Opcode('SSTORE', 0, 0x55)
    JUMP = Opcode('JUMP', 8, 0x56)
    JUMPI = Opcode('JUMPI', 10, 0x57)
    PC = Opcode('PC', 2, 0x58)
    MSIZE = Opcode('MSIZE', 2, 0x59)
    GAS = Opcode('GAS', 2, 0x5a)
    JUMPDEST = Opcode('JUMPDEST', 1, 0x5b)
    PUSH1 = Opcode('PUSH1', 3, 0x60)
    PUSH2 = Opcode('PUSH2', 3, 0x61)
    PUSH3 = Opcode('PUSH3', 3, 0x62)
    PUSH4 = Opcode('PUSH4', 3, 0x63)
    PUSH5 = Opcode('PUSH5', 3, 0x64)
    PUSH6 = Opcode('PUSH6', 3, 0x65)
    PUSH7 = Opcode('PUSH7', 3, 0x66)
    PUSH8 = Opcode('PUSH8', 3, 0x67)
    PUSH9 = Opcode('PUSH9', 3, 0x68)
    PUSH10 = Opcode('PUSH10', 3, 0x69)
    PUSH11 = Opcode('PUSH11', 3, 0x6a)
    PUSH12 = Opcode('PUSH12', 3, 0x6b)
    PUSH13 = Opcode('PUSH13', 3, 0x6c)
    PUSH14 = Opcode('PUSH14', 3, 0x6d)
    PUSH15 = Opcode('PUSH15', 3, 0x6e)
    PUSH16 = Opcode('PUSH16', 3, 0x6f)
    PUSH17 = Opcode('PUSH17', 3, 0x70)
    PUSH18 = Opcode('PUSH18', 3, 0x71)
    PUSH19 = Opcode('PUSH19', 3, 0x72)
    PUSH20 = Opcode('PUSH20', 3, 0x73)
    PUSH21 = Opcode('PUSH21', 3, 0x74)
    PUSH22 = Opcode('PUSH22', 3, 0x75)
    PUSH23 = Opcode('PUSH23', 3, 0x76)
    PUSH24 = Opcode('PUSH24', 3, 0x77)
    PUSH25 = Opcode('PUSH25', 3, 0x78)
    PUSH26 = Opcode('PUSH26', 3, 0x79)
    PUSH27 = Opcode('PUSH27', 3, 0x7a)
    PUSH28 = Opcode('PUSH28', 3, 0x7b)
    PUSH29 = Opcode('PUSH29', 3, 0x7c)
    PUSH30 = Opcode('PUSH30', 3, 0x7d)
    PUSH31 = Opcode('PUSH31', 3, 0x7e)
    PUSH32 = Opcode('PUSH32', 3, 0x7f)
    DUP1 = Opcode('DUP1', 3, 0x80)
    DUP2 = Opcode('DUP2', 3, 0x81)
    DUP3 = Opcode('DUP3', 3, 0x82)
    DUP4 = Opcode('DUP4', 3, 0x83)
    DUP5 = Opcode('DUP5', 3, 0x84)
    DUP6 = Opcode('DUP6', 3, 0x85)
    DUP7 = Opcode('DUP7', 3, 0x86)
    DUP8 = Opcode('DUP8', 3, 0x87)
    DUP9 = Opcode('DUP9', 3, 0x88)
    DUP10 = Opcode('DUP10', 3, 0x89)
    DUP11 = Opcode('DUP11', 3, 0x8a)
    DUP12 = Opcode('DUP12', 3, 0x8b)
    DUP13 = Opcode('DUP13', 3, 0x8c)
    DUP14 = Opcode('DUP14', 3, 0x8d)
    DUP15 = Opcode('DUP15', 3, 0x8e)
    DUP16 = Opcode('DUP16', 3, 0x8f)
    SWAP1 = Opcode('SWAP1', 3, 0x90)
    SWAP2 = Opcode('SWAP2', 3, 0x91)
    SWAP3 = Opcode('SWAP3', 3, 0x92)
    SWAP4 = Opcode('SWAP4', 3, 0x93)
    SWAP5 = Opcode('SWAP5', 3, 0x94)
    SWAP6 = Opcode('SWAP6', 3, 0x95)
    SWAP7 = Opcode('SWAP7', 3, 0x96)
    SWAP8 = Opcode('SWAP8', 3, 0x97)
    SWAP9 = Opcode('SWAP9', 3, 0x98)
    SWAP10 = Opcode('SWAP10', 3, 0x99)
    SWAP11 = Opcode('SWAP11', 3, 0x9a)
    SWAP12 = Opcode('SWAP12', 3, 0x9b)
    SWAP13 = Opcode('SWAP13', 3, 0x9c)
    SWAP14 = Opcode('SWAP14', 3, 0x9d)
    SWAP15 = Opcode('SWAP15', 3, 0x9e)
    SWAP16 = Opcode('SWAP16', 3, 0x9f)
    LOG0 = Opcode('LOG0', 375, 0xa0)
    LOG1 = Opcode('LOG1', 375, 0xa1)
    LOG2 = Opcode('LOG2', 375, 0xa2)
    LOG3 = Opcode('LOG3', 375, 0xa3)
    LOG4 = Opcode('LOG4', 375, 0xa4)
    CREATE = Opcode('CREATE', 32000, 0xf0)
    CALL = Opcode('CALL', 700, 0xf1)
    CALLCODE = Opcode('CALLCODE', 700, 0xf2)
    RETURN = Opcode('RETURN', 0, 0xf3)
    SELFDESTRUCT = Opcode('SELFDESTRUCT', 5000, 0xff)
    DELEGATECALL = Opcode('DELEGATECALL', 700, 0xf4)
    REVERT = Opcode('REVERT', 0, 0xfd)
    RETURNDATASIZE = Opcode('RETURNDATASIZE', 2, 0x3d)
    RETURNDATACOPY = Opcode('RETURNDATACOPY', 3, 0x3e)
    STATICCALL = Opcode('STATICCALL', 700, 0xfa)
