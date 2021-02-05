import inspect


class Aaa:
    def foo(self):
        function_name = inspect.currentframe().f_code.co_name

        try:
            a = False
            # do something
            if a == True:
                # do something more

                return 'aaa'
            else:
                raise Exception('{} internal_1 Exception HTTP != 200'.format(function_name))
        except Exception as err:
            raise Exception('{} main Exception'.format(function_name)).with_traceback(err.__traceback__)