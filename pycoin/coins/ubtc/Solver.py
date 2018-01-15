from ..hardfork.Solver import HardforkSolver
from ...tx.script.flags import SIGHASH_FORKID, SIGHASH_ALL

from .SolutionChecker import UBTCSolutionChecker

class UBTCSolver(HardforkSolver):
    SolutionChecker = UBTCSolutionChecker

    # def solve(self, *args, **kwargs):
    #     if kwargs.get("hash_type") is None:
    #         kwargs["hash_type"] = SIGHASH_ALL
    #     kwargs["hash_type"] |= UBTC_SIGHASH_FORKID
    #     print('add hash type', UBTC_SIGHASH_FORKID)
    #     return super(HardforkSolver, self).solve(*args, **kwargs)
