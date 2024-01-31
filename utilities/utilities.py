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

# properly display an iterable list
@staticmethod
def format_list(thelist, title="", type="dict", border="="):
    #get title length for heading
    formatted = (border*len(title) + "\n") + title + ("\n" + border*len(title) + "\n")

    # display the items
    if type == "dict":
        # formatted += "\n".join(key + ": " + str(val) for key, val in thelist.items()) + "\n"
        formatted += "\n".join(f"[{i+1}] {key}: {val}" for i, (key, val) in enumerate(thelist.items())) + "\n"    # added incrementing numbers for list
    elif type == "weapons_list":
        wlist = []
        wlist = [key for key in thelist.keys()]
        # wlist = list(thelist.keys())
        return wlist
    else:
        formatted = ""
    return formatted


# Define a function that displays the galactic map as a text output
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
        print(lang.content["unsupported_obj"] + " : " + str(type(obj)))
    print("\n##########\n")

# check if input char matches with type. Target types: ('digit', 'alpha', 'instance')
def validate_input_char(input, target_type="digit"):
    if str(input).isdigit() and target_type == "digit":
        return True
    elif str(input).isalpha() and target_type == "alpha":
        return True 
    elif isinstance(input, object) and target_type == "instance":
        return True
    else:
        print(lang.content["invalid_choice"])
        return False
