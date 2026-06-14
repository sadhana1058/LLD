# Before: One class doing three unrelated jobs
class ReportFormatter:
    def format_as_csv(self,data):
        csv_lines = []
        for row in data:
            csv_lines.append(",".join(row))
        csv_output = "\n".join(csv_lines)
        return csv_output
class ReportGenerator:
    def __init__(self):
        self.data = [
            ["Name", "Sales", "Region"],
            ["Alice", "15000", "North"],
            ["Bob", "22000", "South"],
            ["Charlie", "18000", "East"],
        ]
    def generate(self):
        return self.data

class ReportDistributor:
    def distribute(self,recipient,csv_output):
        print(f"Sending report to: {recipient}")
        print(csv_output)
        print("Report sent successfully.")


if __name__ == "__main__":
    # After refactoring, usage should look like:
    generator = ReportGenerator()
    formatter = ReportFormatter()
    distributor = ReportDistributor()
    data = generator.generate()
    formatted = formatter.format_as_csv(data)
    distributor.distribute("manager@company.com", formatted)
    