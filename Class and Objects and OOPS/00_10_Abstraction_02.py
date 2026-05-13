from abc import ABC, abstractmethod

class DataExporter(ABC):
    def validate(self, data: list) -> bool:
        # Return False and print "Export failed: No data to export." if data is empty
        if not data:
            print("Export failed: No data to export.")
            return False
        # Return True and print "Validation passed. Exporting N records." otherwise
        print("Validation passed. Exporting ",len(data),"records." )
        return True

    @abstractmethod
    def export(self, data: list) -> None:
        pass

class CSVExporter(DataExporter):
    def export(self, data: list) -> None:
        # Call self.validate(data) first. If validation fails, return early.
        if  not self.validate(data):
            return

        else:
            print("CSV: ",",".join(data))
            return 
        # Otherwise, print CSV format: "CSV: Alice,Bob,Charlie"
        # Hint: use ",".join(drintata)
        

class JSONExporter(DataExporter):
    def export(self, data: list) -> None:
        # Call self.validate(data) first. If validation fails, return early.
        if  not self.validate(data):
            return

        else:
            print("JSON : ",data)
            return 
        # Otherwise, print JSON array format: JSON: ["Alice", "Bob", "Charlie"]
        


if __name__ == "__main__":
    csv = CSVExporter()
    csv.export(["Alice", "Bob", "Charlie"])

    print()

    json_exp = JSONExporter()
    json_exp.export(["Alice", "Bob", "Charlie"])

    print()

    csv.export([])  # Should fail validation
