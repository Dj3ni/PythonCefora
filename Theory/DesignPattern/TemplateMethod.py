from abc import ABC, abstractmethod

class AbstractReport(ABC):

    def get_header(self):
        return "This is a generic header"

    def get_footer(self):
        return "This is a generic footer"

    @abstractmethod
    def get_body(self):
        pass

    def display_report(self):
        print(self.get_header())
        print(self.get_body())
        print(self.get_footer())


class CustomReport(AbstractReport):
    def get_body(self):
        return "Custom Report"


custom_report = CustomReport()
custom_report.display_report()