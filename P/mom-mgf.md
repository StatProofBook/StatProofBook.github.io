---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 07:51:00

title: "Moment in terms of moment-generating function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "Moment in terms of moment-generating function"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "Moment in terms of Moment Generating Function"
    in: "ProofWiki"
    pages: "retrieved on 2020-08-19"
    url: "https://proofwiki.org/wiki/Moment_in_terms_of_Moment_Generating_Function"

proof_id: "P153"
shortcut: "mom-mgf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a scalar [random variable](/D/rvar) with the [moment-generating function](/D/mgf) $M_X(t)$. Then, the $n$-th [raw moment](/D/mom-raw) of $X$ can be calculated from the moment-generating function via

$$ \label{eq:mom-mgf}
\mathrm{E}(X^n) = M_X^{(n)}(0)
$$

where $n$ is a positive integer and $M_X^{(n)}(t)$ is the $n$-th derivative of $M_X(t)$.


**Proof:** Using the [definition of the moment-generating function](/D/mgf), we can write:

$$ \label{eq:mom-mgf-s1}
M_X^{(n)}(t) = \frac{\mathrm{d}^n}{\mathrm{d}t^n} \mathrm{E}(e^{tX}) \; .
$$

Using the power series expansion of the exponential function

$$ \label{eq:exp-ps}
e^x = \sum_{n=0}^\infty \frac{x^n}{n!} \; ,
$$

equation \eqref{eq:mom-mgf-s1} becomes

$$ \label{eq:mom-mgf-s2}
M_X^{(n)}(t) = \frac{\mathrm{d}^n}{\mathrm{d}t^n} \mathrm{E}\left( \sum_{m=0}^\infty \frac{t^m X^m}{m!} \right) \; .
$$

Because the [expected value is a linear operator](/P/mean-lin), we have:

$$ \label{eq:mom-mgf-s3}
\begin{split}
M_X^{(n)}(t) &= \frac{\mathrm{d}^n}{\mathrm{d}t^n} \sum_{m=0}^\infty \mathrm{E}\left( \frac{t^m X^m}{m!} \right) \\
&= \sum_{m=0}^\infty \frac{\mathrm{d}^n}{\mathrm{d}t^n} \frac{t^m}{m!} \mathrm{E}\left( X^m \right) \; .
\end{split}
$$

Using the $n$-th derivative of the $m$-th power

$$ \label{eq:dndx-xm}
\frac{\mathrm{d}^n}{\mathrm{d}x^n} x^m = \left\{
\begin{array}{rl}
m^{\underline{n}} \, x^{m-n} \; , & \text{if} \; n \leq m \\
0 \; , & \text{if} \; n > m \; .
\end{array}
\right.
$$

with the falling factorial

$$ \label{eq:fact-fall}
m^{\underline{n}} = \prod_{i=0}^{n-1} (m-i) = \frac{m!}{(m-n)!} \; ,
$$

equation \eqref{eq:mom-mgf-s3} becomes

$$ \label{eq:mom-mgf-s4}
\begin{split}
M_X^{(n)}(t) &= \sum_{m=n}^\infty \frac{m^{\underline{n}} \, t^{m-n}}{m!} \mathrm{E}\left( X^m \right) \\
&\overset{\eqref{eq:fact-fall}}{=} \sum_{m=n}^\infty \frac{m! \, t^{m-n}}{(m-n)! \, m!} \mathrm{E}\left( X^m \right) \\
&= \sum_{m=n}^\infty \frac{t^{m-n}}{(m-n)!} \mathrm{E}\left( X^m \right) \\
&= \frac{t^{n-n}}{(n-n)!} \mathrm{E}\left( X^n \right) + \sum_{m=n+1}^\infty \frac{t^{m-n}}{(m-n)!} \mathrm{E}\left( X^m \right) \\
&= \frac{t^0}{0!} \, \mathrm{E}\left( X^n \right) + \sum_{m=n+1}^\infty \frac{t^{m-n}}{(m-n)!} \mathrm{E}\left( X^m \right) \\
&= \mathrm{E}\left( X^n \right) + \sum_{m=n+1}^\infty \frac{t^{m-n}}{(m-n)!} \mathrm{E}\left( X^m \right) \; .
\end{split}
$$

Setting $t = 0$ in \eqref{eq:mom-mgf-s4} yields

$$ \label{eq:mom-mgf-s5}
\begin{split}
M_X^{(n)}(0) &= \mathrm{E}\left( X^n \right) + \sum_{m=n+1}^\infty \frac{0^{m-n}}{(m-n)!} \mathrm{E}\left( X^m \right) \\
&= \mathrm{E}\left( X^n \right)
\end{split}
$$

which conforms to equation \eqref{eq:mom-mgf}.