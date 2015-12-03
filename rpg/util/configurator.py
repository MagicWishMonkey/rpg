import os
from .. import util


class Configurator(object):
    def __init__(self, path):
        settings_path = util.io.path_concat(path, "../.config/settings.json")
        settings_override_path = util.io.path_concat(path, "../.config/settings.override.json")
        if util.io.exists(settings_path) is False:
            settings_path = util.io.path_concat(path, "../settings.json")
            settings_override_path = util.io.path_concat(path, "../settings.override.json")
            if util.io.exists(settings_path) is False:
                raise Exception("The settings file could not be found!")

        settings_object = util.io.read_file(settings_path, text=True, fn=util.unjson)
        settings_object = util.wrap(**(settings_object))
        if util.io.exists(settings_override_path):
            override_object = util.io.read_file(settings_override_path, text=True, fn=util.unjson)
            override_object = util.wrap(**(override_object))
            settings_object.override(override_object)

        def write_node(o, key, val):
            parts = key.split(".")
            name = parts[len(parts) - 1]

            if val[0] == "[" and val[-1] == "]":
                try:
                    val = util.unjson(val)
                except Exception, e:
                    pass

            parts = parts[:-1]
            for part in parts:
                _val = o.get(part, o.get(part.lower(), {}))

                # _val will be either: o[part] or an empty dict
                o[part] = _val
                o = o[part]

            if name.lower() in o:
                o[name.lower()] = val
            elif name.upper() in o:
                o[name.upper()] = val
            else:
                o[name] = val

            return o

        env_var = {}
        for key in os.environ:
            if key.startswith("RPG_"):
                val = os.environ[key]
                key = key.replace("__", "|")
                key = key.replace("_", ".")
                key = key.replace("|", "_")
                key = ".".join(key.split(".")[1:])
                env_var[key] = val

        for key in env_var:
            val = env_var[key]

            # automatic cast bool
            if val == "true":
                val = True
            elif val == "false":
                val = False

            write_node(settings_object, key, val)

        self.__config__ = settings_object
        self.debug = settings_object.DEBUG
        self.secret_key = settings_object.SECRET_KEY
        self.config = settings_object.reduce()

    def contains(self, param):
        try:
            value = self.config[param]
            return True if value is not None else False
        except:
            return False

    def get(self, param, default=None):
        value = None
        try:
            value = self.config[param]
        except:
            return default

        if value is None:
            return default

        if isinstance(value, list) is True:
            if len(value) > 0 and isinstance(value[0], list) is True:
                value[0] = tuple(value[0])
            value = tuple(value)
        return value
