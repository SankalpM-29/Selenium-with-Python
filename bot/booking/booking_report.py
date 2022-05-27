# Parse data to print hotel details
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

class BookingReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name(
            "a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element_by_class_name(
                'fcab3ed991 a23c043802'
            ).get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element_by_class_name(
                'fcab3ed991 bd73d13072'
            ).get_attribute('innerHTML').strip()
            hotel_score = deal_box.find_element_by_class_name(
                'b5cd09854e d10a6220b4'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection

