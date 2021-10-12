---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-07 09:10:00

title: "Addition of the differential entropy upon multiplication with invertible matrix"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
theorem: "Addition upon matrix multiplication"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Differential entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-07"
    url: "https://en.wikipedia.org/wiki/Differential_entropy#Properties_of_differential_entropy"

proof_id: "P261"
shortcut: "dent-addvec"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random vector](/D/rvec). Then, the [differential entropy](/D/dent) of $X$ increases additively when multiplied with an invertible matrix $A$:

$$ \label{eq:dent-addvec}
\mathrm{h}(AX) = \mathrm{h}(X) + \log |A| \; .
$$


**Proof:** By definition, the [differential entropy](/D/dent) of $X$ is

$$ \label{eq:X-dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x
$$

where $f_X(x)$ is the [probability density function](/D/pdf) of $X$ and $\mathcal{X}$ is the set of possible values of $X$.

The [probability density function of a linear function of a continuous random vector](/P/pdf-linfct) $Y = g(X) = \Sigma X + \mu$ is

$$ \label{eq:pdf-linfct}
f_Y(y) = \left\{
\begin{array}{rl}
\frac{1}{\left| \Sigma \right|} f_X(\Sigma^{-1}(y-\mu)) \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\mathcal{Y} = \left\lbrace y = \Sigma x + \mu: x \in \mathcal{X} \right\rbrace$ is the set of possible outcomes of $Y$.

Therefore, with $Y = g(X) = AX$, i.e. $\Sigma = A$ and $\mu = 0_n$, the [probability density function](/D/pdf) of $Y$ is given by

$$ \label{eq:Y-pdf}
f_Y(y) = \left\{
\begin{array}{rl}
\frac{1}{\left| A \right|} f_X(A^{-1}y) \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\mathcal{Y} = \left\lbrace y = A x: x \in \mathcal{X} \right\rbrace$.

Thus, the [differential entropy](/D/dent) of $Y$ is

$$ \label{eq:Y-dent-s1}
\begin{split}
\mathrm{h}(Y) &\overset{\eqref{eq:X-dent}}{=} - \int_{\mathcal{Y}} f_Y(y) \log f_Y(y) \, \mathrm{d}y \\
&\overset{\eqref{eq:Y-pdf}}{=} - \int_{\mathcal{Y}} \left[ \frac{1}{\left| A \right|} f_X(A^{-1}y) \right] \log \left[ \frac{1}{\left| A \right|} f_X(A^{-1}y) \right] \, \mathrm{d}y \; .
\end{split}
$$

Substituting $y = Ax$ into the integral, we obtain

$$ \label{eq:Y-dent-s2}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{X}} \left[ \frac{1}{\left| A \right|} f_X(A^{-1}Ax) \right] \log \left[ \frac{1}{\left| A \right|} f_X(A^{-1}Ax) \right] \, \mathrm{d}(Ax) \\
&= - \frac{1}{\left| A \right|} \int_{\mathcal{X}} f_X(x) \log \left[ \frac{1}{\left| A \right|} f_X(x) \right] \, \mathrm{d}(Ax) \; .
\end{split}
$$

Using the differential $\mathrm{d}(Ax) = \lvert A \rvert \mathrm{d}x$, this becomes

$$ \label{eq:Y-dent-s3}
\begin{split}
\mathrm{h}(Y) &= - \frac{\left| A \right|}{\left| A \right|} \int_{\mathcal{X}} f_X(x) \log \left[ \frac{1}{\left| A \right|} f_X(x) \right] \, \mathrm{d}x \\
&= - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x - \int_{\mathcal{X}} f_X(x) \log \frac{1}{\left| A \right|} \, \mathrm{d}x \; .
\end{split}
$$

Finally, employing [the fact](/D/pdf) that $\int_{\mathcal{X}} f_X(x) \, \mathrm{d}x = 1$, we can derive the [differential entropy](/D/dent) of $Y$ as

$$ \label{eq:Y-dent-s4}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x + \log \left| A \right| \int_{\mathcal{X}} f_X(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:X-dent}}{=} \mathrm{h}(X) + \log |A| \; .
\end{split}
$$