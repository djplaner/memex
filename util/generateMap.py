"""
Generate a graph from the markdown files in the repository.

Based on code (https://github.com/foambubble/foam/issues/1351#issuecomment-2206544442) by https://github.com/j6k4m8

To do
- Bring in front matter and make use of it
"""
import numpy as np
import networkx as nx
import pathlib
import re
files = list(pathlib.Path("../docs/").glob("**/*.md"))
def _extract_wikilinks(text) -> list[str]:
    return re.findall(r"\[\[(.*?)\]\]", text)

def _extract_hashtags(text) -> list[str]:
    # hash with more than two chars
    return re.findall(r"#(\w{2,})", text)

g = nx.DiGraph()
for file in files:
    fname_slug = file.stem
    with open(file, "r") as f:
        text = f.read()
        wikilinks = _extract_wikilinks(text)
        for link in wikilinks:
            link = link.split("#")[0]
            g.add_edge(fname_slug, link)

        g.add_node(fname_slug, __labels__="File")

        hashtags = _extract_hashtags(text)
        for tag in hashtags:
            g.add_edge(fname_slug, tag, __labels__="Tagged")
            g.add_node(tag, __labels__="Tag")

nx.write_graphml(g, "graph.graphml")
