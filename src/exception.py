import sys
## sys module is used to extract detailed error information, such as the file name and line number where the exception occurred.
from src.logger import logging
 
def error_message_detail(error, error_detail:sys):
    ## error_detail taken from sys lib
    _, _, exc_tb = error_detail.exc_info()
    ## .exc_info gives us three details: first 2 not interested, 
    file_name = exc_tb.tb_frame.f_code.co_filename
    '''
        Think of traceback (exc_tb) as a “map” of the function calls that led to the error.
        From exc_tb, you can drill down:
        exc_tb.tb_frame → the stack frame (snapshot of the program at the moment of the error).
        tb_frame.f_code → the code object of that frame.
        f_code.co_filename → the name of the file where that code lives.
    '''
    line_number = exc_tb.tb_lineno
    error_message="Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    def __str__(self):
        return self.error_message
    
    ## checking if correclty running:

if __name__ == "__main__":
    logging.info("Logging has started.")
    ## Every Python file has a built-in variable called __name__. If you run the file directly, Python sets __name__ = "__main__".

try:
    a = 1 / 0
except Exception as e:
    logging.info('Dividing by zero')
    raise CustomException(e, sys)