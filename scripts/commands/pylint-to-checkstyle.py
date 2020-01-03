#!/usr/bin/env python
# <?xml version="1.0" encoding="UTF-8"?>
# <checkstyle version="5.0">
# </checkstyle>

import sys
from io import StringIO
import json
from itertools import groupby


def escape(data):
    # must do ampersand first
    data = data.replace("&", "&amp;")
    data = data.replace(">", "&gt;")
    data = data.replace("<", "&lt;")
    return data


class PylintNote:
    def __init__(self, typ, line, column, message, filepath):
        self.source = "pylint"
        self.type = typ
        self.line = line
        self.column = column
        self.message = message
        self.filepath = filepath

    @property
    def severity(self):
        return {
            "warning": "warning",
            "error": "error",
            "convention": "info",
            "refactor": "info"
        }[self.type]


def read_pylint_json_from_stdin():
    data = json.load(sys.stdin)
    for item in data:
        note = PylintNote(
            typ=item["type"],
            line=item["line"],
            column=item["column"],
            message=item["message"],
            filepath=item["path"],
        )
        yield note


def format_checkstyle(notes):
    keyfn = lambda x: x.filepath
    notes = sorted(notes, key=keyfn)

    f = CheckstyleFormatter()
    f.write_start()

    for group, errors in groupby(notes, keyfn):
        f.write_file_start(group)
        for error in errors:
            f.write_error(error)
        f.write_file_end()

    f.write_end()
    print(f._writer.getvalue())


class CheckstyleFormatter:
    def __init__(self):
        self._writer = StringIO()

    def write_start(self):
        self._writer.write('<?xml version="1.0" encoding="UTF-8"?><checkstyle version="5.0">')

    def write_end(self):
        self._writer.write('</checkstyle>')

    def write_file_start(self, filename):
        self._writer.write('<file name="{filename}">'.format(
            filename=escape(filename)))

    def write_file_end(self):
        self._writer.write('</file>')

    def write_error(self, error):
        tmpl = '<error column="{col}" line="{line}" message="{message}" severity="{severity}" source="{source}"/>'
        self._writer.write(tmpl.format(
            col=error.column,
            line=error.line,
            message=escape(error.message),
            severity=error.severity,
            source=error.source
        ))


def main():
    notes = read_pylint_json_from_stdin()
    format_checkstyle(notes)


if __name__ == '__main__':
    main()