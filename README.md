# Extract Reddit Page Links

Python script to extract all the links of a given page to a list

### Virtual Environment
Install virtualenv for the project (If you haven't already):

```bash
sudo pip install virtualenv virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv redditextractlinks
```

For more information on virtual environments, see [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

### Installation

```bash
git clone https://github.com/TylerNakamura/extract-reddit-page-links reddit-link-extract
cd reddt-link-extract
sudo pip install -r requirements.txt
```

### Usage

```bash
cd extract-reddit-page-links
python extract.py
```

### Contributions

Would love to take PRs
