import sys

def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parametrized
def mdec(f, level):
    def aux(*xs, **kws):
        try:
            return level * f(*xs, **kws)
        except Exception as err:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            if level == 'warning':
                print(f'I am a level {level}. Except string of {filename} => {f.__name__}() function => ' + str(err))
            elif level == 'error':
                print(f'Something else')
    return aux