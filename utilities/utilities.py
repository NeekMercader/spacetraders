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
    print("\n########### CHECKPOINT: ", msg, "\n", var, "\n#############\n\n")

def print_obj_sans_extra(msg, obj):   # print contents of object without the fluff
    print("\n########## PRINT OBJ (without extraneous): ", msg, "\n")
    if isinstance(obj, (list, range)):
        for key, value in enumerate(obj):
            print(f"{key}: {value}")
    elif isinstance(obj, dict):         # handle dictionaries
        for key, value in obj.items():
            print(f"{key}: {value}")
            if hasattr(value, '__dict__'):
                # if a dict value is an object with attributes, print its attributes
                for inner_key, inner_value in vars(value).items():
                    if not inner_key.startswith('__') and not callable(inner_value):
                        print(f"  {inner_key}: {inner_value}")
    else:
        print(lang.content["unsupported_obj"])

    print("\n##########\n")
