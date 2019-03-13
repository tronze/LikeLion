import os
import sys
import django


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(BASE_DIR)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LikeLion.settings')
    django.setup()

    from .extractor import *

    try:
        print("init")
        driver = CrawlBrowser()
        try:
            driver = CrawlBrowser()

            driver.login()

            driver.get_list()

            for i in driver.data:
                driver.get_detail(i)

        except:
            driver.browser.close()
            print("error")
        finally:
            driver.browser.close()
            print("end")
    except:
        print("init error")
    driver.browser.close()
