from utils.pagebase import PageBase
from utils.get_driver import get_chrome_driver
from config import APP_URL, TRACKING_MTD, USERNAME, PASSWORD


def initialize_driver():
    """
    It initializes the driver, sets the download directory, and returns a PageBase object.

    :param request_id: This is the unique identifier for the request
    :return: A PageBase object
    """
    driver = get_chrome_driver()
    pg_obj = PageBase(driver, url=APP_URL)
    return pg_obj


def login(pg_obj, u_name, u_password):
    """
    The function logs in a user with provided credentials.

    :param pg_obj: This is an object of a custom class that represents a web page. It is used to
    interact with the web page and perform actions such as clicking on elements, sending keys, and
    executing JavaScript code
    :param u_name: The username or email address of the user trying to log in
    :param u_password: The password of the user trying to log in
    :return: nothing (i.e., None).
    """
    username = "xpath@@//input[@autocomplete='username']"
    password = "xpath@@//input[@type='password']"
    sign_in_btn = "xpath@@//button[@type='submit']"

    pg_obj.send_keys(username, u_name)
    pg_obj.send_keys(password, u_password)
    print("click sign in button")
    pg_obj.execute_javascript_click(sign_in_btn)
    pg_obj.sleep_in_seconds(5)
    return


def navigate_to_report_and_download(pg_obj, report):
    """
    This allows selenium to navigate to report

    :param pg_obj: The page object representing the current web page
    :param report: The name of the report that needs to be selected
    """
    export_to_excel = "xpath@@//span[@title='Export to Excel']"
    build_excel_report = "xpath@@//button[@class='submit']"
    iframe = "xpath@@//iframe"
    pg_obj.open(url=APP_URL + report)
    pg_obj.sleep_in_seconds(15)
    pg_obj.switch_to_frame(iframe)
    pg_obj.click(export_to_excel)
    pg_obj.sleep_in_seconds(4)
    pg_obj.click(build_excel_report)
    print("report downloaded")
    pg_obj.sleep_in_seconds(10)


if __name__ == '__main__':

    try:

        print('init driver')
        pg_obl = initialize_driver()
        login(pg_obl, USERNAME, PASSWORD)
        navigate_to_report_and_download(pg_obl, TRACKING_MTD)
        print("loaded page with success")

    except Exception as e:
        print(f"Error:: > {e}")
    finally:
        try:

            pg_obl._driver.quit()
        except:
            pass
