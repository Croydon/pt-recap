#!/usr/bin/env python
# -*- coding: utf-8 -*-

from recap.templater import templater


default_template = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Usage statistics</title>
    </head>
    <body>
        <h1>Statistics about daily users: ${start_date} - ${end_date}</h1>
        <hr>
        <ul>
            <li>Average: ${average}</li>
            <li>Min: ${min}</li>
            <li>Max: ${max}</li>
            <li>Biggest increase between two days: ${biggest_increase}</li>
            <li>Biggest decrease between two days: ${biggest_decrease}</li>
            <li>Total change: ${total_change}</li>
        </ul>
    </body>
</html>
"""


def test_load():
    expected_result = default_template
    tpl = templater()
    result = tpl.load()
    assert result == expected_result


def test_fill():
    expected_result = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Usage statistics</title>
    </head>
    <body>
        <h1>Statistics about daily users: 20181101 - 20181130</h1>
        <hr>
        <ul>
            <li>Average: 4766</li>
            <li>Min: 3683</li>
            <li>Max: 5292</li>
            <li>Biggest increase between two days: 1189</li>
            <li>Biggest decrease between two days: 1225</li>
            <li>Total change: 323</li>
        </ul>
    </body>
</html>
"""

    tpl = templater(template_form=default_template)
    result = tpl.fill(
        {"start_date": "20181101",
         "end_date": "20181130",
         "average": "4766",
         "min": "3683",
         "max": "5292",
         "biggest_increase": "1189",
         "biggest_decrease": "1225",
         "total_change": "323"
        }
    )

    assert str(result) == expected_result
