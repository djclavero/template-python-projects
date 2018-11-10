# Install packages in [SUBLIME TEXT 3](https://www.sublimetext.com/) 

Install a package in Sublime Text 3 using **Package Control**

by djclavero@yahoo.com 

---

Open the Command Palette with **CRTL+SHIFT+P**


### Print to HTML

In Command Palette execute *Install*

Look for 'Print to HTML'

Use it with **ALT+SHIFT+P**


### MarkdownEditing

In Command Palette execute *Install*

Look for 'MarkdownEditing'

Use 'Markdown GFM'


### Markdown Preview

In Command Palette execute *Install*

Look for 'Markdown Preview'

Configuration:

* Edit your "Key Bindings - User" in the Menu
* Add the following entrey:

```
{ "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"} }
```

Then you can use **ALT+M** to generate HTML preview of your document that will open in your default browser.




 