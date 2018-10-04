# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/webscraping
# blog: http://thinkdiff.net
# MIT License

# --------------------------
#  Aljazeera.com Demo
# --------------------------

## News title, link scraping

from lib import log
from lib import aljazeera
from lib import helper

if __name__ == '__main__':
    # Define log file location
    log.set_custom_log_info('html/error.log')

    # SSL or HTTPS ISSUE
    helper.verify_https_issue()

    # create scraping object
    aljazeera_scrap = aljazeera.Aljazeera(aljazeera.url_aj, log)

    # checking if we should redownload from url or not
    if helper.check_cache(aljazeera.raw_html, aljazeera.CACHE):
        aljazeera_scrap.retrieve_webpage()
        aljazeera_scrap.write_webpage_as_html()

    aljazeera_scrap.read_webpage_from_html()
    aljazeera_scrap.convert_data_to_bs4()
    #aljazeera_scrap.print_beautiful_soup()
    aljazeera_scrap.parse_soup_to_simple_html()
