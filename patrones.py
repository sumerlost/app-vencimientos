import re

patronfecha = re.compile("^((|[012])(\d|[3][01]))/(\d|[0]\d|[01][012])/\d\d$")
patronnumerico = re.compile("^\d+$")
