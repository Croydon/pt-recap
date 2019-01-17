#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cheetah.Template import Template
import os

basepath = os.path.dirname(__file__)


class templater():
    def __init__(self, template_form=""):
        self.template = template_form
        return

    def load(self, template_file="statistics.html.tmpl"):
        file_path = os.path.abspath(os.path.join(basepath, "data", template_file))
        with open(file_path) as f:
            self.template = f.read()
        return self.template

    def fill(self, namespace):
        readme_parsed = Template(self.template, searchList=[namespace])
        return readme_parsed

    def save(self):
        return None
