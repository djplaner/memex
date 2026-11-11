
import pathlib
import re

fromPath="/Users/davidjones/memex/docs/sense/landscape-garden/plants/solanum-americanum.md "
toPath="/Users/davidjones/memex/docs/sense/Observations/plant-life-list.md"

path_from = pathlib.Path(fromPath)
path_to = pathlib.Path(toPath)

relative_path = path_from.relative_to( path_to, walk_up=True)

print(f"from\n  {path_from} to\n  {path_to} gives\n rel {relative_path}")

parentRe = re.compile('^\.\.\/')
relative_path = pathlib.Path(parentRe.sub( '', str(relative_path)))

print(f"after remove first .. relative path {relative_path}")

print(f"--- same file .. stem is {relative_path.stem}")
relative_path = pathlib.Path(relative_path.stem)
print(f"stem relative path {relative_path}")
