from __future__ import absolute_import, unicode_literals

import datetime

import pytest
from django.http import HttpRequest
from freezegun import freeze_time
from wagtail.wagtailcore.models import Site

from wagtail_personalisation import rules


# Time Rule tests

@freeze_time("10:00:00")
def test_create_time_rule():
    time_rule = rules.TimeRule(start_time=datetime.time(8, 0, 0), end_time=datetime.time(23, 0, 0))

    assert time_rule.test_user() is True


@freeze_time("10:00:00")
def test_time_rule_false():
    time_rule = rules.TimeRule(start_time=datetime.time(11, 0, 0), end_time=datetime.time(23, 0, 0))

    assert time_rule.test_user() is False


@freeze_time("10:00:00")
def test_time_rule_reverse():
    time_rule = rules.TimeRule(start_time=datetime.time(13, 0, 0), end_time=datetime.time(9, 0, 0))

    assert time_rule.test_user() is False


@freeze_time("10:00:00")
def test_time_rule_reverse_next_day():
    time_rule = rules.TimeRule(start_time=datetime.time(11, 0, 0), end_time=datetime.time(11, 0, 0))

    assert time_rule.test_user() is False


# Visit Count Rule tests
def test_visit_count_rule():
    rules.VisitCountRule()


# Test test

@pytest.mark.django_db
def test_test(rf, site):
    request = HttpRequest()
    request.path = '/'
    request.META['HTTP_HOST'] = 'localhost'
    request.META['SERVER_PORT'] = 8000

    assert Site.find_for_request(request) == site


@pytest.mark.django_db
class TestPage(object):
    def test_page_copy_for_segment(self, segmented_page):
        assert segmented_page

    def test_page_has_variations(self, segmented_page):
        assert not segmented_page.is_canonical
        assert not segmented_page.has_variations
        assert segmented_page.canonical_page.is_canonical
        assert segmented_page.canonical_page.has_variations
