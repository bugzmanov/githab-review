
Purpose:


To make code-review in IDE

Steps it does:

1) Fetches origin
2) Creates diff between branches(head and base of pull request) 
3) checs out origin/base branch
4) apply patch 


 
Installation

```
git clone https://github.com/bugzmanov/github-review
cd github-review
sudo ./install-deps.sh
sudo python setup.py install
```

Usage

In clean working directory

```
github-review <github pull request http url>
```



