
# Duplicate Image Detection

This repository hosts a tool designed for the detection of duplicate sub-figures within a larger figure. 
Especially using in Biomedical Engineering.

## Environment Setup
Details see https://github.com/idealo/imagededup

You need update your torch first.

Next, you need to install imagededup. There are two ways to install imagededup:

- Install imagededup from PyPI (recommended):

```
pip install imagededup
```

- Install imagededup from the GitHub source:

```bash
git clone https://github.com/idealo/imagededup.git
cd imagededup
pip install "cython>=0.29"
python setup.py install
```  

## How to use
You can use /split/split_image.py or /split/split_png.py to split the big figure into multi sub-figures.

Then copy the folder (e.g., test_lisa) to /imagededup/tests/data.

Finally, use /imagededup/examples/evaluation.py to get the similar sub figure. You can tune **min_similarity_threshol** for your own need.
