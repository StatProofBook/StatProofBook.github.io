---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-06-21 10:24:32

title: "Mutual information of dependent and independent variables in the general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Mutual information"

sources:

proof_id: "P457"
shortcut: "glm-mi"
username: "JoramSoch"
---


**Theorem:** Consider a [general linear model](/D/glm) $m_1$ with $n \times v$ data matrix $Y$, $n \times p$ design matrix $X$ and [uncorrelated observations](/D/glm), i.e. $V = I_n$,

$$ \label{eq:m1}
m_1: \; Y = X B + E_1, \; E_1 \sim \mathcal{MN}(0, I_n, \Sigma_1) \; ,
$$

as well as another model $m_0$ in which $X$ has no influence on $Y$:

$$ \label{eq:m0}
m_0: \; Y = E_0, \; E_0 \sim \mathcal{MN}(0, I_n, \Sigma_0) \; .
$$

Then, the [mutual information](/D/mi) of $Y$ and $X$ is equal to

$$ \label{eq:glm-mi}
I(X,Y) = - \frac{n}{2} \ln \frac{|\Sigma_1|}{|\Sigma_0|} \; .
$$


**Proof:** The [continuous mutual information can be written in terms of marginal and conditional differential entropy](/P/cmi-mcde) as follows:

$$ \label{eq:cmi-mcde}
\mathrm{I}(X,Y) = \mathrm{h}(Y) - \mathrm{h}(Y|X) \; .
$$

The marginal distribution of $Y$, unconditional on $X$, is given by model $m_0$

$$ \label{eq:m0-dist}
Y \sim \mathcal{MN}(0, I_n, \Sigma_0)
$$

and the conditional distribution of $Y$ given $X$ is given by model $m_1$

$$ \label{eq:m1-dist}
Y \sim \mathcal{MN}(XB, I_n, \Sigma_1) \; .
$$

Since $X$ is [constant](/D/const) and thus only has [one possible value](/D/samp-spc), the [conditional differential entropy](/D/dent-cond) of $Y$ given $X$ is obtained by simply entering $X$ into the [probability distribution](/D/dist) for which the [differential entropy](/D/dent-cond) is calculated:

$$ \label{eq:dent-cond-const}
\begin{split}
\mathrm{h}(Y|X)
&= \int_{z \in \mathcal{X}} p(z) \cdot \mathrm{h}(Y|z) \, \mathrm{d}z \\
&= p(X) \cdot \mathrm{h}(Y|X) \\
&= \mathrm{h}\left[ p(Y|X,B,\Sigma_1) \right] \; .
\end{split}
$$

The [differential entropy of the matrix-normal distribution](/P/matn-dent) is

$$ \label{eq:matn-dent}
\begin{split}
&X \sim \mathcal{MN}(M, U, V) \quad \text{where} \quad X \in \mathbb{R}^{n \times p} \\
\Rightarrow \quad 
&\mathrm{h}(X) = \frac{np}{2} \ln(2\pi) + \frac{n}{2} \ln|V| + \frac{p}{2} \ln|U| + \frac{np}{2} \; ,
\end{split}
$$

such that the mutual information of $Y$ and $X$ becomes

$$ \label{eq:dent-cond}
\begin{split}
\mathrm{I}(X,Y)
&= \mathrm{h}\left[ p(Y|\Sigma_0) \right] - \mathrm{h}\left[ p(Y|X,B,\Sigma_1) \right] \\
&= \mathrm{h}\left[ \mathcal{MN}(0, I_n, \Sigma_0) \right] - \mathrm{h}\left[ \mathcal{MN}(XB, I_n, \Sigma_1) \right] \\
&= \left( \frac{nv}{2} \ln(2\pi) + \frac{n}{2} \ln|\Sigma_0| + \frac{v}{2} \ln|I_n| + \frac{nv}{2} \right) \\
&- \left( \frac{nv}{2} \ln(2\pi) + \frac{n}{2} \ln|\Sigma_1| + \frac{v}{2} \ln|I_n| + \frac{nv}{2} \right) \\
&= \frac{n}{2} \ln|\Sigma_0| - \frac{n}{2} \ln|\Sigma_1| \\
&= \frac{n}{2} \ln \frac{|\Sigma_0|}{|\Sigma_1|} \\
&= - \frac{n}{2} \ln \frac{|\Sigma_1|}{|\Sigma_0|} \; .
\end{split}
$$