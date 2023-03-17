from uuid import uuid4

class CsvWriterService:
    def __init__(self):
        self.filename = f'{uuid4().hex}.csv'

    def writeData(data, filename):
        if filename is not None:
            filenamedata = f'{filename}.csv'
            with open(filenamedata, mode='wb') as f:
                f.write(data)
                return filenamedata

        with open(self.filename, mode='wb') as f:
            f.write(data)
            return filenamedata


