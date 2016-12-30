# coding: utf-8

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("poster")
sns.set_style("ticks")
from sklearn.manifold import TSNE
from gen_network import mesh_clean, id2node

mesh_cats = {
        "A": "Anatomy",
        "B": "Organisms",
        "C": "Diseases",
        "D": "Chemicals and Drugs",
        "E": "Analytical, Diagnostic and Therapeutic Techniques and Equipment",
        "F": "Psychiatry and Psychology",
        "G": "Phenomena and Processes",
        "H": "Disciplines and Occupations",
        "I": "Anthropology, Education, Sociology and Social Phenomena",
        "J": "Technology, Industry, Agriculture",
        "K": "Humanities",
        "L": "Information Science",
        "M": "Named Groups",
        "N": "Health Care",
        "V": "Publication Characteristics",
        "Z": "Geographicals"
}

with open("out/mesh_embedding.txt") as fp:
    i = 0
    id2mesh = []
    embeddings = []
    for line in fp:
        if i == 0:
            i += 1
            continue
        line = line.strip().split()
        id2mesh.append(id2node[int(line[0])])
        embeddings.append([float(k) for k in line[1:]])
        i += 1
        
color_cat = dict(zip(mesh_cats.keys(), sns.color_palette("Set2", len(mesh_cats))))
mesh_color = [color_cat[list(mesh_clean[k])[0][0]] for k in id2mesh]

embeddings_np = np.array(embeddings)
model = TSNE(n_components=2, random_state=0)
#transformed_embeddings = model.fit_transform(embeddings_np)


