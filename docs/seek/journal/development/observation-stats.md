---
title: Observation stats
type: development
tags:
- observations
- computational-component
---

??? note "Current status"

    Generating early observation stats for life lists. 

    Issue with eBird and iNaturalist observations not include the same data for each observation, in particular `wikilinks-scientific-name` - making it difficult to do simple stats e.g. # obs / # species

    Adding `wikilink-scientific-name` to `eBird.py`

## Purpose

As part of [[wood-duck-observations]] Add appropriate statistics to the life list pages ([[plant-life-list]], [[bird-life-list]], [[other-fauna-life-list]]) e.g. # of species, # of observations, # of different types of species (e.g. native, invasive etc), first and most recent observations etc.

Requires updates to `importObservations`

## Development plan

1. Complete exploration

    - Answer the data questions below

2. Implement stats experiments using existing format for species and observation bubbles (don't do much - proof of concept)
3. Update the format of the bubbles for observations and species (probably fixing other related problems)

    - generate new life lists that fit the new python based life list generation 
    - Be clear about the use of `type` etc in front matter to identify bubbles
    - Include more raw data from observation source in front matter
    - Enable the ability to update these bubbles based on both observation source and editing in Foam
    - Add open graph information to species and observation pages?

## Exploration

### What importObservations does

```python
    # import eBird observations and generate any new observations and species pages required
    eBirdObs = importeBird()
    # import iNaturalist observations and generate any new observations and species pages required
    iNatObs = importiNaturalist()

    # update the list list files based on bubble contents 
    #   ignore data imported from CSV files, rely just on bubble contents
    replaceListForLifeLists()
```

### If and where is this data currently available? 

- `importObservations::replaceListForLifeLists` is the harness for generating life lists
- uses `observations::displayObservationsIndex` to generate the content added to the life list

    - is passed a dict `observations`

- `observations::renderObservationsIndex` does the actual work by

    - Extracting species `observations::extractSpecies`
    - Generating unique output for each observation type `observations::generateSpeciesTableContent`

        Because there are different types of observations with different data structures

**Answer** Generating this information on contents of Bubbles - i.e. after observations imported.

### What type of data is kept in bubbles for species and observations?

How do we

- Count the number of species for a particular type (plant, bird, other-fauna)?
    
    - For observation bubbles (type=observation) the `observation-type`  front matter identifies the type
    - For species bubbles (type=<species_type>) indicates a species of that type (<species_type> matches the life lists)
- How to count the number of observations for each?

    - Get the species bubbles, then count the observations per species
- How to identify the first/last observations?

    - Loop through all species and then observations, tracking first and last
    - Could also generate annual counts (# observations per year)

**Answer** `observations:generateLifeListStats()` does it with simply Python

### Lack of commonality in bubble data

**Identify current bubble data**

Raw data is stored in yaml "dict" `observation_data` for all services.

<div class="grid cards" markdown>

-   __eBird__

    ----

    common-name: "Australasian Figbird"<br />
    wikilink-common-name: "australasian-figbird"<br />
    scientific-name: "Sphecotheres vieilloti"<br />
    taxonomic-order: "19489"<br />
    latitude: -27.538546<br />
    longitude: 152.055977<br />
    date: "2024-09-06"<br />
    human-date: "Friday, 06 September 2024"<br />
    time: "09:01 AM"<br />
    county: "Lockyer Valley"<br />
    location: "Postman’s Ridge"<br />


-   __iNaturalist__

    ----

    common-name: "Dollarbird"<br />
    wikilink-common-name: "dollarbird"<br />
    wikilink-scientific-name: "dollarbird"<br />
    scientific-name: "Eurystomus orientalis"<br />
    latitude: -27.5385416667<br />
    longitude: 152.0551<br />
    human-date: "01:38 PM Tuesday, 13 January 2026"<br />
    location: "Postmans Ridge, QLD, AU"<br />
    created_at: "2026-01-14 02:26:43 UTC"<br />
    updated_at: "2026-01-14 02:38:19 UTC"<br />
    quality-grade: "research" <br />
    url: "https://www.inaturalist.org/observations/334676162"<br />
    description: "nan"<br />
    num_identification_agreements: "1"<br />
    taxon_name: "Aves"<br />

</div>

**Decide on what common (base) model to adopt**

Considerations

- the ability to modify the observation data as observations change, but not remove any local edits

    - [ ] yaml/observation_data should handle that
    - [ ] add a HTML comment "macro" around the observation data generated by `importObservation`
- [ ] ensure observation service specific information is included (e.g. iNaturalist reviews)
- [ ] Update the YAML `description:` to be shorter
- [ ] add observations to search generation
- [ ] add observations to network map
- [ ] make standard observation service data as similar as possible

    - wikilink-scientific-name - add to eBird
    - eBird - ?? url

## Representation

[//begin]: # "Autogenerated link references for markdown compatibility"
[wood-duck-observations]: ../../../colophon/wood-duck-observations "Wood Duck observations"
[plant-life-list]: ../../../sense/Observations/plant-life-list "Plant life list"
[bird-life-list]: ../../../sense/Observations/bird-life-list "Bird life list"
[other-fauna-life-list]: ../../../sense/Observations/other-fauna-life-list "Other-Fauna life list"
[//end]: # "Autogenerated link references"