# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#0.3527777778
import csv, glob, re, math
convertor = 0.3527777
style = ("sheetwise", "worknturn", "workntumble", "single_sided", "perfector")
ptTomm = lambda x: math.ceil(float("{:.4f}".format(x)) * convertor)


def readTplFile(path):
    with open(path, "r") as f:
        return f.readlines()[9].split(" ")[1:8]

def writeCsv(path):
    try:
        with open(path, "w") as f:
            fileWriter = csv.writer(f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
            fileWriter.writerow(["width", "Height", "Style", "pages", "pageWidth", "pageHeight"])
            for file in glob.glob("/run/media/master/Transcend/Templates/EPIPEDES/" + "**/*tpl", recursive=True):
                x = readTplFile(file)
                fileWriter.writerow([ptTomm(float(x[0])), ptTomm(float(x[1])), style[int(x[4])]])
    except UnicodeDecodeError:
        print(file)
    except IndexError:
        print(file)
    except ValueError:
        print(file)

def regTest(path):
    pattern1 = "%SSiPressSheet: (\d{4}.\d{5} ){2}\d\.\d{5} \d{2,5}\.\d{5} \d"
    patterns11 = ["%SSiSignature: .+[\r\n]+([^\r\n]+)","%SSiSignature: .+[\r\n]%SSiPressSheet: \d{2,4}.\d{1,5} \d{2,4}.\d{1,5} \d{1,4}.\d{1,5} \d{1,4}.\d{1,5} ([01234])", "(?<=%SSiPrshMatrix: 8) [\d]{2,5}.\d{2,5}", "%SSiSignature: .+[\r\n]%SSiPressSheet: (\d{2,4}.\d{1,5}) (\d{2,4}.\d{1,5})",  "(?<=%SSiPrshMatrix: 9) [\d]{2,5}.\d{2,5}", "(?<=%SSiPrshMatrix: 1 )[\d]{1,2}"]
    patterns = ["%SSiSignature: .+[\r\n]%SSiPressSheet: (\d{2,4}.\d{1,5})", "%SSiSignature: .+[\r\n]%SSiPressSheet: \d{2,4}.\d{1,5} (\d{2,4}.\d{1,5})", "%SSiSignature: .+[\r\n]%SSiPressSheet: \d{2,4}.\d{1,5} \d{2,4}.\d{1,5} \d{1,4}.\d{1,5} \d{1,4}.\d{1,5} ([01234])", "(?<=%SSiPrshMatrix: 8) [\d]{2,5}.\d{2,5}", "(?<=%SSiPrshMatrix: 9) [\d]{2,5}.\d{2,5}" ]
    with open(path, "r") as f:
        ff = f.read()
        for pattern in patterns:
            pattern123 = re.compile(pattern)

            matches = pattern123.findall(ff)
            print(int(ptTomm(float(matches[0]))))


if __name__ == '__main__':
    regTest("/home/master/Downloads/test/Dubois soma 272sel 14x21 4-1-21 58x86.job")
    #writeCsv("/home/master/base1.csv")