---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-26 11:20:00

title: "Law of total variance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Law of total variance"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Law of total variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-11-26"
    url: "https://en.wikipedia.org/wiki/Law_of_total_variance#Proof"

proof_id: "P292"
shortcut: "var-tot"
username: "JoramSoch"
---


**Theorem:** (law of total variance, also called "conditional variance formula") Let $X$ and $Y$ be [random variables](/D/rvar) defined on the same [probability space](/D/prob-spc) and assume that the [variance](/D/var) of $Y$ is finite. Then, the sum of the [expectation](/D/mean) of the conditional variance and the [variance](/D/var) of the conditional expectation of $Y$ given $X$ is equal to the [variance](/D/var) of $Y$:

$$ \label{eq:var-tot}
\mathrm{Var}(Y) = \mathrm{E}[\mathrm{Var}(Y \vert X)] + \mathrm{Var}[\mathrm{E}(Y \vert X)] \; .
$$


**Proof:** The [variance can be decomposed into expected values](/P/var-mean) as follows:

$$ \label{eq:var-tot-s1}
\mathrm{Var}(Y) = \mathrm{E}(Y^2) - \mathrm{E}(Y)^2 \; .
$$

This can be rearranged into:

$$ \label{eq:var-tot-s2}
\mathrm{E}(Y^2) = \mathrm{Var}(Y) + \mathrm{E}(Y)^2 \; .
$$

Applying the [law of total expectation](/P/mean-tot), we have:

$$ \label{eq:var-tot-s3}
\mathrm{E}(Y^2) = \mathrm{E}\left[ \mathrm{Var}(Y \vert X) + \mathrm{E}(Y \vert X)^2 \right] \; .
$$

Now subtract the second term from \eqref{eq:var-tot-s1}:

$$ \label{eq:var-tot-s4}
\mathrm{E}(Y^2) - \mathrm{E}(Y)^2 = \mathrm{E}\left[ \mathrm{Var}(Y \vert X) + \mathrm{E}(Y \vert X)^2 \right] - \mathrm{E}(Y)^2 \; .
$$

Again applying the [law of total expectation](/P/mean-tot), we have:

$$ \label{eq:var-tot-s5}
\mathrm{E}(Y^2) - \mathrm{E}(Y)^2 = \mathrm{E}\left[ \mathrm{Var}(Y \vert X) + \mathrm{E}(Y \vert X)^2 \right] - \mathrm{E}\left[ \mathrm{E}(Y \vert X) \right]^2 \; .
$$

With the [linearity of the expected value](/P/mean-lin), the terms can be regrouped to give:

$$ \label{eq:var-tot-s6}
\mathrm{E}(Y^2) - \mathrm{E}(Y)^2 = \mathrm{E}\left[ \mathrm{Var}(Y \vert X) \right] + \left( \mathrm{E}\left[ \mathrm{E}(Y \vert X)^2 \right] - \mathrm{E}\left[ \mathrm{E}(Y \vert X) \right]^2 \right) \; .
$$

Using the [decomposition of variance into expected values](/P/var-mean), we finally have:

$$ \label{eq:var-tot-s7}
\mathrm{Var}(Y) = \mathrm{E}[\mathrm{Var}(Y \vert X)] + \mathrm{Var}[\mathrm{E}(Y \vert X)] \; .
$$