class CounterList(list):
    """
    A list has a counter attribute (initially zero), which is incremented 
    each time you access a list element
    """

    def __init__(self, value):
        super().__init__(value)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)
