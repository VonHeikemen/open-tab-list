# Open Tab List

Search throught the list of opened files.

## Why?

While you can indeed search the opened files with the standard `ctrl+p` the results of your search will be affected by the fact that sublime is looking in the whole project. So I wanted something similar to the `:Buffers` command you find in [fzf.vim](https://github.com/junegunn/fzf.vim), a way of fuzzy find just the opened files with a few nice features.

* Display the current file as the first item in the list.
* Show a number ID so I can select quickly between the items.
* Preserve the order of the "view stack", so I can navigate quickly between the current file and last recently used with `ctrl+tab`.

## Getting Started

### Installation
#### Recommended (for now, 'cause is not in Package control's repository)

Install `OpenTabList` via Package Control.

1. Open the Command Palette via <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>
2. Select *Package Control: Add Repository*
3. Copy the link of this repository on the input
4. Search for `OpenTabList` and press <kbd>↲ Enter</kbd>

#### Manual

1. Clone or download this repository, (re)name the folder to `OpenTabList` if necessary.
2. Move the folder inside your sublime `/Packages`. (*Preferences > Browse Packages...*)

## Support

If you find this plugin useful and want to support my efforts, [buy me a coffee ☕](https://www.buymeacoffee.com/vonheikemen).

[![buy me a coffee](https://res.cloudinary.com/vonheikemen/image/upload/v1618466522/buy-me-coffee_ah0uzh.png)](https://www.buymeacoffee.com/vonheikemen)

