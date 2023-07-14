import languages.en as lang
import data.data as data
import views.en as views

# display message
@staticmethod
def msg(msg_id, source="lang"):
    return lang.content[msg_id] if source == "lang" else views.content[msg_id]


# format_table : create an ASCII-delimited table
#   textlist: list of lists of content data (e.g. [["Arms",2,2,6],]) 
#   header: list of table header labels (e.g. ["Inventory", "Qty", ...])
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


# Define a function that displays the map as a text output
def display_map():
    print(lang.content["label_header_map"])
    print(lang.content["label_line_header_map"])
    for planet in data.planets:
        print(planet)
    print(lang.content["label_line_header_map"])


def debug_checkpoint(msg, var=""):
    print("\n###########", msg, "\n", var, "\nCHECKPOINT\n#############\n\n\n")