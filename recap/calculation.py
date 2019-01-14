#!/usr/bin/env python
# -*- coding: utf-8 -*-


class calculation():
    """ Class to make some calculations for user statistics
    """
    def __init__(self):
        return None

    """ Returns the average amount of users,
        rounded as there aren't half users :) 
    """
    @staticmethod
    def average(numbers: list):
        user_sum = 0
        for day in numbers:
            user_sum += day
        return round(user_sum / len(numbers))

    @staticmethod
    def min(numbers: list):
        user_min = None
        for day in numbers:
            if not user_min:
                user_min = day
            if user_min > day:
                user_min = day
        return user_min

    @staticmethod
    def max(numbers: list):
        return None

    @staticmethod
    def biggest_increase(numbers: list):
        return None

    @staticmethod
    def biggest_decrease(numbers: list):
        return None

    """ Total change of users, over the a time span,
        basically first - last number
    """
    @staticmethod
    def total_change(numbers: list):
        return None
