---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-01-10 17:44:46

title: "Sample standard deviation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Measures of statistical dispersion"
definition: "Sample standard deviation"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Erwartungswerte"
    in: "Wahrscheinlichkeitstheorie und Frequentistische Inferenz"
    pages: "Einheit (5), Folie 32"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Wintersemester+2324/Wahrscheinlichkeitstheorie+und+Frequentistische+Inferenz/5_Erwartungswerte.pdf"
  - authors: "Wikipedia"
    year: 2025
    title: "Standard deviation"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Standard_deviation#Estimation"

def_id: "D214"
shortcut: "std-samp"
username: "JoramSoch"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the sample standard deviation of $x$ is given by

$$ \label{eq:var-std}
\hat{\sigma} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

and the unbiased sample standard deviation of $x$ is given by

$$ \label{eq:var-samp-unb}
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

where $\bar{x}$ is the [sample mean](/D/mean-samp).