#
# textlist = list of lists of content data; header = labels
#
def make_table(textlist, header):
    longwidths = [len(str(max(idx))) for idx in zip(*textlist)]
    strfull = ""
    delimiter = " | "  

    # table header labels
    labelwidths = header
    titlewidths = [len(labelwidths[w]) if len(labelwidths[w]) >= longwidths[w] else longwidths[w] for w in range(len(labelwidths))]
    

    # table data rows
    for rows in textlist:
        row = delimiter.join([str(cell).ljust(width) for cell, width in zip(rows, titlewidths)])
        strfull += delimiter + row + delimiter + "\n"
    
    # connect table body to header and footer
    # border =  (" " + ((len(thead)-3)*"-")) + "\n"
    thead = delimiter + delimiter.join([label.center(wid) for label, wid in zip(labelwidths, titlewidths)]) + delimiter + "\n"    
    border = " +-" + "-+-".join([("-"*w) for w in titlewidths]) + "-+" + "\n"
    strfull = "\n" + border + thead + border + strfull + border

    return strfull


    