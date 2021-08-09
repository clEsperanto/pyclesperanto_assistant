from IPython.display import Javascript

def what_next():
    return Javascript("""var index = IPython.notebook.get_selected_index() - 2;
    var text = IPython.notebook.get_cell(index).get_text()

    var cell = IPython.notebook.insert_cell_above();

    var elements = text.replace("cle.imshow", "").split("cle.")
    if (elements.length > 1) {
        cell.set_text("next_suggestions('" + elements[1].split("\(")[0] + "')")

        var index2 = IPython.notebook.find_cell_index(cell);
        IPython.notebook.execute_cells([index2])

    } else {
        cell.set_text("# the oracle has no idea")
    }
    """)

def how_to(search_string):
    from pyclesperanto_assistant import example_code as pa_example_code
    from pyclesperanto_assistant import find_functions
    from pyclesperanto_assistant import find_functions_in_categories

    function_names = find_functions(search_string)
    function_names_in_categories = find_functions_in_categories(search_string)

    code = ""
    if len(function_names_in_categories) > 0:
        code = code + "# Operations found by category:"
        for suggestion in function_names_in_categories:
            code = code + "\\n" + pa_example_code(suggestion)
    if len(function_names) > 0:
        code = code + "# Operations found by name:"
        for suggestion in function_names:
            code = code + "\\n" + pa_example_code(suggestion)

    if len(code) > 0:
        code = code + "\\ncle.imshow(image)"
        return _replace_code_in_current_cell(code)
    else:
        code = "how_to('" + search_string + "')\\n" + \
            "# no results found when searching for '" + search_string + "'"
        return _replace_code_in_current_cell(code)

def next_suggestions(function_name):
    from pyclesperanto_assistant import next_suggestions as pa_next_suggestions
    from pyclesperanto_assistant import example_code as pa_example_code
    from pyclesperanto_assistant import _online_help
    suggestions = pa_next_suggestions(function_name)

    if len(suggestions) == 0:
        url = _online_help(function_name)
        if url is None:
            url = "https://github.com/clesperanto/pyclesperanto_prototype"
        _replace_current_cell_with_markdown("Assistant: I have no good suggestions here. Check out the [documentation](" + url + ").")

    code = "# After " + function_name + " often follow these operations (choose one):"

    for suggestion in suggestions:
        code = code + "\\n" + pa_example_code(suggestion)
    code = code + "\\ncle.imshow(image)"

    return _replace_code_in_current_cell(code)


def _replace_current_cell_with_markdown(markdown):
    return Javascript(
        "var index = IPython.notebook.get_selected_index();IPython.notebook.get_cell(index - 1).set_text('" + markdown + "');IPython.notebook.get_cell(index).set_text('');IPython.notebook.cells_to_markdown([index - 1]);IPython.notebook.execute_cells([index - 1]);")

def _replace_code_in_current_cell(code):
    return Javascript(
        "var index = IPython.notebook.get_selected_index();IPython.notebook.get_cell(index - 1).set_text('" + code + "');IPython.notebook.get_cell(index).set_text('')")

def _add_code_cell_below(code):
    return Javascript(
        "IPython.notebook.insert_cell_above().set_text('" + code + "');")