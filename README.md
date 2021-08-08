# pyclesperanto assistant

[![License](https://img.shields.io/pypi/l/pyclesperanto-assistant.svg?color=green)](https://github.com/clesperanto/pyclesperanto_assistant/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/pyclesperanto-assistant.svg?color=green)](https://pypi.org/project/pyclesperanto_assistant)
[![Python Version](https://img.shields.io/pypi/pyversions/pyclesperanto-assistant.svg?color=green)](https://python.org)
[![tests](https://github.com/clesperanto/pyclesperanto_assistant/workflows/tests/badge.svg)](https://github.com/clesperanto/pyclesperanto_assistant/actions)
[![codecov](https://codecov.io/gh/clesperanto/pyclesperanto_assistant/branch/master/graph/badge.svg)](https://codecov.io/gh/clesperanto/pyclesperanto_assistant)

Assisted [pyclesperanto](https://github.com/clEsperanto/pyclesperanto_prototype) scripting in [jupyter](https://jupyter.org/) notebooks.

![](https://github.com/clesperanto/pyclesperanto_assistant/blob/main/docs/images/pylesperanto_assistant_ipython2.gif?raw=true)
[Download full movie](https://github.com/clesperanto/pyclesperanto_assistant/blob/main/docs/images/pylesperanto_assistant_ipython.mp4?raw=true)

----------------------------------

## Usage
When hacking jupyter notebooks, add this import statement:
```python
from pyclesperanto_assistant.ipython import *
```

Afterwards, when executing `what_next()` in a cell, the cell will be replaced by suggestions derived from the [CLIJ online documentation](https://clij.github.io/clij2-docs/reference).
For making good suggestions, it analyses the code in the notebook cell above.

## Installation

You can install `pyclesperanto_assistant` via [pip]:

    pip install pyclesperanto_assistant

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [BSD-3] license,
"pyclesperanto_assistant" is free and open source software

## Issues

If you encounter any problems, please [open a thread on image.sc](https://image.sc) along with a detailed description and tag [@haesleinhuepf](https://github.com/haesleinhuepf).

[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
