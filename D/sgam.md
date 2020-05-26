---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-26 23:36:00

title: "Standard gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
definition: "Standard gamma distribution"

sources:
  - authors: "JoramSoch"
    year: 2017
    title: "Gamma-distributed random numbers"
    in: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    pages: "retrieved on 2020-05-26"
    url: "https://github.com/JoramSoch/MACS/blob/master/MD_gamrnd.m"
    doi: "10.5281/zenodo.845404"

def_id: "D64"
shortcut: "sgam"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to have a standard gamma distribution, if $X$ follows a [gamma distribution](/D/gam) with shape $a > 0$ and rate $b = 1$:

$$ \label{eq:sgam}
X \sim \mathrm{Gam}(a, 1) \; .
$$