---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-07 10:39:00

title: "Non-invariance of the differential entropy under change of variables"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
theorem: "Non-invariance and transformation"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Differential entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-07"
    url: "https://en.wikipedia.org/wiki/Differential_entropy#Properties_of_differential_entropy"
  - authors: "Bernhard"
    year: 2016
    title: "proof of upper bound on differential entropy of f(X)"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2021-10-07"
    url: "https://math.stackexchange.com/a/1759531"
  - authors: "peek-a-boo"
    year: 2019
    title: "How to come up with the Jacobian in the change of variables formula"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2021-08-30"
    url: "https://math.stackexchange.com/a/3239222"
  - authors: "Wikipedia"
    year: 2021
    title: "Jacobian matrix and determinant"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-07"
    url: "https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant#Inverse"
  - authors: "Wikipedia"
    year: 2021
    title: "Inverse function theorem"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-07"
    url: "https://en.wikipedia.org/wiki/Inverse_function_theorem#Statement"
  - authors: "Wikipedia"
    year: 2021
    title: "Determinant"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-07"
    url: "https://en.wikipedia.org/wiki/Determinant#Properties_of_the_determinant"

proof_id: "P262"
shortcut: "dent-noninv"
username: "JoramSoch"
---


**Theorem:** The [differential entropy](/D/dent) is not invariant under change of variables, i.e. there exist random variables $X$ and $Y = g(X)$, such that

$$ \label{eq:dent-noninv}
\mathrm{h}(Y) \neq \mathrm{h}(X) \; .
$$

In particular, for an invertible transformation $g: X \rightarrow Y$ from a random vector $X$ to another random vector of the same dimension $Y$, it holds that

$$ \label{eq:dent-trans}
\mathrm{h}(Y) = \mathrm{h}(X) + \int_{\mathcal{X}} f_X(x) \log \left| J_g(x) \right| \, \mathrm{d}x \; .
$$

where $J_g(x)$ is the Jacobian matrix of the vector-valued function $g$ and $\mathcal{X}$ is the set of possible values of $X$.


**Proof:** By definition, the [differential entropy](/D/dent) of $X$ is

$$ \label{eq:X-dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x
$$

where $f_X(x)$ is the [probability density function](/D/pdf) of $X$.

The [probability density function of an invertible function of a continuous random vector](/P/pdf-invfct) $Y = g(X)$ is

$$ \label{eq:pdf-invfct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace$ is the set of possible outcomes of $Y$ and $J_{g^{-1}}(y)$ is the Jacobian matrix of $g^{-1}(y)$

$$ \label{eq:jac}
J_{g^{-1}}(y) = \left[ \begin{matrix}
\frac{\mathrm{d}x_1}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_1}{\mathrm{d}y_n} \\
\vdots & \ddots & \vdots \\
\frac{\mathrm{d}x_n}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_n}{\mathrm{d}y_n}
\end{matrix} \right] \; .
$$

Thus, the [differential entropy](/D/dent) of $Y$ is

$$ \label{eq:Y-dent-s1}
\begin{split}
\mathrm{h}(Y) &\overset{\eqref{eq:X-dent}}{=} - \int_{\mathcal{Y}} f_Y(y) \log f_Y(y) \, \mathrm{d}y \\
&\overset{\eqref{eq:pdf-invfct}}{=} - \int_{\mathcal{Y}} \left[ f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \right] \log \left[ f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \right] \, \mathrm{d}y \; .
\end{split}
$$

Substituting $y = g(x)$ into the integral and applying $J_{f^{-1}}(y) = J_f^{-1}(x)$, we obtain

$$ \label{eq:Y-dent-s2}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{X}} \left[ f_X(g^{-1}(g(x))) \, \left| J_{g^{-1}}(y) \right| \right] \log \left[ f_X(g^{-1}(g(x))) \, \left| J_{g^{-1}}(y) \right| \right] \, \mathrm{d}[g(x)] \\
&= - \int_{\mathcal{X}} \left[ f_X(x) \, \left| J_g^{-1}(x) \right| \right] \log \left[ f_X(x) \, \left| J_g^{-1}(x) \right| \right] \, \mathrm{d}[g(x)] \; .
\end{split}
$$

Using the relations $y = f(x) \Rightarrow \mathrm{d}y = \lvert J_f(x) \rvert \, \mathrm{d}x$ and $\lvert A \rvert \lvert B \rvert = \lvert AB \rvert$, this becomes

$$ \label{eq:Y-dent-s3}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{X}} \left[ f_X(x) \, \left| J_g^{-1}(x) \right| \left| J_g(x) \right| \right] \log \left[ f_X(x) \, \left| J_g^{-1}(x) \right| \right] \, \mathrm{d}x \\
&= - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x - \int_{\mathcal{X}} f_X(x) \log \left| J_g^{-1}(x) \right| \, \mathrm{d}x \; .
\end{split}
$$

Finally, employing [the fact](/D/pdf) that $\int_{\mathcal{X}} f_X(x) \, \mathrm{d}x = 1$ and the determinant property $\lvert A^{-1} \rvert = 1/\lvert A \rvert$, we can derive the [differential entropy](/D/dent) of $Y$ as

$$ \label{eq:Y-dent-s4}
\begin{split}
\mathrm{h}(Y) &= - \int_{\mathcal{X}} f_X(x) \log f_X(x) \, \mathrm{d}x - \int_{\mathcal{X}} f_X(x) \log \frac{1}{\left| J_g(x) \right|} \, \mathrm{d}x \\
&\overset{\eqref{eq:X-dent}}{=} \mathrm{h}(X) + \int_{\mathcal{X}} f_X(x) \log \left| J_g(x) \right| \, \mathrm{d}x \; .
\end{split}
$$

Because there exist $X$ and $Y$, such that the integral term in \eqref{eq:Y-dent-s4} is non-zero, this also demonstrates that there exist $X$ and $Y$, such that \eqref{eq:dent-noninv} is fulfilled.