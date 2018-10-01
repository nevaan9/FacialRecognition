import xlrd
import xlwt
import xlutils

#Class to extract data from excel files
class DataExtract(object):

    #The constructor takes a filename.
    def __init__(self, fileName):
        #set the filename as instance data
        self.fileName = fileName

        #open the excel file
        self.workBook = xlrd.open_workbook(self.fileName, on_demand=True)

        #get the spreadsheet we want in the excel file
        self.workSheet = self.workBook.sheet_by_index(0)


    #Test function to print the entire spreadsheet
    def printSheet(self):
        x = self.workSheet.get_rows()
        l = [0,4,5]
        row = ""
        for i in range(self.workSheet.row_len(0)):
            y = next(x)
            for j in l:
                row += str(y[j]).split(':')[1].strip('\'') + "       "
            print(row)
            row = ""
            #w = list(map(lambda x: str(x).split(':')[1], y))
            # row = ""
            # for anItem in w:
            #     row += anItem.strip('\'') + "   "
            #print(y)



if __name__ == '__main__':

    x = DataExtract('testWorkbook.xlsx')
    x.printSheet()











