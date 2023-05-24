import datetime

class LogActivity:
    """Class logs time function was called, its arguments and return value."""

    def __init__(self, funct:callable) -> None:
        self.funct = funct


    def __call__(self, *args, **kwds):
        """Methond logs date when decorated function was called."""
        try:
            with open("activity_log.txt",'a') as log_file:
                log_file.write(f"A function {self.funct.__name__} was called on {datetime.datetime.now()}\n")
                log_file.write(f"Function was called for:\n{args}, {kwds}\n")
                log_file.write(f"Function returned:\n{self.funct(*args, **kwds)}\n") 
        except Exception as e:
            print("LogActivity encountered a problem:", e)
        

