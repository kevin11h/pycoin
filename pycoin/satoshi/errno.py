OK = 0
UNKNOWN_ERROR = 1
EVAL_FALSE = 2
OP_RETURN = 3

# Max sizes
SCRIPT_SIZE = 4
PUSH_SIZE = 5
OP_COUNT = 6
STACK_SIZE = 7
SIG_COUNT = 8
PUBKEY_COUNT = 9

# Failed verify operations
VERIFY = 10
EQUALVERIFY = 11
CHECKMULTISIGVERIFY = 12
CHECKSIGVERIFY = 13
NUMEQUALVERIFY = 14

# Logical/Format/Canonical errors
BAD_OPCODE = 15
DISABLED_OPCODE = 16
INVALID_STACK_OPERATION = 17
INVALID_ALTSTACK_OPERATION = 18
UNBALANCED_CONDITIONAL = 19

# CHECKLOCKTIMEVERIFY and CHECKSEQUENCEVERIFY
NEGATIVE_LOCKTIME = 20
UNSATISFIED_LOCKTIME = 21

# Malleability
SIG_HASHTYPE = 22
SIG_DER = 23
MINIMALDATA = 24
SIG_PUSHONLY = 25
SIG_HIGH_S = 26
SIG_NULLDUMMY = 27
PUBKEYTYPE = 28
CLEANSTACK = 29
MINIMALIF = 30
NULLFAIL = 31

# softfork safeness
DISCOURAGE_UPGRADABLE_NOPS = 32
DISCOURAGE_UPGRADABLE_WITNESS_PROGRAM = 33

# segregated witness
WITNESS_PROGRAM_WRONG_LENGTH = 34
WITNESS_PROGRAM_WITNESS_EMPTY = 35
WITNESS_PROGRAM_MISMATCH = 36
WITNESS_MALLEATED = 37
WITNESS_MALLEATED_P2SH = 38
WITNESS_UNEXPECTED = 39
WITNESS_PUBKEYTYPE = 40

ERROR_COUNT = 41
