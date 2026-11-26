---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-20 20:00:00

title: "Conditional expectation and variance under Berkson error model in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Conditional expectation and variance under Berkson error model"

sources:
  - authors: "Emmanuel Lesaffre, Andrew B. Lawson"
    year: 2012
    title: "Measurement error"
    in: "Bayesian Biostatistics"
    pages: "Section 13.1.2, pp. 376-378"

proof_id: "P564"
shortcut: "slrbem-meanvar"
username: "kjpetrykowski"
---

**Theorem:** Let $W$ be the assigned exposure, $U$ the difference between true and assigned exposure, and $\varepsilon$ the outcome noise. Assume that $W,U,\varepsilon$ are mutually [independent](/D/ind) and have finite variances. The assigned exposure may be constant. Let the errors have means and variances

$$ \label{eq:assumptions}
\begin{gathered}
\mathrm{E}(U)=\mathrm{E}(\varepsilon)=0,\\
\mathrm{Var}(U)=\tau^2,\qquad
\mathrm{Var}(\varepsilon)=\sigma^2 \; .
\end{gathered}
$$

For fixed real numbers $\alpha,\beta$, define the true exposure $X$ and outcome $Y$ by the Berkson error model:

$$ \label{eq:model}
X=W+U,\qquad Y=\alpha+\beta X+\varepsilon \; .
$$

Here true exposure varies around the assigned value. In a classical measurement error model, the recorded exposure varies around the true value. The following conditional mean and variance hold [with probability one](/D/almost-sure) under the distribution of $W$. Any exceptional exposure values together have probability zero.

$$ \label{eq:conditional}
\mathrm{E}(Y\mid W)=\alpha+\beta W,\qquad
\mathrm{Var}(Y\mid W)=\beta^2\tau^2+\sigma^2 \; .
$$

**Proof:** Substitute $X=W+U$ into the outcome equation. Write $V=\beta U+\varepsilon$ for the combined error:

$$ \label{eq:substitute}
Y=\alpha+\beta W+V,\qquad V=\beta U+\varepsilon \; .
$$

Mutual independence implies that the pair $(U,\varepsilon)$, and therefore $V$, is independent of $W$. By [linearity of expectation](/P/mean-lin),

$$ \label{eq:error-mean}
\mathrm{E}(V)=\beta\mathrm{E}(U)+\mathrm{E}(\varepsilon)=0 \; .
$$

Independence of $U$ and $\varepsilon$ gives zero covariance. Thus the [variance-of-a-sum formula](/P/var-sum) yields

$$ \label{eq:error-variance}
\begin{split}
\mathrm{Var}(V)
&=\beta^2\mathrm{Var}(U)+\mathrm{Var}(\varepsilon)
 +2\beta\mathrm{Cov}(U,\varepsilon)\\
&=\beta^2\tau^2+\sigma^2 \; .
\end{split}
$$

Conditioning on $W$ fixes $\alpha+\beta W$ and leaves the distribution of $V$ unchanged. Therefore,

$$ \label{eq:mean}
\mathrm{E}(Y\mid W)=\alpha+\beta W+\mathrm{E}(V\mid W)
=\alpha+\beta W
$$

and

$$ \label{eq:variance}
\mathrm{Var}(Y\mid W)=\mathrm{Var}(V\mid W)
=\mathrm{Var}(V)=\beta^2\tau^2+\sigma^2 \; .
$$

These two identities prove \eqref{eq:conditional}. They use independence and the first two error moments and hold also for nonnormal errors.

<span id="mjx-eqn-eq:least-squares"></span>
The [population least-squares proof](/P/slrbem-popls) explains why the minimizing line has a unique slope when $\mathrm{Var}(W)>0$.
