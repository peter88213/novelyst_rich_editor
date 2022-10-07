[Project homepage](https://peter88213.github.io/novelyst_rich_editor)

--- 

A [novelyst](https://peter88213.github.io/novelyst/) multi-scene "rich text" editor plugin based on the *tkinter.Text* widget.

### Installation

If [novelyst](https://peter88213.github.io/novelyst/) is installed, the setup script auto-installs the *novelyst_editor* plugin in the *novelyst* plugin directory.

The plugin adds an "Edit" entry to the *novelyst* "Scene" menu. 

## Operation

### Launch the scene editor

- Open a scene editor window by double-clicking on a scene or via the **Scene > Edit** menu entry when a scene is selected, or by hitting the *Enter* key.
- If the project is locked, editor windows cannot be opened.
- If you choose a scene already open, the window will be brought to the foreground.

### Select text

- Select a word via double-clicking.
- Select a paragraph via triple-clicking.
- Extend the selection via **Shift-Arrow**.
- Extend the selection to the next word via **Ctrl-Shift-Arrow**.
- **Ctrl-A** selects the whole text.

### Copy/Paste text

- **Ctrl-C** copies the selected text to the clipboard.
- **Ctrl-X** cuts the selected text and moves it to the clipboard.
- **Ctrl-V** pastes the clipboard text content to the cursor position.

### Format text

- **Ctrl-I** formats the selected text "Italic". If the selection is already italic, remove formatting.
- **Ctrl-B** formats the selected text "Bold". If the selection is already bold, remove formatting.
- **Ctrl-M** removes "Bold" and "Italic" formatting from the selection.

*Be sure not to nest markup by accident.*

#### A note about formatting text

It is assumed that very few types of text markup are needed for a novel text:

- *Emphasized* (shown as italics).
- *Strongly emphasized* (shown as bold).
- *Citation* (paragraph visually distinguished from body text).

When exporting to ODT format, *novelyst* replaces these formattings as follows: 

- Italic text is formatted as *Emphasized*.
- Bold text is formatted as *Strong emphasized*. 
- Paragraphs starting with `> ` are formatted as *Quote*.

### Undo/Redo

- **Ctrl-Z** undoes the last editing. Multiple undo is possible.
- **Ctrl-Y** redoes the last undo. Multiple redo is possible.

### Split a scene

Via **File > Split at cursor position** or **Ctrl-Alt-S** you can split the scene at the cursor position. 

- All the text from the cursor position is cut and pasted into a newly created scene. 
- The new scene is placed after the currently edited scene.
- The new scene is appended to the currently edited scene.
- The new scene has the same status as the currently edited scene.  
- The new scene is of the same type as the currently edited scene.  
- The new scene has the same viewpoint character as the currently edited scene.  


### Word count

- The scene word count is displayed at the status bar at the bottom of the window.
- By default, word count is updated manually, either by pressing the **F5** key, or via the **Word count > Update** menu entry.
- The word count can be updated "live", i.e. just while entering text. This is enabled via the **Word count > Enable live update** menu entry. 
- Live update is disabled by the **Word count > Disable live update** menu entry. 

**Please note**

*Live updating the word count is resource intensive and may slow down the program when editing big scenes. This is why it's disabled by default.*

### Apply changes

- You can apply changes to the scene with **Ctrl-S**. Then "Modified" status is displayed in *novelyst*.
- If the project is locked in *novelyst*, you will be asked to unlock it before changes can be applied.

### Exit 

- You can exit via **File > Exit**, or with **Ctrl-Q**.
- When exiting the program, you will be asked for applying changes.

## License

This is Open Source software, and the *novelyst_rich_editor* plugin is licenced under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/novelyst_rich_editor/blob/main/LICENSE) file.

