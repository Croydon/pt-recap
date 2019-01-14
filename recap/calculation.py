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
        user_max = None
        for day in numbers:
            if not user_max:
                user_max = day
            if user_max < day:
                user_max = day
        return user_max

    @staticmethod
    def biggest_increase(numbers: list):
        former_users = None
        biggest_increase = 0
        for day in numbers:
            if not former_users:
                former_users = day
            else:
                change_to_last_day = (day - former_users)
                if change_to_last_day > biggest_increase:
                    biggest_increase = change_to_last_day
        return biggest_increase

    """ The decrease is without sign, so it is a positive int
    """
    @staticmethod
    def biggest_decrease(numbers: list):
        former_users = None
        biggest_decrease = 0
        for day in numbers:
            if not former_users:
                former_users = day
            else:
                change_to_last_day = (former_users - day)
                if change_to_last_day > biggest_decrease:
                    biggest_decrease = change_to_last_day
        return biggest_decrease

    """ Total change of users, over the a time span,
        basically first - last number
    """
    @staticmethod
    def total_change(numbers: list):
        return None
