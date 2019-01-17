#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cheetah.Template import Template
import os

basepath = os.path.dirname(__file__)


class templater():
    def __init__(self, template_form="", template_generated=""):
        self.template = template_form
        self.generated = template_generated
        return

    def load(self, template_file="statistics.html.tmpl"):
        file_path = os.path.abspath(os.path.join(basepath, "data", template_file))
        with open(file_path) as f:
            self.template = f.read()
        return self.template

    def fill(self, namespace):
        readme_parsed = Template(self.template, searchList=[namespace])
        self.generated = str(readme_parsed)
        return readme_parsed

    def save(self, file_path=os.path.join("output", "statistics.html")):
        if not os.path.isdir("output"):
            os.mkdir("output")
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(self.generated)

        return file_path
