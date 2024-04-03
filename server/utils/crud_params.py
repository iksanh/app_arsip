class CrudParams:

    def __init__(self, modul, *args, **kwargs):
        self._module = modul.lower()
        self._args = args
        self._extra = kwargs

    @property
    def params(self):
        return {
            "module": self._module,
            "links": {
                "create": f"create-{self._module}",
                "edit": f"edit-{self._module}",
                "delete": f"delete-{self._module}",
                "list": f"list-{self._module}"
            },
            "active": "active",
            "args": self._args,
            "parameter": self._extra
        }

    def parameter(self, **kwargs):
        
        return {
            "module": self._module,
            "links": {
                "create": f"create-{self._module}",
                "edit": f"edit-{self._module}",
                "delete": f"delete-{self._module}",
                "list": f"list-{self._module}"
            },
            "active": "active",
            "parameter": kwargs
        }


    def parameters(self, **kwargs):
        default_parameter = {
            "module": self._module,
            "links": {
                "create": f"create-{self._module}",
                "edit": f"edit-{self._module}",
                "delete": f"delete-{self._module}",
                "list": f"list-{self._module}"
            },
        }

        default_parameter.update(kwargs)

        return default_parameter
