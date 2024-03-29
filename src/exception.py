#Exception Handling 
import sys
import logging 
from logger import LOG_FILE_PATH  #

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #This line uses the exc_info() method of the error_detail instance (which is an instance of sys) to get information about the current exception.and extracts the traceback object.
    file_name = exc_tb.tb_frame.f_code.co_filename #This line extracts the filename of the Python script where the exception occurred from the traceback object.
    error_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error) #This line constructs an error message string that includes the filename, line number, and error message.
        
    ) 
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message 
    

