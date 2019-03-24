# hello_challenge
#### Library requirements
```
scrapy
functools
treelib #to create decision tree layout
json
```
#### To run scrapy with spider to crawling https://www.drukzo.nl.joao.hlop.nl/python.php dropdowns:
```
scrapy crawl hello_tree
```

#### To run from docker:
```
sudo docker run -v $(pwd):/hello_docker  hello_docker
```
#### Outputs:
Decision tree: *Tree.txt*
```
A
├── B
│   ├── F
│   │   ├── M
│   │   │   └── 1
│   │   └── N
│   │       ├── 2
│   │       └── 3
│   └── G
│       ├── O
│       │   ├── 4
│       │   └── 5
│       ├── P
│       │   ├── 6
│       │   └── 9
│       └── Q
│           ├── 7
│           └── 8
└── C
    ├── D
    │   ├── H
    │   │   └── R
    │   ├── I
    │   │   ├── S
    │   │   ├── T
    │   │   └── U
    │   └── J
    │       └── V
    └── E
        ├── K
        │   └── X
        └── L
            ├── Y
            └── Z
```
All pair combinations: *items.json*
