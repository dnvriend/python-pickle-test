from dataclasses import dataclass
import pickle


def test_pickle_dict():
    expected_dict: dict = {'name': 'dnvriend', 'age': 44}
    # Return the pickled representation of the object as a bytes object
    serialized: bytes = pickle.dumps(expected_dict, pickle.HIGHEST_PROTOCOL)
    # Read a pickled object hierarchy from a bytes object and return the reconstituted object hierarchy
    # and auto-detect the contained protocol version
    actual_dict: dict = pickle.loads(serialized)
    assert actual_dict == expected_dict


@dataclass
class Person:
    name: str
    age: int


def test_pickle_class():
    expected = Person('Dennis', 44)
    serialized: bytes = pickle.dumps(expected, pickle.HIGHEST_PROTOCOL)
    actual = pickle.loads(serialized)
    assert actual == expected
