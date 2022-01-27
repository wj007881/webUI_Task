from time import sleep

import pytest
from pytest_bdd import when, then, parsers
from pytest_bdd import scenario, given


###############
# STEPS #
###############
@given(parsers.parse('I have a book and its name is {learn}'))
def step_click_my_audience_page(learn):
    print('I have a book and its name is '+learn+'123')


@given('I have finished 20 pages')
def book_page_i_have_a_book():
    print("hello yes i have a book and its name is {}".format("book"))


@when(parsers.parse('I begin to read the {num} page'))
def book_i(num):
    print('I begin to read the '+num+' page')


@when('I read 10 pages')
def book_2():
    print('I read 10 pages')


@then('I verify the next time I should read from Page 31')
def book333():
    print('I verify the next time I should read from Page 31')


@given(parsers.cfparse('case {num}'))
def book_seq(num):
    print('Hello there,I am reading book page {}'.format(num))