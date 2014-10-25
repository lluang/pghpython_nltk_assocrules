Natural Language Toolkit and Association Rules
===============================================

This repository is for the Natural Language Toolkit and Association Rules talk given at the Pittsburgh Python Meetup on October 22, 2014.

It uses the Accident Injuries data set relased as [Open Government Data](http://www.msha.gov/OpenGovernmentData/OGIMSHA.asp) by the Mine Safety and Health Administration (MSHA). This contains data submitted as part of MSHA Form 7000-1 for all accidents, injuries and illnesses reported by mine operators and contractors since 1/1/2000.  The Accident Injuries Data Set is updated weekly.

####To use the repository,

1.  Check out quickstart if new to python and nltk
2.  Download the Accident Injuries data set and unzip it in this directory.
3.  Run 'python generate_clean_narrative_pickel.py' to create the pickle 'all_narrative_cleanup.txt'
4.  Run 'python generate_narrative_tag_pickle.py' to create the pickle 'all_narrative_tagged.txt'
5.  Open 'nltk_assocrules_pghpython.ipynb' in the IPython Notebook

Code in this repository was developed by Haoxian He (https://bitbucket.org/ethan1989111) and Louis Luangkesorn (https://github.com/lluang)

#### Quickstart
- Install `pip` [Docs](http://pip.readthedocs.org/en/latest/installing.html)
- Install `pandas` - `pip install pandas`
- Install `nltk` - `pip install nltk`
- Download NLTK Corpus
    - open py interpreter `python`
    - import the toolkit `import nltk`
    - open the download ui `nltk.download()`
    - More info [Docs](http://www.nltk.org/data.html)

