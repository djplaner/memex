---
backlinks:
- title: Teaching Digital Technologies
  url: /sense/Teaching/Digital_Technologies/teaching-digital-technologies.html
tags: computing, digital-technologies, teaching-digital-technologies
title: Satellite imagery
type: note
---
Collection of resources/ideas/projects around the use of Satellite imagery and other data.

## Links

- [NASA APIs](https://api.nasa.gov/) - intended to make NASA data accessible to application developers - hourly limit of 1,000 requests/hour
- [NASA's Earthdata developer portal](https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api)
- [Google earth engine](https://earthengine.google.com/) - with [publicly available datasets](https://developers.google.com/earth-engine/datasets/)
- Programmable Web's (retired) [list of Satellite APIs](https://web.archive.org/web/20200622070732/https://www.programmableweb.com/category/satellites/api)

## APIs

### Astronomy picture of the day (APOD)

Call `https://api.nasa.gov/planetary/apod?api_key=<yourkey>` and get JSON response with fields including: date, explanation, hdurl, media_type, title, url

### Landsat 8 imagery

`https://api.nasa.gov/planetary/earth/imagery` - returns an image

#### Request

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| lat | float | | Latitude |
| lon | float | | Longitude |
| dim | float | 0.025 | Width and height of image in degrees |
| date | YYYY-MM-DD | today | Date of image |
| api_key | string | DEMO_KEY | api.nasa.gov key for expanded usage |


#### Response