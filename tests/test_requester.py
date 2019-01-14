#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import json
import pytest
# from unittest import mock


from recap.requester import requester


def test_get_daily_users():
    result = requester.get_daily_users(start_date="20181101", end_date="20181130")
    expected_result = [
       {'count': 5061, 'date': '2018-11-30', 'end': '2018-11-30'},
       {'count': 5281, 'date': '2018-11-29', 'end': '2018-11-29'},
       {'count': 5359, 'date': '2018-11-28', 'end': '2018-11-28'},
       {'count': 5374, 'date': '2018-11-27', 'end': '2018-11-27'},
       {'count': 5292, 'date': '2018-11-26', 'end': '2018-11-26'},
       {'count': 4067, 'date': '2018-11-25', 'end': '2018-11-25'},
       {'count': 3832, 'date': '2018-11-24', 'end': '2018-11-24'},
       {'count': 4686, 'date': '2018-11-23', 'end': '2018-11-23'},
       {'count': 4763, 'date': '2018-11-22', 'end': '2018-11-22'},
       {'count': 5128, 'date': '2018-11-21', 'end': '2018-11-21'},
       {'count': 5241, 'date': '2018-11-20', 'end': '2018-11-20'},
       {'count': 5213, 'date': '2018-11-19', 'end': '2018-11-19'},
       {'count': 4041, 'date': '2018-11-18', 'end': '2018-11-18'},
       {'count': 3857, 'date': '2018-11-17', 'end': '2018-11-17'},
       {'count': 4954, 'date': '2018-11-16', 'end': '2018-11-16'},
       {'count': 5210, 'date': '2018-11-15', 'end': '2018-11-15'},
       {'count': 5182, 'date': '2018-11-14', 'end': '2018-11-14'},
       {'count': 5237, 'date': '2018-11-13', 'end': '2018-11-13'},
       {'count': 5033, 'date': '2018-11-12', 'end': '2018-11-12'},
       {'count': 3897, 'date': '2018-11-11', 'end': '2018-11-11'},
       {'count': 3777, 'date': '2018-11-10', 'end': '2018-11-10'},
       {'count': 4966, 'date': '2018-11-09', 'end': '2018-11-09'},
       {'count': 5104, 'date': '2018-11-08', 'end': '2018-11-08'},
       {'count': 5076, 'date': '2018-11-07', 'end': '2018-11-07'},
       {'count': 5180, 'date': '2018-11-06', 'end': '2018-11-06'},
       {'count': 5060, 'date': '2018-11-05', 'end': '2018-11-05'},
       {'count': 3944, 'date': '2018-11-04', 'end': '2018-11-04'},
       {'count': 3683, 'date': '2018-11-03', 'end': '2018-11-03'},
       {'count': 4745, 'date': '2018-11-02', 'end': '2018-11-02'},
       {'count': 4738, 'date': '2018-11-01', 'end': '2018-11-01'}
    ]
    assert result == expected_result


def test_get_daily_users_invalid_dates():
    with pytest.raises(requester.ExceptionInvalidDates):
        requester.get_daily_users(start_date="1940110", end_date="00112233")


def test_get_daily_users_end_data_before_start():
    with pytest.raises(requester.ExceptionInvalidDates):
        requester.get_daily_users(start_date="20181130", end_date="20181101")
