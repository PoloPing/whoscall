from importlib import import_module


def load_settings(path):
    mod = import_module(path)
    setting = {}
    for var in dir(mod):
        if var.isupper():
            value = getattr(mod, var)
            setting[var] = value
    return setting
