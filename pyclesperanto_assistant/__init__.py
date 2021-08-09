__version__ = "0.1.1"

def _get_docs(function_name):
    if callable(function_name):
        return function_name.__doc__
    import pyclesperanto_prototype as cle
    try:
        func = cle.operation(function_name)
    except KeyError:
        return None
    if func is None:
        return None
    else:
        return func.__doc__

def _online_help(function_name):
    docs = _get_docs(function_name)
    if docs is None:
        print("I don't know " + str(function_name))
        return

    temp = docs.split("https://")
    if len(temp) <= 1:
        print("I don't know " + str(function_name))
        return

    link = "https://" + temp[1].split("\n")[0]
    return link


def _clij_name_to_clesperanto_name(clij_name):
    import re
    import pyclesperanto_prototype as cle

    name = re.sub(r'(?<!^)(?=[A-Z])', '_', clij_name).lower()
    candidates = [k for k in cle.operations().keys() if name in k]
    if len(candidates) > 0:
        return candidates[0]
    else:
        return None

def find_functions(search_string):
    import re
    import pyclesperanto_prototype as cle
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', search_string).lower()

    candidates = [k for k in cle.operations().keys() if name in k]
    return candidates

def find_functions_in_categories(search_string):
    import pyclesperanto_prototype as cle
    return list(cle.operations(search_string).keys())

def next_suggestions(function_name):
    import urllib
    url = _online_help(function_name)
    file = urllib.request.urlopen(url)

    search_mode = False

    candidates = []

    for line in file:
        decoded_line = line.decode("utf-8")
        if "often-followed-by" in decoded_line:
            search_mode = True
            continue
        if search_mode:
            if "</ul>" in decoded_line:
                break
            temp = decoded_line.split("reference_")
            if len(temp) <= 1:
                continue
            command = temp[1].split("\"")[0]

            candidate = _clij_name_to_clesperanto_name(command)
            if candidate is not None:
                candidates.append(candidate)
    return candidates

def example_code(function_name):
    import pyclesperanto_prototype as cle
    func = getattr(cle, function_name)
    if hasattr(func, "fullargspec"):
        args = func.fullargspec.args
    else:
        import inspect
        args = inspect.getfullargspec(func).args
    return "image = cle." + func.__name__ + "(" + (", ".join(args)) + ")"