---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-21 17:23:00

title: "Relation of continuous mutual information to joint and conditional differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Continuous mutual information"
theorem: "Relation to joint and conditional differential entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Mutual information"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-21"
    url: "https://en.wikipedia.org/wiki/Mutual_information#Relation_to_conditional_and_joint_entropy"

proof_id: "P60"
shortcut: "cmi-jcde"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be continuous [random variables](/D/rvar) with the [joint probability](/D/prob-joint) $p(x,y)$ for $x \in \mathcal{X}$ and $y \in \mathcal{Y}$. Then, the [mutual information](/D/mi) of $X$ and $Y$ can be expressed as

$$ \label{eq:dmi-jce}
\mathrm{I}(X,Y) = \mathrm{h}(X,Y) - \mathrm{h}(X|Y) - \mathrm{h}(Y|X)
$$

where $\mathrm{h}(X,Y)$ is the [joint differential entropy](/D/dent-joint) of $X$ and $Y$ and $\mathrm{h}(X \vert Y)$ and $\mathrm{h}(Y \vert X)$ are the [conditional differential entropies](/D/dent-cond).


**Proof:** The existence of the joint [probability density function](/D/pdf) ensures that the [mutual information](/D/mi) is defined:

$$ \label{eq:MI}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(x)\,p(y)} \, \mathrm{d}y \, \mathrm{d}x \; .
$$

The [relation of mutual information to conditional differential entropy](/P/cmi-mcde) is:

$$ \label{eq:cmi-mcde1}
\mathrm{I}(X,Y) = \mathrm{h}(X) - \mathrm{h}(X|Y)
$$

$$ \label{eq:cmi-mcde2}
\mathrm{I}(X,Y) = \mathrm{h}(Y) - \mathrm{h}(Y|X)
$$

The [relation of mutual information to joint differential entropy](/P/cmi-mjde) is:

$$ \label{eq:cmi-mjde}
\mathrm{I}(X,Y) = \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y) \; .
$$

It is true that

$$ \label{eq:MI-s1}
\mathrm{I}(X,Y) = \mathrm{I}(X,Y) + \mathrm{I}(X,Y) - \mathrm{I}(X,Y) \; .
$$

Plugging in \eqref{eq:cmi-mcde1}, \eqref{eq:cmi-mcde2} and \eqref{eq:cmi-mjde} on the right-hand side, we have

$$ \label{eq:MI-s2}
\begin{split}
\mathrm{I}(X,Y) &= \mathrm{h}(X) - \mathrm{h}(X|Y) + \mathrm{h}(Y) - \mathrm{h}(Y|X) - \mathrm{h}(X) - \mathrm{h}(Y) + \mathrm{h}(X,Y) \\
&= \mathrm{h}(X,Y) - \mathrm{h}(X|Y) - \mathrm{h}(Y|X)
\end{split}
$$

which proves the identity given above.