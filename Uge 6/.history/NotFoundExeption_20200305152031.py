class NotFoundException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]