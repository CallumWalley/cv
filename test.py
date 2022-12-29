import render

cv = render.load_json_yaml("CurriculumVitae.json")
test_obj = {
    "general": {"a": 1, "b": 2},
    "work": [{"name": "thing1"}, {"slug": "thing2"}],
}
test_filter = {"general": True, "work": ["thing2"]}

print(test_obj)
print("after")
print(dict(render.return_filtered(test_obj, test_filter)))
