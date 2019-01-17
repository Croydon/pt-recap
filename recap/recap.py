#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .requester import requester
from .calculation import calculation
from .templater import templater


def main(args):
    """ Main entry point

    :param args: User arguments
    """

    start_date = "20181101"
    end_date = "20181130"

    data = requester.get_daily_users(start_date=start_date, end_date=end_date)
    numbers = requester.get_users_numbers_only(data)

    # get statistics
    statistics = {
        "start_date": start_date,
        "end_date": end_date,
        "average": calculation.average(numbers),
        "min": calculation.min(numbers),
        "max": calculation.max(numbers),
        "biggest_increase": calculation.biggest_increase(numbers),
        "biggest_decrease": calculation.biggest_decrease(numbers),
        "total_change": calculation.total_change(numbers)
    }

    tpl = templater()
    tpl.load()
    tpl.fill(namespace=statistics)
    tpl.save()
