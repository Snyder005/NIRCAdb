"""Errors and Exceptions for NIRCAdb Package.

This contains the code for user-defined Errors and Exceptions used by the
NIRCAdb Package.

"""

################################################################################
##
## NIRCAdb Exceptions and Errors
##
################################################################################

class Error(Exception):
    """Base class for other exceptions."""
    pass

class QueryError(Error):
    """Raised when a SQLite query returns an empty list."""
    pass

