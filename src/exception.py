import sys
from typing import Optional


def error_message_detail(error: Exception, error_detail: Optional[object] = None) -> str:
    """Return a consistent, debuggable exception message."""
    if error_detail is None:
        error_detail = sys

    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    return (
        f"Error occurred in python script [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] error message [{error}]"
    )


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Optional[object] = None) -> None:
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
