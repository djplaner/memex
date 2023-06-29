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

# Understanding Sharepoint

See also: [[computing]]

Aim here is to document and ponder some experiments with Sharepoint for the purposes of supporting the work of a small (learning/curriculum) design group.

A SharePoint site (web site?) supports a number of different items

| Item | Description |
| ---- | ----------- |
| List | |
| Document Library | "Filing cabinent" place to organise files and folders |
| Page | |
| Space | |
| News post | |
| News link| |
| Plan | |
| App | |

Limits  
- Number of items that can be viewed - 5,000 or so and performance is a pain, including syncing
  - No more than 20,000 files in a single library 
  - Create multiple libraries
- 400 character SharePoint URL limit - including length of site name, document library name, folders, and file names
  - Use short names
  - Flatten the folder hierarchy 
  - Consider using metadata
- Windows 256 character path limit - problem when syncing to PCs 
  - Don't sync (IMHO problematic)
  - Flatten the folder hierarchy 
  - Use metadata 
- 300,000 item sync limit on OneDrive sync 

## Mental model 

- A Microsoft Team has a SharePoint site. A SharePoint site can be created other ways. 
- Every SharePoint site has 1 default document library 
- Can create many. 

## Library (aka document library)

- where you store your documents in SharePoint, used to organise documents
- Every SharePoint site has one document library when created 
- Multiple can be created 
- Library can have up to 30 million files/folders - but more than 100,000 causes limitations 
- Permissions can be set for a library
- metadata created at the library level


## Lists 

- "for non-document information you would typically store in Excel" - a table of information
- must be created manually on a SharePoint site
- Support storing documents via the attachement capability - but without normal document management capabilities (version history, check-in/check-out)
- There is a list app - essentially a Home for all the lists you have across tenant sites
- Can create a personal list associated with your onedrive 

Why you should [never attach documents to a SharePoint list](https://sharepointmaven.com/why-you-should-never-use-sharepoint-lists-for-storing-files-and-attachments/)

1. Lack of document management features
2. Lack of version history on the attached files 
3. Now way to organise attachments or apply document specific metadata 
4. Can't upload multiple attachements at once (classic list only)

Might be a good idea to do this for some application, but **not** when storing multiple documents for clients/projects.

## Document set 

> Create a document set when you want to manage multiple documents as a single work product. 

e.g. when you want to create a project

- a folder with metadata
- is given a purpose specific name
- items stored within the folder can have metadata assigned
- Additional features of a document set are 
  - WElcome page - displaying folder-level metadata 
  - Ability to inherit metadata 
  - Unique permission for each data set
  - Ability to search across document sets  

How to set up document sets 

1. Enable document sets 
2. Create a document set content type
3. Add content type to the document library
4. Create metadata columns 
5. Add metadata to the content type 


## Metadata 




## Sources 

- [Document sets - the hidden gem of sharepoint](https://sharepointmaven.com/document-sets-hidden-gem-sharepoint/)
- [What are Microsoft lists](https://sharepointmaven.com/what-are-microsoft-lists/)
- [Why you should never attach documents in a SharePoint list](https://sharepointmaven.com/why-you-should-never-use-sharepoint-lists-for-storing-files-and-attachments/)
- [Lists vs libraries: sharepoint online](https://sharepointmaven.com/lists-vs-libraries-in-sharepoint-online/)
- [Folder vs library](https://sharepointmaven.com/folder-vs-library-sharepoint/)
- [5 limitations of SharePoint online](https://sharepointmaven.com/top-5-limitations-of-sharepoint-online/)
- [Document management in sharepoint without folders - introducing metadata](https://sharepointmaven.com/document-management-in-sharepoint-without-folders-introduction-to-metadata/)
- [How to explain SharePoint metadata to employees in 5 easy steps](https://sharepointmaven.com/explain-sharepoint-metadata-employees-5-easy-steps/)

[//begin]: # "Autogenerated link references for markdown compatibility"
[computing]: ../computing "Computing"
[//end]: # "Autogenerated link references"