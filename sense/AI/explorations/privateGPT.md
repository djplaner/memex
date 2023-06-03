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

# PrivateGPT 

See also: [[AI]]

Log of an experiment to get [privateGPT](https://github.com/imartinez/privateGPT) working locally. HT to Chris Bigum and [this post](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/?utm_source=feedly&utm_medium=rss&utm_campaign=create-privategpt-local-llm)

## Process overview 

1. [Preparation](#preparation) - install the software on my laptop ✔ 
2. [Initial testing](#initial-testing) - get the software working with the supplied test file ✔ 
3. [Examine possible refinements](#examine-possible-refinements) - it's a work in progress with a lot of people experimenting, what refinements exist and are doable? 🚧 - all require a bit of work - for later
4. [Test with blog posts](#test-with-blog-posts) - Use the ??? posts on my blog as the first major test 🚧 

## Preparation 

Preparation
1. Clone the repo. ✔ 
   -  GitHub desktop FTW
2. Set up virtual environment. ✔
   - `pip install virtualenv`
   - In the local repo, 
     - `py -m venv env`
     - `. ./env/Scripts/activate`


Specific to privateGPT

3. Install requirements. ✔ 
   - using `requirements.txt` not working (thank you MOE security rules that don't like bash.exe)
   - attempting to manually install with Python 
     - Initially not paying attention to the specific versions - this may bite me on the...which given how long a fresh install takes is not a good thing.
   - First install didn't work for ChromaDb -- needed v14 or later of [C++ build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
     - Apparently including a ~2Gb download/install
4. Download and install the recommended LLM  ✔
	- **hint** Do this early will take some time
5. Modify the environment file ✔
6. Do a test - apparently comes with the state of the union ✔
   - `python ingest.py` and the fun begins - see [Initial testing](#initial-testing)

## Initial testing

Aim here is to run using just the provided [single text file](https://github.com/imartinez/privateGPT/blob/main/source_documents/state_of_the_union.txt). 

- forgot to rename the `env.example` file to `.env` - fixed
- `sentence_transformers` not installed, suggesting more issues with my manual install of requirements - perhaps due to the Visual C++ build tools update issue?
- `python -m pip install sentence_transformers` - fixed, but due to the local env, this takes a while given a lot of requirements
- Will do a manual install on all after chromdb, just in case, listing those that did require install
  - `llama-cpp-python`

  Success

![First test run success with ingest](images/ingestSuccess.png)

But loading the module gets an error 
bash```
  File "C:\Users\..\privateGPT\env\lib\site-packages\gpt4all\pyllmodel.py", line 141, iload_model
    llmodel.llmodel_loadModel(self.model, model_path.encode('utf-8'))
OSError: exception: access violation reading 0x000000D4AABF0000
```

Try the "Git Bash/UTF-8" fix - add the following to start of `ingest.py` - fixed
python```
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
```

![PrivateGPT answering question based on supplied text file](images/privateGPTTestWorking.png)


## Examine possible refinements

Some possible refinements include  -- all require some significant tinkering

- Different LLMs, possibilities include 
  - [h2oGPT](https://github.com/h2oai/h2ogpt#windows-1011) - appears to require a very different install than the binary for the default LLM (i.e. complexity)
- [Chroma collections](https://github.com/imartinez/privateGPT/discussions/298)
  - Chroma - the vector database used here - supports "collections" to separate out document types - questions exist how to integrate in privateGPT
- Add a web (or other) interface (beyond the command line)
  - [Example/attempt](https://github.com/imartinez/privateGPT/discussions/487) to get ChatGPT-4 to write a [streamlit version](https://streamlit.io/)


### Streamlit experiment

- Install streamlit `pip install streamlit`
- Copy and paste the code from the example 
- `streamlit run streamLitPrivateGPT.py`

Running into problems with MOE configuration stopping Streamlit being run

## Test with blog posts 

[My blog](https://djon.es/blog/) is probably the biggest collection of personal text I have (my Zotero library is another option)

1. Export posts 
2. Decide what format to convert to: file format and file structure (separate files?)
   - separate text files seems the go 
3. Convert to that format and place in privateGPT - see [Blog posts to import files](#blog-posts-to-import-files)


## Blog posts to import files

### Parsing and writing files 

Uses [feedparser Python library](https://feedparser.readthedocs.io/en/latest/) ends up with individual posts in array of hashes with the following keys 

- Check out content titles for a few more posts to see if/how it changes - appears to be HTML
  - Anything with a URL `p=<wp_post_id>` appears to be draft
- Figure what files to write - maybe HTML with links, title etc.
  - 1425 files written

| Keys | Content/Description | 
| ---- | ------------------- |
| `title`| String - title of post   |
| `content`| List of dicts **do more**   |
| `link`| URL for the original post - using `p=<wp_post_id>`   |
| `title_detail`| FeedParserDict of information about the title, including value, type, language   |
| `links`| Dict with misc details about lnks   |
| `published`| String no value in test   |
| `published_parsed`| String, None   |
| `authors`| List of author usernames   |
| `author`| String user author name   |
| `author_detail`| Dict with more detail of author   |
| `id`| String - in first example an old CQ-PAN URL and id   |
| `guidislink`| Boolean   |
| `summary`| String empty   |
| `summary_detail`| Dict   |
| `excerpt_encoded`| String empty   |
| `wp_post_id`| String # matching link   |
| `wp_post_date`| STring date   |
| `wp_post_date_gmt`| STring date   |
| `wp_post_modified`| STring date   |
| `wp_post_modified_gmt`| STring date   |
| `wp_comment_status`| String "open"   |
| `wp_ping_status`| String "open"   |
| `wp_post_name`| String empty   |
| `wp_status`| STring draft : 346 in draft; 1439 private, 5 trash, and 5 private  |
| `wp_post_parent`| String 0   |
| `wp_menu_order`|String 0    |
| `wp_post_type`| String `post`   |
| `wp_post_password`| String empty   |
| `wp_is_sticky`| String 0   |
| `tags` | List of dicts `{ term: '', scheme: '', Label: None }` - 304 different categories, top 20 have 43 posts or more.  Uncategorised the largest with 862 (only published)|

### Ingest and query 




[//begin]: # "Autogenerated link references for markdown compatibility"
[AI]: ../AI "AI"
[//end]: # "Autogenerated link references"