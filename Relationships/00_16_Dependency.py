class Document:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content
		
class Printer:
    def print(self, document):
        print("Printing:", document.get_content())
		
if __name__ == "__main__":
    doc = Document("Hello, World!")
    printer = Printer()

    printer.print(doc)

    # After print() returns, the printer has no reference to the document.
    # The document can be garbage collected independently of the printer.				