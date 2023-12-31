__version__ = "{{ cookiecutter.version }}"
{%- if cookiecutter.c_extension_support == "cffi" %}

from .{{ cookiecutter.c_extension_module }} import ffi as _ffi
from .{{ cookiecutter.c_extension_module }} import lib as _lib


def {{ cookiecutter.c_extension_function }}(args):
    args = [_ffi.new("char[]", arg) for arg in args]
    result = _lib.{{ cookiecutter.c_extension_function }}(len(args), _ffi.new("char *[]", args))
    if result == _ffi.NULL:
        return ""
    else:
        return _ffi.string(result)
{%- elif cookiecutter.c_extension_support != "no" %}
{%- if cookiecutter.c_extension_optional == "yes" %}
try:
    from .{{ cookiecutter.c_extension_module }} import {{ cookiecutter.c_extension_function }}
except ImportError:

    def {{ cookiecutter.c_extension_function }}(args):
        return max(args, key=len)
{%- else %}
from .{{ cookiecutter.c_extension_module }} import {{ cookiecutter.c_extension_function }}

__all__ = [
    "{{ cookiecutter.c_extension_function }}",
]
{%- endif %}
{%- endif %}
