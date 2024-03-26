# -*- coding: utf-8 -*-
"""

@author: DanielSui
"""

from crawler import write_crawl_results

#find top 10 urls for item 1 & 2 and .....
the_data = write_crawl_results(
    ["columbia university",
     "yale university"], 10)