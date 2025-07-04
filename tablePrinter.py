def printTable(tableData):
    
    # Create empty list of Column Widths
    colWidths = [0] * len(tableData)
    
    # Loop through each list
    for i in range(len(colWidths)):
        # Find longest string of each list
        for word in tableData[i]:
            new = len(word)
            if new > colWidths[i]:
                colWidths[i] = new
                
    # Right-adjust each word based on longest string
    for row in range(len(tableData[0])):
        for j in range(len(colWidths)):
            print(tableData[j][row].rjust(colWidths[j]), end=' ')
        print()
    
    
# Default table data
data = [['apples', 'oranges', 'cherries', 'bananas'],
        ['Alice', 'Bob', 'Carol', 'Danielle'],
        ['dogs', 'cats', 'moose', 'goose']]

# Function call
printTable(data)