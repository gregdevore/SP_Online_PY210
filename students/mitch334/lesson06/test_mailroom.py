"""Lesson 06 | Mailroom Part 4"""
#!/usr/bin/env python

"""Used to test the mailroom.py file."""

import os
# import pytest
from mailroom import *


def test_create_report():
    assert create_report() == \
f'Donor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------\n\
Jeff Bezos                 $    1510.00           3  $      503.33\n\
Paul Allen                 $    1000.00           1  $     1000.00\n\
Warren Buffet              $     900.00           2  $      450.00\n\
Mark Zuckerberg            $     270.00           3  $       90.00\n\
William Gates, III         $     150.00           2  $       75.00\n'


def test_donors_list_list():
    assert donors_list('list') == \
f'\nDonor List:\n\
\tWilliam Gates, III\n\
\tJeff Bezos\n\
\tMark Zuckerberg\n\
\tWarren Buffet\n\
\tPaul Allen\n'


def test_donors_list_db():
    assert donors_list('db') == \
f'\nDonor Database:\n\
\tWilliam Gates, III        [100.0, 50.0]\n\
\tJeff Bezos                [1000.0, 10.0, 500.0]\n\
\tMark Zuckerberg           [200.0, 20.0, 50.0]\n\
\tWarren Buffet             [600.0, 300.0]\n\
\tPaul Allen                [1000.0]\n'


def test_add_donation(test_name = 'Matthew Mitchell', test_amount = 250.12):
    add_donation(test_name, test_amount)
    assert test_name in donors
    assert donors[test_name] == [test_amount]

    add_donation(test_name, 150)
    # assert donors[test_name] == test_amount[-1]

    assert create_report() == \
f'Donor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------\n\
Jeff Bezos                 $    1510.00           3  $      503.33\n\
Paul Allen                 $    1000.00           1  $     1000.00\n\
Warren Buffet              $     900.00           2  $      450.00\n\
Matthew Mitchell           $     400.12           2  $      200.06\n\
Mark Zuckerberg            $     270.00           3  $       90.00\n\
William Gates, III         $     150.00           2  $       75.00\n'


def test_create_email(test_name = 'Matthew Mitchell', test_amount = 250):
    assert create_email(test_name, test_amount) == \
f'Dear Matthew Mitchell,\n\nThank you for the generous donation of $250.00.\n\n\
Sincerely,\nMatthew Mitchell'


def test_send_letters():
    # send_letters()
    for file in send_letters():
        assert(os.path.isfile(file))
