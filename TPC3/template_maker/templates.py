from jinja2 import Template

def get_pyproject(name,command,username,email):
    template_str = """[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "{{name}}"
authors = [
    {name = "{{username}}", email = "{{email}}"},
]
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.8"
dynamic = ["version", "description"]
dependencies = [ ] #TODO:: FIXME

[project.scripts]
{{command}} = "{{name}}:main"
    """
    template = Template(template_str)
    rendered_template = template.render(name=name,command=command,username=username,email=email)
    return rendered_template

def prependPythonData(file):
    s="""#!/usr/bin/env python3

'''
Name 

SYNOPSIS


DESCRIPTIONS

FILES:


'''

__version__ = "0.0.1"

"""
    old = None
    with open(file,"r") as f:
        old = f.read()
    new = s+old
    with open(file,"w") as f:
        f.write(new)
    