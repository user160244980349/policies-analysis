from collections import Counter
from scripts.functions import aggregate_groups
from scripts.groups import groups
from scripts.lda import LDA
from scripts.functions import files
import os, json



def main():

    policies = []

    os.mkdir(os.path.abspath(f"./keywords"))

    fs = files("resources/datasets/plain_policies", r".*")
    for f in fs:
        with open(f, "r", encoding="utf-8") as fl:
            policies.append({"policy": os.path.basename(f), "paragraphs": [p for p in fl.read().split("\n") if len(p) >= 100]})

    words = ["notif", "chang", "updat", "breach"]

    for w in words:
        with open(os.path.abspath(f"./keywords/{w}.json"), "w") as stream:
            json.dump(catch(w, policies), stream)
        

def catch(word, policies):
    catch_list = []
    for pol in policies: 
        p = {"policy": pol["policy"], "paragraphs": []}
        for par in pol["paragraphs"]:
            if word in par:
                p["paragraphs"].append(par)
        catch_list.append(p)
    return catch_list


if __name__ == "__main__":
    main()