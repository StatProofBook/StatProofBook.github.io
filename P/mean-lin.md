---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-13 21:08:00

title: "Linearity of the expected value"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Linearity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Expected value"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-13"
    url: "https://en.wikipedia.org/wiki/Expected_value#Basic_properties"
  - authors: "Michael B, Kuldeep Guha Mazumder, Geoff Pilling et al."
    year: 2020
    title: "Linearity of Expectation"
    in: "brilliant.org"
    pages: "retrieved on 2020-02-13"
    url: "https://brilliant.org/wiki/linearity-of-expectation/"

proof_id: "P53"
shortcut: "mean-lin"
username: "JoramSoch"
---


**Theorem:** The [expected value](/D/mean) is a linear operator, i.e.

$$ \label{eq:mean-lin}
\begin{split}
\mathrm{E}(X + Y) &= \mathrm{E}(X) + \mathrm{E}(Y) \\
\mathrm{E}(a\,X) &= a\,\mathrm{E}(X)
\end{split}
$$

for [random variables](/D/rvar) $X$ and $Y$ and a [constant](/D/const) $a$.


**Proof:**

1) If $X$ and $Y$ are [discrete random variables](/D/rvar-disc), the [expected value](/D/mean) is

$$ \label{eq:mean-disc}
\mathrm{E}(X) = \sum_{x \in \mathcal{X}} x \cdot f_X(x)
$$

and the [law of marginal probability](/D/prob-marg) states that

$$ \label{eq:lmp-disc}
p(x) = \sum_{y \in \mathcal{Y}} p(x,y) \; .
$$

Applying this, we have

$$ \label{eq:mean-lin-s1-disc}
\begin{split}
\mathrm{E}(X + Y) &= \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} (x+y) \cdot f_{X,Y}(x,y) \\
&= \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} x \cdot f_{X,Y}(x,y) + \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} y \cdot f_{X,Y}(x,y) \\
&= \sum_{x \in \mathcal{X}} x \sum_{y \in \mathcal{Y}} f_{X,Y}(x,y) + \sum_{y \in \mathcal{Y}} y \sum_{x \in \mathcal{X}} f_{X,Y}(x,y) \\
&\overset{\eqref{eq:lmp-disc}}{=} \sum_{x \in \mathcal{X}} x \cdot f_X(x) + \sum_{y \in \mathcal{Y}} y \cdot f_{Y}(y) \\
&\overset{\eqref{eq:mean-disc}}{=} \mathrm{E}(X) + \mathrm{E}(Y)
\end{split}
$$

as well as

$$ \label{eq:mean-lin-s2-disc}
\begin{split}
\mathrm{E}(a\,X) &= \sum_{x \in \mathcal{X}} a \, x \cdot f_X(x) \\
&= a \, \sum_{x \in \mathcal{X}} x \cdot f_X(x) \\
&\overset{\eqref{eq:mean-disc}}{=} a \, \mathrm{E}(X) \; .
\end{split}
$$

<br>
2) If $X$ and $Y$ are [continuous random variables](/D/rvar-disc), the [expected value](/D/mean) is

$$ \label{eq:mean-cont}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x
$$

and the [law of marginal probability](/D/prob-marg) states that

$$ \label{eq:lmp-cont}
p(x) = \int_{\mathcal{Y}} p(x,y) \, \mathrm{d}y \; .
$$

Applying this, we have

$$ \label{eq:mean-lin-s1-cont}
\begin{split}
\mathrm{E}(X + Y) &= \int_{\mathcal{X}} \int_{\mathcal{Y}} (x+y) \cdot f_{X,Y}(x,y) \, \mathrm{d}y \, \mathrm{d}x \\
&= \int_{\mathcal{X}} \int_{\mathcal{Y}} x \cdot f_{X,Y}(x,y) \, \mathrm{d}y \, \mathrm{d}x + \int_{\mathcal{X}} \int_{\mathcal{Y}} y \cdot f_{X,Y}(x,y) \, \mathrm{d}y \, \mathrm{d}x \\
&= \int_{\mathcal{X}} x \int_{\mathcal{Y}} f_{X,Y}(x,y) \, \mathrm{d}y \, \mathrm{d}x + \int_{\mathcal{Y}} y \int_{\mathcal{X}} f_{X,Y}(x,y) \, \mathrm{d}x \, \mathrm{d}y \\
&\overset{\eqref{eq:lmp-cont}}{=} \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x + \int_{\mathcal{Y}} y \cdot f_Y(y) \, \mathrm{d}y \\
&\overset{\eqref{eq:mean-cont}}{=} \mathrm{E}(X) + \mathrm{E}(Y)
\end{split}
$$

as well as

$$ \label{eq:mean-lin-s2-cont}
\begin{split}
\mathrm{E}(a\,X) &= \int_{\mathcal{X}} a \, x \cdot f_X(x) \, \mathrm{d}x \\
&= a \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:mean-cont}}{=} a \, \mathrm{E}(X) \; .
\end{split}
$$

<br>
Collectively, this shows that both requirements for linearity are fulfilled for the [expected value](/D/mean), for [discrete](/D/rvar-disc) as well as for [continuous](/D/rvar-disc) random variables.