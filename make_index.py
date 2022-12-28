#!/usr/bin/env python3

import jinja2
import os
import glob
import json
import re
import datetime
import pdfkit
import yaml
from render import load_json_yaml
from pathlib import Path


VIBES_FILE = "vibes.yaml"
INDEX_TEMPLATE = "index.html.jinja"


if __name__ == "__main__":

    vibes = load_json_yaml(VIBES_FILE)

    jinja_env = jinja2.environment.Environment(
        loader=jinja2.FileSystemLoader(Path(INDEX_TEMPLATE).parent)
    )

    template = jinja_env.get_template(INDEX_TEMPLATE)

    html = template.render({"vibes": vibes})
    with open("docs/index.html", "w+") as f:
        f.write(html)
