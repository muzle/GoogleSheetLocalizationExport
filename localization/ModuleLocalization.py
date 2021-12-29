class ModuleLocalization:
    def __init__(self, module, keys):
        # A module is a group of components linked by a common presentation, for example, an authorization screen
        self.module = module
        # KeyLocalizations
        self.keys = keys
