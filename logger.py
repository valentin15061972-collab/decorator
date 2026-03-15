from datetime import datetime
from functools import wraps


def logger():
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            call_datetime = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            log_record = f"{call_datetime} | {func_name} | args:{args} | kwargs:{kwargs} | result:{result}\n"

            with open('log', 'a', encoding='utf-8') as file:
                file.write(log_record)
            return result
        return new_function
    return __logger
