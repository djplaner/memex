---
title: No title found
---
<!--
 Copyright (C) 2023 David Jones
 
 This file is part of memex.
 
 memex is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 memex is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with memex.  If not, see <http://www.gnu.org/licenses/>.
-->

# Data Transfer Project (Initiative)



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