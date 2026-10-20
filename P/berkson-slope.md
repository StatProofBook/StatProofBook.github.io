---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-20 20:00:00

title: "No slope attenuation under Berkson error in a linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Population regression under Berkson measurement error"

sources:
  - authors: "Emmanuel Lesaffre, Andrew B. Lawson"
    year: 2012
    title: "Measurement error"
    in: "Bayesian Biostatistics"
    pages: "Section 13.1.2, pp. 376-378"

proof_id: "P564"
shortcut: "berkson-slope"
username: "kjpetrykowski"
---

**Theorem:** Let $W$ be an assigned or recorded exposure with $0<\mathrm{Var}(W)<\infty$. Let $U$ be the difference between true and assigned exposure, and let $\varepsilon$ be outcome noise. Assume $W,U,\varepsilon$ are mutually independent and

$$ \label{eq:berkson-slope-assumptions}
\begin{gathered}
\mathrm{E}(U)=\mathrm{E}(\varepsilon)=0,\\
\mathrm{Var}(U)=\tau^2<\infty,\qquad
\mathrm{Var}(\varepsilon)=\sigma^2<\infty \; .
\end{gathered}
$$

For fixed real coefficients $\alpha$ and $\beta$, define true exposure $X$ and outcome $Y$ by

$$ \label{eq:berkson-slope-model}
X=W+U,\qquad Y=\alpha+\beta X+\varepsilon \; .
$$

Then

$$ \label{eq:berkson-slope-conditional}
\mathrm{E}(Y\mid W)=\alpha+\beta W,\qquad
\mathrm{Var}(Y\mid W)=\beta^2\tau^2+\sigma^2 \; .
$$

The population least-squares regression of $Y$ on an intercept and $W$ has intercept $\alpha$ and slope $\beta$.

The variables $X,W,U$ have the same exposure units. The variables $Y,\alpha,\varepsilon$ have outcome units, and $\beta$ has outcome units per exposure unit. Thus $\beta^2\tau^2$ and $\sigma^2$ both have squared outcome units. No normality assumption is required.

**Proof:** Substitute the true-exposure equation into the outcome equation:

$$ \label{eq:berkson-slope-substitute}
Y=\alpha+\beta W+\beta U+\varepsilon \; .
$$

Because $U$ and $\varepsilon$ are independent of $W$ and have mean zero,

$$ \label{eq:berkson-slope-mean}
\mathrm{E}(Y\mid W)
=\alpha+\beta W+\beta\mathrm{E}(U\mid W)
 +\mathrm{E}(\varepsilon\mid W)
=\alpha+\beta W \; .
$$

Mutual independence also makes the conditional joint distribution of $(U,\varepsilon)$ given $W$ equal to its independent marginal distribution. The random part after conditioning on $W$ is therefore $\beta U+\varepsilon$, with variance

$$ \label{eq:berkson-slope-variance}
\begin{split}
\mathrm{Var}(Y\mid W)
&=\beta^2\mathrm{Var}(U)+\mathrm{Var}(\varepsilon)\\
&\quad{}+2\beta\mathrm{Cov}(U,\varepsilon)\\
&=\beta^2\tau^2+\sigma^2 \; .
\end{split}
$$

Population least squares chooses an intercept and slope to minimize expected squared prediction error. Let $a$ and $b$ denote trial values of those coefficients. Conditional centering, or expansion of the square, gives

$$ \label{eq:berkson-slope-least-squares}
\begin{split}
\mathrm{E}[(Y-a-bW)^2]
&=\mathrm{E}[(\alpha-a+(\beta-b)W)^2]\\
&\quad{}+\beta^2\tau^2+\sigma^2\\
&=[\alpha-a+(\beta-b)\mathrm{E}(W)]^2\\
&\quad{}+(\beta-b)^2\mathrm{Var}(W)
 +\beta^2\tau^2+\sigma^2 \; .
\end{split}
$$

The first two terms are nonnegative. Since $\mathrm{Var}(W)>0$, they are both zero only when $b=\beta$ and $a=\alpha$. This proves the population regression claim. Equivalently, its slope is $\mathrm{Cov}(W,Y)/\mathrm{Var}(W)=\beta$.

This model specifies $X=W+U$: true exposure varies around assigned exposure. Classical measurement error specifies the reverse direction, $W=X+U$, together with different independence assumptions. It generally gives an attenuated slope. These are different joint models.
