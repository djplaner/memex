
from corpus import corpus
from pprint import pprint

def test_work_history():
    """
    Testing ability to select by type and paths
    """

    print("********************\nworkHistory test\n********************")
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

def test_bubble_frontmatter():
    """
    Test ability to select bubbles by frontmatter tags
    """

    print("********************\nfrontmatter tag test\n********************")
    allBubbles = corpus( )

    singlePlantBubbles = allBubbles.get_bubble_by_type("single-plant")

    matter = {
        "type": "single-plant",
        "region": "gatton-creek-frontage"
    }

    singlePlantGattonCreekBubbles = allBubbles.get_bubbles_by_frontmatter( matter )

    print(f"Number of single-plant bubbles: {len(singlePlantBubbles)}")
    print(f"Number of single-plant bubbles in gatton-creek-frontage: {len(singlePlantGattonCreekBubbles)}")

    for plant in singlePlantBubbles:
        yaml = plant.get("yaml", {})
        title = yaml.get("title", "No title")
        region = yaml.get("region", "No region")
        plantType = yaml.get("type", "No type")
        print(f"Region: {region} \tPlant: {title} ({plantType})")


if __name__ == "__main__":
#    test_work_history()

    test_bubble_frontmatter()