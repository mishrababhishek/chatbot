from data import data

def get_intends():
    return data.intends

def get_query_with_intends():
    return data.querys

def one_hot_encode(index: int, length: int):
    encoded = [0] * length
    if index is None:
        return encoded
    encoded[index] = 1
    return encoded
    