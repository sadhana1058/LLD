class Book:
    def __init__(self, title :str, author :str ,isbn :str):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._isAvailable = True
    
    def borrowBook(self) -> str:
        if self._isAvailable:
            self._isAvailable ="False"
            return "success"
        else:
            return "failure"

    def returnBook(self) -> None:
        self._isAvailable=True
        return
    
    def displayInfo(self) -> None:

        if self._isAvailable:
            print(f"The book {self._isbn} titled {self._title} by {self._author} is available")
        else:
            print(f"The book {self._isbn} titled {self._title} by {self._author} is not available")
    
if __name__ == "__main__":
    a1 =Book("panchathanthira", "ramanujam" ,"123456" )
    a1.displayInfo()