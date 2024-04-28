# CV

## Setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Original Idea

* JSON file should drive creation of CV.
* Tag information for multiple variations. e.g.
  * cv-design.pdf
  * cv-engineering.pdf
  * cv-computerscience.pdf
* Also generate gh-pages page.
* CI/CD
* Python / Jinja (for pdf format at least). Maybe MKdocs for gh-pages

Inspired somewhat by this

* <https://timsainburg.com/curriculum-vitae-in-python-html-jinja.html>
* JSON resume <https://jsonresume.org/>

Similar to <https://github.com/nikaro/resume-pycli>

## Whats in this repo

### `cvibes/`

`cvibes` stupidly named python package does all the stuff.

### `theme-metro/`

A theme contains all the jinja files, css and other assets specific to the theme.
More info on theme in `SPECIFICATION`
This theme is called `metro` cause my bf said my cv looked like a subway map.

### `CurriculumVitae.yaml`

My CV. Based on https://jsonresume.org/ with some sensible changes, and yaml.
Could also be json if you swing that way.

### `vibes.yaml`

A bunch of different 'vibes' for my CV. Loaded by `make_all.`.

### `make_all.py`

Calls `cvibes` function using `CurriculumVitae.yaml` and `vibes.yaml` to generate various CVs.

### `includes/`

Assets not specific to a theme. e.g. picures of my face. References in `CurriculumVitae.yaml` and `vibes.yaml`

### `index.html.jinja`

Jinja template for making a index page for gh-pages. Not related to `cvibes`

### `make_index.py`

Makes index from `index.html.jinja`. Not related to `cvibes`

