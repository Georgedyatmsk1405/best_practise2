class IgnoreExceptions:
    def __init__(self, exceptions: tuple):
        self.exception = exceptions

    def __enter__(self):
        yield

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exception:
            return True
        return 

