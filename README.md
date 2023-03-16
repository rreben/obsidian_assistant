# obsidian_assistant
Tools to maintain and manage obsidian vault.

## Journaling
The assistant extracts certain paragraphs from the daily note files and merges them into one single file. So that you can review a given time frame more easily. This also helpful if you need to convert this information into a different file format like pdf.

## Setting up everything for development
### Virtual Evironment
We set up our virtual environment with ```virtualenv --python python3.10 venv``` and then activate this environment via ```source venv/bin/activate```.

### Setting up VSCode
We need the "Python Test Explorer" plugin to be able to discover our tests. We use the ```pytest``` testing framework.
