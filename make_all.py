#!/usr/bin/env python3

from cvibes.cv import CurriculumVitae, load_json_yaml

if __name__ == "__main__":

    cv = CurriculumVitae("CurriculumVitae.yaml")
    vibes = load_json_yaml("vibes.yaml")

    # Add missing slugs to cv file.
    cv.ensluginate()


    for vibe in vibes:
        cv.generate_vibe(**vibe)
    