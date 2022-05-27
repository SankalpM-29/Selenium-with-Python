# from dotenv import load_dotenv
# load_dotenv()
# import booking.constants as const
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency="INR")
        bot.select_destination(input("Where you want to go ?"))
        bot.select_dates(check_in_date=input("What is the check in date ?"),
                         check_out_date=input("What is the check out date ?")) # yyyy-mm-dd
        bot.select_travellers(int(input("How many people ?")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()  # A workaround to let our bot to grab the data properly
        bot.report_results()


except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
