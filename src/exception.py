import sys
# import logging
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in pythion script name[{file_name}] line number [{exc_tb.tb_lineno}] error mesage[{str(error)}]"
    return error_message

class CustomException(Exception):   # custom exception class inheriting from 'Exception'
    def __init__(self, error_message, error_detail:sys):    # constructor class
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# to test exception
'''
if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Exception raised for: Divide by Zero error......")
        raise CustomException(e,sys)
# '''