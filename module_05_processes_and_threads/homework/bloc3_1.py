import io
import sys
import traceback
class RedirectFlows:
    def __init__(self, st_out, er_out=None):
        self.st_out = st_out
        self.er_out = er_out
        self.standart_out=sys.stdout
        self.standart_err=sys.stderr

    def __enter__(self):
        sys.stdout = self.st_out
        sys.stderr = self.er_out

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            traceback.print_exception(
                exc_type, exc_val, exc_tb
            )
        sys.stdout=self.standart_out
        sys.stderr=self.standart_err

with RedirectFlows(io.StringIO()):
    print('This line goes to file')
print('This line appears on screen')
