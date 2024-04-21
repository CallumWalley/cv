## Setup


```sh
git clone https://github.com/
cd 
python -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```


<a id="__init__"></a>

# \_\_init\_\_

<a id="cv"></a>

# cv

<a id="cv.load_json_yaml"></a>

#### load\_json\_yaml

```python
def load_json_yaml(path)
```

Loads a json, or yaml file from 'path'

<a id="cv.kw_mask"></a>

#### kw\_mask

```python
def kw_mask(obj, mask_value)
```

Filters one dictionary based on another.
Tried to use as common sense rules as possible.

<a id="cv.html2pdf"></a>

#### html2pdf

```python
def html2pdf(html, pdf_path)
```

Attempts to render html to pdf

<a id="cv.copy_or_render"></a>

#### copy\_or\_render

```python
def copy_or_render(source, dest)
```

Copy all files from source to dest. If it is scss, render it instead.

<a id="cv.CurriculumVitae"></a>

## CurriculumVitae Objects

```python
class CurriculumVitae()
```

Class representing a CV, with info fo all it's possible configs.

<a id="cv.CurriculumVitae.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path)
```

Parameters
----------
path : path to cv file. Can be yaml or json.

<a id="cv.CurriculumVitae.generate_vibe"></a>

#### generate\_vibe

```python
def generate_vibe(theme,
                  outputs,
                  name="",
                  includes=False,
                  mask=True,
                  overwrite=False)
```

Parameters
----------
theme : str
    Path to theme directory.
outputs : list
    List of paths specifying what outputs you want. 
    Currently supports '.html', '.pdf'.
    Must include at least one output.
    Build directory will be parent of first output.
name : str, optional
    Does nothing.
    (default is "")
includes : str, optional
    Path to include directory. 
    Any paths referenced in CV (or overwrites), must be relative to this directory.
    (default is False)
mask : dict, optional
    Determines what data is used to generate cv.
    (default is True)
    TODO: examples.
overwrite : dict, optional
    A dictionary mirroring the CV file.
    Any values specified here will overwrite CV values for this build only.
    (default is False)

