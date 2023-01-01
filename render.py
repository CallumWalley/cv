#!/usr/bin/env python3

import jinja2
import os
import glob
import json
import re
import datetime
import pdfkit
import yaml
from slugify import slugify
from pathlib import Path
import sass

CV_FILE = "CurriculumVitae.yaml"
VIBES_FILE = "vibes.yaml"
TEMPLATES = "templates"


def ensluginate(obj):
    # Order in which to use key as slug.
    key_order = ["slug", "name", "organization", "institution", "title", "language"]
    for category in obj.values():
        if isinstance(category, dict):
            continue
        for item in category:
            for key in key_order:
                if key in item:
                    item["slug"] = slugify(item[key])
                    continue


def return_filtered(obj, filter_value):

    ensluginate(obj)
    if isinstance(filter_value, bool):
        # If true, return all unmodified.
        return obj if filter_value else []
    elif isinstance(filter_value, (tuple, list, set)):
        return (
            dict(filter(lambda x: (get_slug(x) in filter_value), obj.items()))
            if isinstance(obj, dict)  # Unpack if dict
            else list(filter(lambda x: (get_slug(x) in filter_value), obj))
        )
    else:
        return {
            key: return_filtered(obj[key], value) if key in obj else []
            for key, value in filter_value.items()
        }


def load_json_yaml(path):
    with open(path, "r") as f:
        suffix = Path(path).suffix
        if suffix in [".json"]:
            return json.load(f)
        elif suffix in [".yaml", ".yml"]:
            return yaml.load(f, Loader=yaml.SafeLoader)
        else:
            raise Exception(f"'{path}' doesn't look like yaml or json.")


def generate_vibe(vibe, cv):

    # Filter CV data.
    cv = return_filtered(cv, vibe["filter"])
    # always generate html.
    template_path = os.path.abspath(vibe["template"])

    jinja_env = jinja2.environment.Environment(
        loader=jinja2.FileSystemLoader(Path(template_path).parent)
    )

    template = jinja_env.get_template(Path(template_path).name)

    html = template.render(**cv)

    for output in vibe["output"]:
        file_type = Path(output).suffix
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        if file_type == ".html":
            with open(output, "w+") as f:
                f.write(html)
            print(f"Created {output}")
        elif file_type == ".pdf":
            html2pdf(html, output)
            print(f"Created {output}")
        else:
            print(f"File type {file_type} no instructions to make.")
    return


def generate_css():
    sass.compile(dirname=("style", "docs"), output_style="compressed")


def html2pdf(html, pdf_path):
    options = {
        "page-size": "Letter",
        "margin-top": "0.35in",
        "margin-right": "0.75in",
        "margin-bottom": "0.75in",
        "margin-left": "0.75in",
        "encoding": "UTF-8",
        "enable-local-file-access": True,
        "user-style-sheet": "style/base.css",
    }
    pdfkit.from_string(html, pdf_path, options=options, verbose=True)


if __name__ == "__main__":

    cv = load_json_yaml(CV_FILE)
    vibes = load_json_yaml(VIBES_FILE)

    for vibe in vibes:
        generate_vibe(vibe, cv)

    generate_css()
# def load_data(json_glob):
#     def _ordinal_day(e):
#         return -datetime.date(
#             e.get("year", 1), e.get("month", 1), e.get("day", 1)
#         ).toordinal()

#     datas = []
#     for json_file in glob.glob(json_glob):
#         with open(json_file) as f:
#             data = json.load(f)
#             data = {k: sorted(v, key=_ordinal_day) for k, v in data.items()}
#             entries = list(data.values())[0]
#             for entry in entries:

#                 if "day" in entry and "month" in entry and "year" in entry:
#                     entry_time = datetime.datetime(
#                         entry["year"], entry["month"], entry["day"]
#                     )
#                     if entry_time > now:
#                         entry["year"] = "{} (to appear)".format(entry["year"])
#                     if entry_time > now - datetime.timedelta(days=365):
#                         entry["recent"] = True

#                 if "authors" in entry:
#                     authors = entry["authors"].split(", ")
#                     if len(authors) > 11:
#                         n_to_show = 4
#                         if "Colin Raffel" in authors[n_to_show]:
#                             n_to_show += 1
#                         while "*" in authors[n_to_show]:
#                             n_to_show += 1
#                         entry["authors"] = ", ".join(
#                             entry["authors"].split(", ")[:n_to_show]
#                         )
#                         n_additional = len(authors) - n_to_show
#                         entry["authors"] += f", and {n_additional} others"
#                         if "Colin Raffel" not in entry["authors"]:
#                             entry["authors"] += " including Colin Raffel"

#                     entry["authors"] = re.sub(
#                         r"(Colin Raffel)", r"<b>\1</b>", entry["authors"]
#                     )

#                 if "end" in entry and entry["end"] == "now":
#                     entry["current"] = True
#             datas.append(data)

#     return dict((k, v) for d in datas for (k, v) in d.items())
