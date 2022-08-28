def check_index(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integar. If is not an integer, 
    a TypeError is raised; if it is negative, an IndexError is raised (since the 
    sequence is of infinite length).
    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence. 
        start --- the first value in the sequence
        step --- the difference between two adjacent values
        changed --- a dictionary of values that have been modified by the user
        """
        self.start = start      # store the start value
        self.step = step        # store the step value
        self.changed = {}       # no items have been modified

    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence
        """
        check_index(key)

        try:
            return self.changed[key]                # modified?
        except KeyError:                             # otherwise
            return self.start + key * self.step      # calculate the value

    def __setitem__(self, key, value):
        """
        Chang an item in the arithmetic sequence.
        """
        check_index(key)

        self.changed[key] = value    # store the changed value
