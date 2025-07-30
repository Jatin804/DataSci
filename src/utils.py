# handling exception !

import sys
from src.logger import logging

# error extraction ! from sys
def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()       # extracting 3rd error message only
    file_name = exc_tb.tb_frame.f_code.co_filename      # extracing file name
    error_message = "Error in py script [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )
    return error_message

class Custom__exception(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message