from .gpt import GPT_Magic

def load_ipython_extension(ipython):
    ipython.register_magics(GPT_Magic)