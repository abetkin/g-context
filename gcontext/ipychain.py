import IPython
from IPython.core.magic import Magics, magics_class, line_magic

def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(ExtraContextMagics)
    # ip.events.register('pre_run_cell', auto_reload.pre_run_cell)
    # ip.events.register('post_execute', auto_reload.post_execute_hook)

def unload_ipython_extension(ipython): pass
    # If you want your extension to be unloadable, put that logic here.


@magics_class
class ExtraContextMagics(Magics):

    @line_magic
    def use(self, context_var):
        user_ns = self.shell.user_ns

    @line_magic
    def inject(self, callabl):
        1
