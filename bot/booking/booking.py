import booking.constants as const
import os
from booking.booking_filtrations import BookingFiltrations
from selenium import webdriver
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = const.DRIVER_PATH, teardown = False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        preferred_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        preferred_currency_element.click()

    def select_destination(self, destination):
        input_searchbar = self.find_element_by_id('ss')
        input_searchbar.clear()
        input_searchbar.send_keys(destination)
        first_result = self.find_element_by_css_selector(
            "li[data-i='0']"
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_travellers(self, adult_count = 1):
        traveller_menu = self.find_element_by_id('xp__guests__toggle')
        traveller_menu.click()

        while True:
            adult_count_decrease = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            adult_count_decrease.click()

            ## if the value of adults reaches 1 then leave loop
            adult_counter = self.find_element_by_id('group_adults').get_attribute(
                'value'
            )
            if int(adult_counter) == 1:
                break

        for i in range(adult_count - 1):
            adult_count_increase = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Adults"]'
            )
            adult_count_increase.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtrations = BookingFiltrations(driver = self)
        filtrations.apply_star_rating(3,4,5)
        filtrations.sort_price_lowest_first()

    def report_results(self):

        # hotel_boxes = self.find_element_by_id(
        #     'search_results_table'
        # )

        report = BookingReport(self)
        print(len(report.deal_boxes))
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)


