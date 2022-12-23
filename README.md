# About "Technique Son"


## How to build the book

This book is written in RMarkdown. To build or serve the book, you must install :

+ R
  + rmarkdown
  + bookdown
+ Python
  + Numpy
  + Matplotlib

Clone the repository and run bookdown::render_book("index.Rmd", "bookdown::gitbook")

Alternatively, the book can be edited while monitoring the changes in real-time using bookdown::serve_book(".", "_book")