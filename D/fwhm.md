---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 05:40:00

title: "Full width at half maximum"
chapter: "General Theorems"
section: "Probability theory"
topic: "Measures of statistical dispersion"
definition: "Full width at half maximum"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Full width at half maximum"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-19"
    url: "https://en.wikipedia.org/wiki/Full_width_at_half_maximum"

def_id: "D91"
shortcut: "fwhm"
username: "JoramSoch"
---


**Definition:** Let $X$ be a continuous [random variable](/D/rvar) with a unimodal [probability density function](/D/pdf) $f_X(x)$ and [mode](/D/mode) $x_M$. Then, the full width at half maximum of $X$ is defined as

$$ \label{eq:FWHM}
\mathrm{FHWM}(X) = \Delta x = x_2 - x_1
$$

where $x_1$ and $x_2$ are specified, such that

$$ \label{eq:x12}
f_X(x_1) = f_X(x_2) = \frac{1}{2} f_X(x_M) \quad \text{and} \quad x_1 < x_M < x_2 \; .
$$