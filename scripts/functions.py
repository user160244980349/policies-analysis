import re
import os
from os import walk
from os.path import join, isfile, abspath
from IPython.display import Image
# from scripts.groups import groups


def offline_image(fig):
    return Image(fig.to_image(format='png', width=1200, height=700, scale=1))


def files(path: str, pattern: str):
    path = abspath(path)
    fs = []
    for dir_path, dir_names, file_names in walk(path):
        fs.extend([join(dir_path, f) for f in file_names if re.match(pattern, f) is not None])
    return fs


# def aggregate_groups(model, paragraphs, groups, file="aggregated_groups.txt"):
#     labeled_paragraphs = []
#     best = []

#     with open(os.path.join("resources", file), "w", encoding="utf-8") as f:
#         i = 0

#         for p in paragraphs:
#             affs = model.get_document_topics(p[1].lower().split(), minimum_probability=.3)
#             alffs = []
#             for g in groups:
#                 for a in affs:

#                     if a[0] in g["topics"]:
#                         labeled_paragraphs.append((g["name"], "?"))
#                         alffs.append((a[1], g["name"]))

#             best.extend([a[1] for a in alffs])
#             i += 1

#     return labeled_paragraphs, best


def resolve_group_name(id, groups):
    for g in groups:
        if id == g["id"]:
            return g["name"]
        
    return None
