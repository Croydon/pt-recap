#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import requests
import json


class requester():
    def __init__(self):
        return None

    class ExceptionInvalidDates(Exception):
        pass

    @staticmethod
    def _validate_date_format(date_text):
        try:
            datetime.strptime(date_text, '%Y%m%d')
        except ValueError:
            raise requester.ExceptionInvalidDates("Incorrect date format. Use YYYYMMDD format.")

    @staticmethod
    def _transform_data(json_data):
        return json.loads(json_data)

    @staticmethod
    def get_users_numbers_only(data):
        return None

    @staticmethod
    def get_daily_users(start_date="20181101", end_date="20181130"):
        """ Basic checks first if dates are valid
        """
        if start_date > end_date:
            raise requester.ExceptionInvalidDates("Start date is after end date!")

        requester._validate_date_format(start_date)
        requester._validate_date_format(end_date)

        # TODO: Improve error handling when API is unreachable or returns in another way something unexpected
        api = "https://addons.mozilla.org/en-US/firefox/addon/vertical-tabs-reloaded/statistics/usage-day-{}-{}.json".format(
            start_date,
            end_date
        )

        r = requests.get(api)

        return requester._transform_data(r.text)
