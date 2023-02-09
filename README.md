# About "Guide pratique de la prise de son et du mixage appliqués à la musique"


## How to build the book

This book is written in RMarkdown. To build or serve the book, you must install :

+ R
  + rmarkdown
  + bookdown
  + plotly
  + ggplot2
+ Python
  + Numpy
  + Matplotlib

Clone the repository and run bookdown::render_book("index.Rmd", "bookdown::gitbook") to generate the html version. Run bookdown::render_book("index.Rmd", "bookdown::pdf_book") to generate the pdf version. I recommand to delete the _book and _bookdown folder before compiling the pdf document (sometimes pictures don't show up otherwise).

Alternatively, the book can be edited while monitoring the changes in real-time using bookdown::serve_book(".", "_book")