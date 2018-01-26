import binascii


def bytes32(string):
    """
    Convert string to bytes32 data type for smart contract

    Parameters
    ----------
    string: str

    Returns
    -------
    list

    """
    return binascii.hexlify(string.encode('utf-8'))


def b32_str(bytes32):
    """
    Convert bytes32 to string

    Parameters
    ----------
    input: bytes object

    Returns
    -------
    str

    """
    return binascii.hexlify(bytes32.decode('utf-8'))
