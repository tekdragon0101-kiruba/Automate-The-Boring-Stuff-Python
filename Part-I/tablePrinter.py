#! python3
# tablePrinter - printing lists of texts in table format.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    # colWidth = [0] * lengthOfTableData
    colWidth = [(max(len(data) for data in column)) for column in tableData]
    for j in range(len(tableData[0])):
        for k in range(len(tableData)):
            print(tableData[k][j].rjust(colWidth[k]), end=' ')
        print()

printTable()