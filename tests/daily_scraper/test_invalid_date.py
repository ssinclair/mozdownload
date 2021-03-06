#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest

from mozdownload import DailyScraper

import mozhttpd_base_test as mhttpd


# testing with an invalid date parameter should raise an error
tests_with_invalid_date = [
    # -p win32 --branch=mozilla-central --date=20140317030202
    {'args': {'branch': 'mozilla-central',
              'date': '20140317030202',
              'locale': 'pt-PT',
              'platform': 'win32'}
    },
    # -p win64 --branch=mozilla-central --date=2013/07/02
     {'args': {'branch': 'mozilla-central',
              'date': '2013/07/02',
              'platform': 'win64'},
     },
    # -p win32 --branch=mozilla-central --date=2013-March-15
    {'args': {'branch': 'mozilla-central',
              'date': '2013-March-15',
              'platform': 'win32'},
    }
]

tests = tests_with_invalid_date


class TestDailyScraperInvalidParameters(mhttpd.MozHttpdBaseTest):
    """test mozdownload DailyScraper class with invalid parameters"""

    def test_scraper(self):
        """Testing download scenarios with invalid parameters for DailyScraper"""

        for entry in tests:
            self.assertRaises(ValueError, DailyScraper,
                              destination=self.temp_dir,
                              base_url=self.wdir,
                              logger=self.logger,
                              **entry['args'])


if __name__ == '__main__':
    unittest.main()
