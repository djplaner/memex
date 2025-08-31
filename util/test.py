
from corpus import corpus
from pprint import pprint

workHistory = corpus( 
    type="work-history",
    paths=["sense/landscape-garden/work-files/"]
    )

print(f"Number of work history items: {len(workHistory)}")

#-- count the number of regions

regions = {}

for item in workHistory:
    yaml = item.get("yaml", {})
    if not yaml:
        continue
    region = yaml.get("region", "unknown")
    # convert region to a list, if not already
    if not isinstance(region, list):
        region = [region]
    for r in region:
        print(f"Region: {r}")
        print("regions")
        pprint( regions)
        print("region keys", list(regions.keys()))
        #-- extract keys of regions
        if r not in list(regions.keys()):
            regions[r] = 0
        regions[r] += 1
        print()

print("Regions and their counts:")
pprint(regions)