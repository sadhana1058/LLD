from enum import Enum

class HttpStatus(Enum):

    OK = (200,"OK")
    BAD_REQUEST=(400,"Bad Request")
    NOT_FOUND =(404,"Not Found")
    INTERNAL_SERVER_ERROR = (500,"Internal Server Error")

    def isSuccess(self) -> bool:
        if self.value[0]<400:
            return True
        return False
    
    def display(self) ->None:
        print(f"{self.value[0]} {self.value[1]}")
    @staticmethod
    def fromCode(code):
        # _httpcodes={
        #     HttpStatus.OK.value[0] : HttpStatus.OK.value[1],
        #     HttpStatus.BAD_REQUEST.value[0] : HttpStatus.BAD_REQUEST.value[1],
        #     HttpStatus.NOT_FOUND.value[0] : HttpStatus.NOT_FOUND.value[1],
        #     HttpStatus.INTERNAL_SERVER_ERROR.value[0] :HttpStatus.INTERNAL_SERVER_ERROR.value[1]
        # }
        # return _httpcodes[code]
        for status in HttpStatus:
            if status.value[0] == code:
                return status
        return None




if __name__ == "__main__":
    HttpStatus.OK.display()
    HttpStatus.NOT_FOUND.display()

    print(f"Is 200 success? {str(HttpStatus.OK.isSuccess()).lower()}")
    print(f"Is 404 success? {str(HttpStatus.NOT_FOUND.isSuccess()).lower()}")

    found = HttpStatus.fromCode(500)
    if found :
        print(found)
        print("Found by code 500: ", end="")
        found.display()