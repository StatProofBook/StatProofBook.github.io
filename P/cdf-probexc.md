---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-09-06 10:27:35

title: "Exceedance probability for a random variable in terms of cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Cumulative distribution function"
theorem: "Exceedance probability based on cumulative distribution function"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Zufallsvariablen"
    in: "Wahrscheinlichkeitstheorie und Frequentistische Inferenz"
    pages: "Einheit (3), Folie 34"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Wintersemester+2324/Wahrscheinlichkeitstheorie+und+Frequentistische+Inferenz/3_Zufallsvariablen.pdf"

proof_id: "P466"
shortcut: "cdf-probexc"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with possible values $\mathcal{X}$ and [cumulative distribution function](/D/cdf) $F_X(x)$. Then, the [exceedance probability](/D/prob-exc) that $X$ is larger than some value $x$ is

$$ \label{eq:cdf-prob-exc}
\mathrm{Pr}(X > x) = 1 - F_X(x) \; .
$$


**Proof:** Note that $\left\lbrace X \mid X > x \right\rbrace$ and $\left\lbrace X \mid X \leq x \right\rbrace$ are disjoint sets

$$ \label{eq:intersection}
\left\lbrace X \mid X > x \right\rbrace \cap \left\lbrace X \mid X \leq x \right\rbrace = \emptyset
$$

and that they comprise the set of all outcomes, i.e. the [sample space](/D/samp-spc):

$$ \label{eq:union}
\left\lbrace X \mid X > x \right\rbrace \cup \left\lbrace X \mid X \leq x \right\rbrace = \mathcal{X} = \Omega \; .
$$

Using the [second axiom of probability](/D/prob-ax), we have:

$$ \label{eq:cdf-prob-exc-s1}
\begin{split}
p(\Omega) &= 1 \\
p\left( \left\lbrace X \mid X > x \right\rbrace \cup \left\lbrace X \mid X \leq x \right\rbrace \right) &= 1 \; .
\end{split}
$$

Using the [third axiom of probability](/D/prob-ax), we get:

$$ \label{eq:cdf-prob-exc-s2}
\begin{split}
p\left( \left\lbrace X \mid X > x \right\rbrace \right) + p\left( \left\lbrace X \mid X \leq x \right\rbrace \right) &= 1 \\
p\left( \left\lbrace X \mid X > x \right\rbrace \right) &= 1 - p\left( \left\lbrace X \mid X \leq x \right\rbrace \right) \\
\mathrm{Pr}(X > x) &= 1 - \mathrm{Pr}(X \leq x) \; .
\end{split}
$$

Using the [definition of the cumulative distribution function](/D/cdf), we finally have:

$$ \label{eq:cdf-prob-exc-qed}
\mathrm{Pr}(X > x) = 1 - F_X(x) \; .
$$