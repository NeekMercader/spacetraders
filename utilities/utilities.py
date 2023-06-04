#
# maketable : create an ASCII-delimited table
#   textlist = list of lists of content data (e.g. [["Arms",2,2,6],]) 
#   header = list of table header labels (e.g. ["Inventory", "Qty",])
#
def format_table(textlist, header):
    max_widths = [max(len(str(cell)) for cell in column) for column in zip(header, *textlist)]
    strfull = ""
    delimiter = " | "
    border = " +-" + "-+-".join([("-"*w) for w in max_widths]) + "-+" + "\n"

    # table data rows
    for rows in textlist:
        row = delimiter.join([str(cell).ljust(width) if isinstance(cell, str) else str(cell).rjust(width) for cell, width in zip(rows, max_widths)])
        strfull += delimiter + row + delimiter + "\n"
    
    # connect table body to header and footer stringsb
    thead = delimiter + delimiter.join([label.center(wid) for label, wid in zip(header, max_widths)]) + delimiter + "\n"
    strfull = border + thead + border + strfull + border

    return strfull
