---
backlinks:
- title: Understanding the Foam Code Base
  url: /memex/sense/Web-development/foam-dev/foam-code/understanding-foam-code-base.html
tags:
- foam-dev
- foam-code
- FLOSS
title: Foam extension manifest
type: note
---
Explorations into the Foam extension manifest file - `package.json`.

## Activation event

```json
"activationEvents": [
    "workspaceContains:.vscode/foam.json"
  ],
```

I assume this asks the question: Does the workspace contain the given file?

The contents of `foam.json` appear to be a placeholder

```json
{
  "purpose": "this file exists to tell the foam-vscode plugin that it's currently in a foam workspace",
  "future": "we may use this for custom configuration"
}
```

## Contributes

- markdownItPlugins - appears to be turning on associated plugins?
- markdown.previewStyles
- grammars - focus on wikilink (injection)?
- colors - defines colours for Foam placeholders (only entry, more evenetually??)
- views - defines some views in the VSCode UI 
- viewsWelcome - appear to define initial views for various tool panes (e.g. orphans == "No orphans found...")
- menus - apparently define when certain visual UI elements are visible
    - view/title
    - commandPalette
- commands - long list of dicts of foam commands, e.g. foam-vscode.create-note
- configuration - apart from the title defines various properties
    - foam.supportedLanguages 
    - foam.completion.label 
    - foam.completion.useAlias 
    - foam.files.ignore 
    - foam.files.notesExtensions 
    - foam.files.newNotePath 
    - foam.logging.level 
    - foam.edit.linkReferenceDefinitions
    - foam.links.sync.enable
    - foam.links.hover.enable
    - foam.openDailyNote.onStartup
    - foam.openDailyNote.fileExtension 
    - foam.openDailyNote.fileExtension
    - foam.openDailyNote.titleFormat
    - foam.openDailyNote.directory
    - foam.orphans.exclude
    - foam.placeholders.exclude
    - foam.dateSnippets.afterCompletion
    - foam.preview.embedNoteType
    - foam.graph.titleMaxLength
    - foam.graphy.style
- keybindings - only two associated with daily notes (which I don't really use)