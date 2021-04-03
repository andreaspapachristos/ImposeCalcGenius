# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# real convertor 0.3527777778
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
            fileWriter.writerow(["width", "Height", "Style", "pageWidth", "pageHeight", "pages"])
            for file in glob.glob("/home/master/Downloads/test/" + "**/*job", recursive=True):
                x = regTest(file)
                fileWriter.writerow([x[0], x[1], style[x[2]], x[3], x[4], x[5]])
    except UnicodeDecodeError:
        print(file)
    except IndexError:
        print(file)
    except ValueError:
        print(file)

def regTest(path):
    #pattern1 = "%SSiPressSheet: (\d{4}.\d{5} ){2}\d\.\d{5} \d{2,5}\.\d{5} \d"
    #patterns11 = ["%SSiSignature: .+[\r\n]+([^\r\n]+)","%SSiSignature: .+[\r\n]%SSiPressSheet: \d{2,4}.\d{1,5} \d{2,4}.\d{1,5} \d{1,4}.\d{1,5} \d{1,4}.\d{1,5} ([01234])", "(?<=%SSiPrshMatrix: 8) [\d]{2,5}.\d{2,5}", "%SSiSignature: .+[\r\n]%SSiPressSheet: (\d{2,4}.\d{1,5}) (\d{2,4}.\d{1,5})",  "(?<=%SSiPrshMatrix: 9) [\d]{2,5}.\d{2,5}", "(?<=%SSiPrshMatrix: 1 )[\d]{1,2}"]
    var = []
    patterns = ["%SSiSignature: .+[\r\n]%SSiPressSheet: (\d{2,4}.\d{1,5})", "%SSiSignature: .+[\r\n]%SSiPressSheet: \d{2,4}.\d{1,5} (\d{2,4}.\d{1,5})", "%SSiSignature: .+[\r\n]%SSiPressSheet: \d{2,4}.\d{1,5} \d{2,4}.\d{1,5} \d{1,4}.\d{1,5} \d{1,4}.\d{1,5} ([01234])", "(?<=%SSiPrshMatrix: 8) [\d]{2,5}.\d{2,5}", "(?<=%SSiPrshMatrix: 9) [\d]{2,5}.\d{2,5}" ]
    with open(path, "r") as f:
        ff = f.read()
        for pattern in patterns:
            pattern123 = re.compile(pattern)
            matches = pattern123.findall(ff)
            if matches:
                var.append(int(ptTomm(float(matches[0]))))
            else: var.append(0)
        pages = (re.findall("(?<=%SSiPrshMatrix: 1) [\d]{1,2}", ff))
        if pages:
            var.append(int(pages[0]))
        else: var.append(0)
        #print(var)
    return var

if __name__ == '__main__':
    #regTest("/run/media/master/Transcend/Templates/PERIODIKA/EBDOMADIAIA/KARFITSA/bhmagazino_208x280_karfitsa_k4.tpl")
    writeCsv("/home/master/jobs.csv")