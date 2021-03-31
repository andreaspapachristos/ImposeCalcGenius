# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv, glob, re
convertor = 0.3527777778
style = ("sheetwise", "worknturn", "workntumble", "single_sided", "perfector")
ptTomm = lambda x: int(x * convertor)


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
                fileWriter.writerow([float(x[0])*convertor, float(x[1])*convertor, style[int(x[4])]])
    except UnicodeDecodeError:
        print(file)
    except IndexError:
        print(file)
    except ValueError:
        print(file)

def regTest(path):
    pattern1 = "%SSiPressSheet: (\d{4}.\d{5} ){2}\d\.\d{5} \d{2,5}\.\d{5} \d"
    patterns = ["%SSiSignature: .+[\r\n]+([^\r\n]+)", "(?<=%SSiPrshMatrix: 8) [\d]{2,5}.\d{2,5}", "(?<=%SSiPrshMatrix: 9) [\d]{2,5}.\d{2,5}", "(?<=%SSiPrshMatrix: 1 )[\d]{1,2}"]
    with open(path, "r") as f:
        pattern = re.compile(r'(?<=%SSiPrshMatrix: 8) [\d]{2,5}.\d{2,5}')
        ff = f.read()
        matches = pattern.findall(ff)
        for match in matches:
            print(match)


if __name__ == '__main__':
    regTest("/run/media/master/Transcend/Templates/EPIPEDES/man roland 708/61x86_S-S_290x400_s8_Head15mm.tpl")
    #writeCsv("/home/master/base.csv")