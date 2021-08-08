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

def next_suggestions(function_name):
    import pyclesperanto_prototype as cle

    from pyclesperanto_assistant import next_suggestions as pa_next_suggestions
    from pyclesperanto_assistant import _online_help
    suggestions = pa_next_suggestions(function_name)

    if len(suggestions) == 0:
        url = _online_help(function_name)
        if url is None:
            url = "https://github.com/clesperanto/pyclesperanto_prototype"
        return Javascript(
            "var index = IPython.notebook.get_selected_index();IPython.notebook.get_cell(index - 1).set_text('Assistant: I have no good suggestions here. Check out the [documentation](" + url + ").');IPython.notebook.get_cell(index).set_text('');IPython.notebook.cells_to_markdown([index - 1]);IPython.notebook.execute_cells([index - 1]);")

    code = ""

    for suggestion in suggestions:
        # example = example_code(suggestion)
        # if example is not None:
        #    print(example)
        #    continue

        func = getattr(cle, suggestion)
        if len(code) > 0:
            code = code + "\\n"
        code = code + "image = cle." + func.__name__ + "(" + (", ".join(func.fullargspec.args)) + ")"
    code = code + "\\ncle.imshow(image)"

    return Javascript(
        "var index = IPython.notebook.get_selected_index();IPython.notebook.get_cell(index - 1).set_text('" + code + "');IPython.notebook.get_cell(index).set_text('')")