from ...tx.script import errno
from ...tx.script import ScriptError
from ...tx.script.flags import SIGHASH_FORKID

from ..bitcoin.SolutionChecker import BitcoinSolutionChecker

class BCashSolutionChecker(BitcoinSolutionChecker):
    sighash_forkid = SIGHASH_FORKID
    def signature_hash(self, tx_out_script, unsigned_txs_out_idx, hash_type, **kw):
        """
        Return the canonical hash for a transaction. We need to
        remove references to the signature, since it's a signature
        of the hash before the signature is applied.

        tx_out_script: the script the coins for unsigned_txs_out_idx are coming from
        unsigned_txs_out_idx: where to put the tx_out_script
        hash_type: one of SIGHASH_NONE, SIGHASH_SINGLE, SIGHASH_ALL,
        optionally bitwise or'ed with SIGHASH_ANYONECANPAY
        """
        if hash_type & SIGHASH_FORKID != SIGHASH_FORKID:
            raise ScriptError()
        return self.signature_for_hash_type_segwit(tx_out_script, unsigned_txs_out_idx, hash_type)
