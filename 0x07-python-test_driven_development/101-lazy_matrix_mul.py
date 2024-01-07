#!/usr/bin/python3
"""Matrix multiplication function using NumPy."""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Matrix multiplication function using NumPy.

    Args:
        m_a (list): First matrix represented as a list of lists.
        m_b (list): Second matrix represented as a list of lists.

    Raises:
        ValueError: If matrices cannot be multiplied due to incompatible shapes or invalid data types.
        TypeError: If matrix parameters are not properly formatted or contain unsupported data types.

    Returns:
        list: Resultant matrix after multiplication.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b).tolist()
        return result
    except ValueError as ve:
        raise ValueError(f"shapes {np_a.shape} and {np_b.shape} not aligned: {np_a.shape[1]} (dim 1) != {np_b.shape[0]} (dim 0)") from ve
    except Exception as e:
        raise TypeError("Scalar operands are not allowed, use '*' instead") from e
