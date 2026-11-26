---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-24 21:23:47

title: "Population least squares under the Berkson error model in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Population least squares under the Berkson error model"

sources:
  - authors: "Emmanuel Lesaffre, Andrew B. Lawson"
    year: 2012
    title: "Measurement error"
    in: "Bayesian Biostatistics"
    pages: "Section 13.1.2, pp. 376-378"
  - authors: "Fumio Hayashi"
    year: 2000
    title: "Least Squares Projection"
    in: "Econometrics"
    pages: "Section 2.9, pp. 138-139, Propositions 2.7-2.8"

proof_id: "P581"
shortcut: "slrbem-popls"
username: "kjpetrykowski"
---

**Theorem:** Let $W$ be the assigned exposure, $X=W+U$ the true exposure, and $Y=\alpha+\beta X+\varepsilon$ the outcome, where $\alpha$ and $\beta$ are fixed real numbers. Assume that $W,U,\varepsilon$ are mutually independent with finite variances. The errors $U$ and $\varepsilon$ have mean zero and variances $\tau^2$ and $\sigma^2$, respectively.

Let $a$ and $b$ be any real numbers. The line $a+bW$ predicts the outcome from the assigned exposure using intercept $a$ and slope $b$. Its population mean squared prediction error is

$$ \label{eq:population-risk}
R(a,b)=\mathrm{E}[(Y-a-bW)^2] \; .
$$

If $\mathrm{Var}(W)>0$, the unique minimizing pair is $(a,b)=(\alpha,\beta)$. If $W=w\_0$ with probability one, the minimizing pairs are exactly those for which $a+bw\_0=\alpha+\beta w\_0$.

**Proof:** Substituting $X=W+U$ in the outcome equation gives $Y=\alpha+\beta W+V$, where $V=\beta U+\varepsilon$. The [conditional-moments proof for the Berkson model](/P/slrbem-meanvar) shows that $V$ is independent of $W$, has mean zero and has variance $\beta^2\tau^2+\sigma^2$.

For any candidate line, put $D=\alpha-a+(\beta-b)W$, the difference between the conditional mean $\alpha+\beta W$ and the prediction $a+bW$. Then $Y-a-bW=D+V$. Since $D$ is a function of $W$, it is independent of $V$, and

$$ \label{eq:cross-term}
\mathrm{E}(DV)=\mathrm{E}(D)\mathrm{E}(V)=0 \; .
$$

Expanding the square gives

$$ \label{eq:least-squares-first}
\begin{split}
\mathrm{E}[(Y-a-bW)^2]
&=\mathrm{E}[(D+V)^2]\\
&=\mathrm{E}(D^2)+2\mathrm{E}(DV)+\mathrm{E}(V^2)\\
&=\mathrm{E}(D^2)+\beta^2\tau^2+\sigma^2 \; .
\end{split}
$$

Use [the identity](/P/var-mean) $\mathrm{E}(D^2)=[\mathrm{E}(D)]^2+\mathrm{Var}(D)$. Here,

$$ \label{eq:candidate-moments}
\begin{split}
\mathrm{E}(D)&=\alpha-a+(\beta-b)\mathrm{E}(W),\\
\mathrm{Var}(D)&=(\beta-b)^2\mathrm{Var}(W) \; .
\end{split}
$$

Consequently,

$$ \label{eq:least-squares}
\begin{split}
R(a,b)
&=[\alpha-a+(\beta-b)\mathrm{E}(W)]^2\\
&\quad+(\beta-b)^2\mathrm{Var}(W)
 +\beta^2\tau^2+\sigma^2 \; .
\end{split}
$$

The first two terms are nonnegative, and both are zero at $(a,b)=(\alpha,\beta)$. The smallest possible value of $R(a,b)$ is therefore $\beta^2\tau^2+\sigma^2$. When $\mathrm{Var}(W)>0$, the second term is zero only if $b=\beta$. With $b=\beta$, the first term reduces to $(\alpha-a)^2$, which is zero only if $a=\alpha$. This proves uniqueness.

If instead $W=w\_0$ with probability one, \eqref{eq:least-squares} reduces to

$$ \label{eq:constant-exposure-risk}
R(a,b)=[(\alpha+\beta w_0)-(a+bw_0)]^2+\beta^2\tau^2+\sigma^2 \; .
$$

Every line through the point $(w\_0,\alpha+\beta w\_0)$ gives the same optimal prediction at the only assigned exposure. Its slope can be chosen freely.
