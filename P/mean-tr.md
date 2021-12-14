---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-07 09:03:00

title: "Expected value of the trace of a matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Expectation of a trace"

sources:
  - authors: "drerD"
    year: 2018
    title: "'Trace trick' for expectations of quadratic forms"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2021-12-07"
    url: "https://math.stackexchange.com/a/3004034/480910"

proof_id: "P298"
shortcut: "mean-tr"
username: "JoramSoch"
---


**Theorem:** Let $A$ be an $n \times n$ [random matrix](/D/rmat). Then, the [expectation](/D/mean) of the trace of $A$ is equal to the trace of the [expectation](/D/mean) of $A$:

$$ \label{eq:mean-tr}
\mathrm{E}\left[ \mathrm{tr}(A) \right] = \mathrm{tr}\left( \mathrm{E}[A] \right) \; .
$$


**Proof:** The trace of an $n \times n$ matrix $A$ is defined as:

$$ \label{eq:tr}
\mathrm{tr}(A) = \sum_{i=1}^{n} a_{ii} \; .
$$

Using this definition of the trace, the [linearity of the expected value](/P/mean-lin) and the [expected value of a random matrix](/D/mean-rmat), we have:

$$ \label{eq:mean-tr-qed}
\begin{split}
\mathrm{E}\left[ \mathrm{tr}(A) \right] &= \mathrm{E}\left[ \sum_{i=1}^{n} a_{ii} \right] \\
&= \sum_{i=1}^{n} \mathrm{E}\left[ a_{ii} \right] \\
&= \mathrm{tr}\left( \left[ \begin{matrix} \mathrm{E}[a_{11}] & \ldots & \mathrm{E}[a_{1n}] \\ \vdots & \ddots & \vdots \\ \mathrm{E}[a_{n1}] & \ldots & \mathrm{E}[a_{nn}] \end{matrix} \right] \right) \\
&= \mathrm{tr}\left( \mathrm{E}[A] \right) \; .
\end{split}
$$