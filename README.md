# Python package template

This repository can be used as a template for Python packages!


## How to install
```bash
$ git clone https://github.com/IkokObi/package_template.git
$ pip install package_template/
```

## How to use
```python
import package_template as pt

# Cast
digit = pt.cast.cast_int(4.5)  # digit: 4
s = pt.cast.cast_str('3.14')  # s: '3.14'

# Data analysis
data = [1, 2, 4, 8]
analysis = pt.stat.stat_analysis(data) # analysis: {'mean': 3.75, 'std': 2.680951323690902}

# Greeting
pt.greet('Spam')
"""[Output]
Hello Spam!
I'm Koki Obinata.
This repository is template for Python package.
Have a great project!  
"""
```
