class NotFoundException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        print('calling str in custom exception')
        if self.message:
            return 'NotFoundException, {0} '.format(self.message)
        else:
            return 'NotFoundException has been raised'

raise NotFoundException("I'm a test")