---
title: Data Transfer Project (Initiative)
---
The [Data Transfer Project](https://dtinit.org/documentation) has three components  (sadly Java)

1. Data models - [code](https://github.com/google/data-transfer-project/tree/master/portability-types-common/src/main/java/org/datatransferproject/types/common/models)
   - canonical formats that establish a common understanding of how to transfer data (both proprietary data and authentication formats)
   - recognises an ideal situation would be the use of interoperable APIs (e.g. ActivityPub), but not common 
   - data models clustered by industry grouping to form _Verticals_
   - ideally each vertical has a small number of defined/adopted data models
2. Company specific adapters - [code](https://github.com/google/data-transfer-project/tree/master/extensions/data-transfer)
	- Tranlate provider's API into data models, come in pairs: exporter/importer
	- Adapters for data and authentication 
	- Outside core infrastructure - writen by provider or third parties 
3. Task management - "The rest is just plumbing"