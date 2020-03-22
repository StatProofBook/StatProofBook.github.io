---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-22 22:57:00

title: "Poisson distribution with exposure values"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson distribution with exposure values"
definition: "Definition"

sources:
  - authors: "Gelman A, Carlin JB, Stern HS, Dunson DB, Vehtari A, Rubin DB"
    year: 2014
    title: "Other standard single-parameter models"
    in: "Bayesian Data Analysis"
    pages: "3rd edition, ch. 2.6, p. 45, eq. 2.14"
    url: "http://www.stat.columbia.edu/~gelman/book/"

def_id: "D42"
shortcut: "poissexp"
username: "JoramSoch"
---


**Definition:** A Poisson distribution with exposure values is defined as a set of observed counts $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$, independently distributed according to a [Poisson distribution](/D/poiss) with common rate $\lambda$ and a set of concurrent exposures $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$:

$$ \label{eq:Poiss-exp}
y_i \sim \mathrm{Poiss}(\lambda x_i), \quad i = 1, \ldots, n \; .
$$