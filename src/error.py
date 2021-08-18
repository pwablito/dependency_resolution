class SoftwareNotFoundError(Exception):
    pass


class QueueEmptyError(Exception):
    pass


class CircularDependencyError(Exception):
    pass
