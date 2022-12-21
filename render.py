import jinja2
import os
import glob
import json
import re
import datetime
import pdfkit

# now = datetime.datetime.now()
# output_name = "test"

# env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
# template = env.get_template("base.html")
# parsed = template.render()
# print(parsed)


# with open(f"generated/html/{output_name}.html", "w") as f:
#     f.write(parsed)
]from css_html_js_minify import css_minify

STYLE_SHEETS = "../style"
TEMPLATE_PATH = "../templates"

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


def compile_template(template_path, data):
    template_path = os.path.abspath(template_path)

    env = jinja2.environment.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(template_path))
    )

    template = env.get_template(os.path.basename(template_path))

    return template.render(**data)


def html2pdf(html_path, pdf_path):
    options = {
        "page-size": "Letter",
        "margin-top": "0.35in",
        "margin-right": "0.75in",
        "margin-bottom": "0.75in",
        "margin-left": "0.75in",
        "encoding": "UTF-8",
        "enable-local-file-access": True,
        "user-style-sheet": "formatting/base.css",
    }
    with open(html_path) as f:
        pdfkit.from_file(f, pdf_path, options=options, verbose=True)


if __name__ == "__main__":
    template_file = "templates/base.html.jinja"
    filename = os.path.splitext(os.path.split(template_file)[1])[0]

    compiled = compile_template(template_file, json.load(open("CurriculumVitae.json")))
    with open("generated/html/test.html", "w+") as f:
        f.write(compiled)

    html2pdf("generated/html/test.html", "generated/pdf/test.pdf")
