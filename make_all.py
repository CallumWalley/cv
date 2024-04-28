#!/usr/bin/env python3

from crass.cv import CurriculumVitae, load_json_yaml

if __name__ == "__main__":

    cv = CurriculumVitae("CurriculumVitae.yaml")
    vibes = load_json_yaml("vibes.yaml")

    for vibe in vibes:
        cv.generate_vibe(**vibe)