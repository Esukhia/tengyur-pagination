import openpyxl
import os
from pathlib import Path
import glob

sourceDir = 'sources'

print(f'finding xlsx files in {sourceDir}')

# get all excel files in sources
xlFiles = glob.glob(f'{sourceDir}/**/*.xlsx', recursive=True)

def xlsx2csv(xlFile):
    # convert to csv with parent dir
    xlFile = Path(xlFile)

    # get data from excel file
    xlsx = openpyxl.load_workbook(xlFile, data_only=True)
    sheet = xlsx.active
    data = sheet.rows

    # create/open dir and create csv
    outDir = Path.cwd() / xlFile.parts[-2].split(' ')[0]    # strip the tibetan with split
    outDir.mkdir(parents=True, exist_ok=True)
    outStem = xlFile.stem
    outPath = outDir / f'{outStem}.csv'

    # write data in csv
    csv = open(outPath, "w+", encoding='utf-8')
    for row in data:
        l = list(row)
        for i in range(len(l)):
            if i == len(l) - 1:
                csv.write(str(l[i].value))
            else:
                csv.write(str(l[i].value) + ',')
        csv.write('\n')
    csv.close()


for xl in xlFiles:
    print(f'converting: {xl}')
    xlsx2csv(xl)
