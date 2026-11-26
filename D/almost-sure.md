---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-07 13:11:07

title: "Almost sure statements"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Almost sure statements"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Almost sure convergence"
    in: "Statistical Inference"
    pages: "Second edition, Section 5.5.2, p. 234"

def_id: "D251"
shortcut: "almost-sure"
username: "kjpetrykowski"
---

**Definition:** A statement about a random outcome holds almost surely, or with probability one, if the event $E$ on which it is true satisfies

$$ \label{eq:almost-sure}
p(E)=1 \; .
$$

It may fail only on an event of probability zero. In particular, random variables $Z$ and $W$ are equal almost surely if

$$ \label{eq:almost-sure-equality}
\mathrm{Pr}(Z=W)=1 \; .
$$

The probability distribution must be specified: for a statement about data $X$, this is the distribution of $X$ under the stated model.
