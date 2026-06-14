from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_doc(self, document):
        pass
class Scannable(ABC):
    @abstractmethod
    def scan(self, document):
        pass
class Faxable(ABC):
    @abstractmethod
    def fax(self, document, number):
        pass
class Stapleable(ABC):
    @abstractmethod
    def staple(self, document):
        pass

class BasicPrinter(Printable):
    def print_doc(self, document):
        print(f"BasicPrinter -> Printing: {document}")
class OfficePrinter(Printable,Scannable,Faxable):
    def print_doc(self, document):
        print(f"OfficePrinter -> Printing: {document}")

    def scan(self, document):
        print(f"OfficePrinter -> Scanning: {document}")

  
    def fax(self, document,number):
        print(f"OfficePrinter -> Faxing: {document} to {number}")
class FullDevice(Printable,Scannable,Faxable,Stapleable):
    
    def print_doc(self, document):
        print(f"FullDevice -> Printing: {document}")

    def scan(self, document):
        print(f"FullDevice -> Scanning: {document}")

  
    def fax(self, document,number):
        print(f"FullDevice -> Faxing: {document} to {number}")
    def staple(self, document):
        print(f"FullDevice -> Stapling: {document}")

if __name__ == "__main__":
    printer = BasicPrinter()
    printer.print_doc("report.pdf")

    officeprinter = OfficePrinter()
    officeprinter.print_doc("memo.pdf")
    officeprinter.scan("memo.pdf")
    officeprinter.fax("memo.pdf",'555-1234')
    
    fulldevice = FullDevice()
    fulldevice.print_doc("contract.pdf")
    fulldevice.scan("contract.pdf")
    fulldevice.fax("contract.pdf",'555-5678')
    fulldevice.staple('contract.pdf')

# TODO: Create Printable, Scannable, Faxable, and Stapleable interfaces.
# TODO: Refactor BasicPrinter to implement only Printable.
# TODO: Create an OfficePrinter that implements Printable, Scannable, and Faxable.
# TODO: Create a FullDevice that implements all four interfaces.