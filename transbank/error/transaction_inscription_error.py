from transbank.error.transbank_error import TransbankError


class TransactionInscriptionError(TransbankError):
    def __init__(self, message="Inscription Transaction could not be performed. Please verify given parameters",
                 code=0):
        super().__init__(message, code)
