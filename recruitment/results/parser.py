import os
import sys
import django


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(BASE_DIR)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LikeLion.settings')
    django.setup()

    from recruitment.results.extractor import *

    try:
        print("init")
        driver = CrawlBrowser()
        try:
            driver = CrawlBrowser()

            driver.login()

            driver.get_list()

            for i in driver.data:
                driver.get_detail(i)

            driver.browser.close()

        except Exception as e:
            print(e)
            driver.browser.close()
        finally:
            driver.browser.close()
            print("end")
    except Exception as e:
        print(e)

