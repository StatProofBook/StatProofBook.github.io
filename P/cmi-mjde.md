---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-21 17:13:00

title: "Relation of continuous mutual information to marginal and joint differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Continuous mutual information"
theorem: "Relation to marginal and joint differential entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Mutual information"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-21"
    url: "https://en.wikipedia.org/wiki/Mutual_information#Relation_to_conditional_and_joint_entropy"

proof_id: "P59"
shortcut: "cmi-mjde"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be continuous [random variables](/D/rvar) with the [joint probability](/D/prob-joint) $p(x,y)$ for $x \in \mathcal{X}$ and $y \in \mathcal{Y}$. Then, the [mutual information](/D/mi) of $X$ and $Y$ can be expressed as

$$ \label{eq:cmi-mjde}
\mathrm{I}(X,Y) = \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y)
$$

where $\mathrm{h}(X)$ and $\mathrm{h}(Y)$ are the [marginal differential entropies](/D/dent) of $X$ and $Y$ and $\mathrm{h}(X,Y)$ is the [joint differential entropy](/D/dent-joint).


**Proof:** The [mutual information](/D/mi) of $X$ and $Y$ is defined as

$$ \label{eq:MI}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(x)\,p(y)} \, \mathrm{d}y \, \mathrm{d}x \; .
$$

Separating the logarithm, we have:

$$ \label{eq:MI-s1}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x,y) \, \mathrm{d}y \, \mathrm{d}x - \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x) \, \mathrm{d}y \, \mathrm{d}x - \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(y) \, \mathrm{d}y \, \mathrm{d}x \; .
$$

Regrouping the variables, this reads:

$$ \label{eq:MI-s2}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x,y) \, \mathrm{d}y \, \mathrm{d}x - \int_{\mathcal{X}} \left( \int_{\mathcal{Y}} p(x,y) \, \mathrm{d}y \right) \log p(x) \, \mathrm{d}x - \int_{\mathcal{Y}} \left( \int_{\mathcal{X}} p(x,y) \, \mathrm{d}x \right) \log p(y) \, \mathrm{d}y \; .
$$

Applying the [law of marginal probability](/D/prob-marg), i.e. $p(x) = \int_{\mathcal{Y}} p(x,y)$, we get:

$$ \label{eq:MI-s3}
\mathrm{I}(X,Y) = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x,y) \, \mathrm{d}y \, \mathrm{d}x - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x - \int_{\mathcal{Y}} p(y) \log p(y) \, \mathrm{d}y \; .
$$

Now considering the definitions of [marginal](/D/dent) and [joint](/D/dent-joint) differential entropy

$$ \label{eq:MDE-JDE}
\begin{split}
\mathrm{h}(X) &= - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x \\
\mathrm{h}(X,Y) &= - \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \log p(x,y) \, \mathrm{d}y \, \mathrm{d}x \; ,
\end{split}
$$

we can finally show:

$$ \label{eq:MI-qed}
\begin{split}
\mathrm{I}(X,Y) &= - \mathrm{h}(X,Y) + \mathrm{h}(X) + \mathrm{h}(Y) \\
&= \mathrm{h}(X) + \mathrm{h}(Y) - \mathrm{h}(X,Y) \; .
\end{split}
$$