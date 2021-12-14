---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-14 07:23:00

title: "Sample correlation coefficient"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
definition: "Sample correlation coefficient"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Pearson correlation coefficient"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-12-14"
    url: "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#For_a_sample"

def_id: "D168"
shortcut: "corr-samp"
username: "JoramSoch"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ and $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be [samples](/D/samp) from [random variables](/D/rvar) $X$ and $Y$. Then, the sample correlation coefficient of $x$ and $y$ is given by

$$ \label{eq:corr-samp}
r_{xy} = \frac{\sum_{i=1}^n (x_i-\bar{x}) (y_i-\bar{y})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n (y_i-\bar{y})^2}}
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp).