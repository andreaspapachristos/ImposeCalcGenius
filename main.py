# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv, glob
convertor = 0.3527777778
style = ("sheetwise", "worknturn", "workntumble", "single_sided", "perfector")
ptTomm = lambda x: int(x * convertor)


def readTplFile(path):
    with open(path, "r") as f:
        return f.readlines()[9].split(" ")[1:8]

def writeCsv(path):


    with open(path, "w") as f:
        fileWriter = csv.writer(f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        fileWriter.writerow(["width", "Height", "Style", "pages", "pageWidth", "pageHeight"])
        for file in glob.glob("/run/media/master/Transcend/Templates/EPIPEDES/" + "**/*tpl", recursive=True):
            x = readTplFile(file)
            fileWriter.writerow([float(x[0])*convertor, float(x[1])*convertor, style[int(x[4])]])
if __name__ == '__main__':
    writeCsv("/home/master/test.csv")
