---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-11 01:39:00

title: "Square of expectation of product is less than or equal to product of expectation of squares"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Squared expectation of a product"

sources:
  - authors: "ProofWiki"
    year: 2022
    title: "Square of Expectation of Product is Less Than or Equal to Product of Expectation of Squares"
    in: "ProofWiki"
    pages: "retrieved on 2022-10-11"
    url: "https://proofwiki.org/wiki/Square_of_Expectation_of_Product_is_Less_Than_or_Equal_to_Product_of_Expectation_of_Squares"

proof_id: "P359"
shortcut: "mean-prodsqr"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [random variables](/D/rvar) with [expected values](/D/mean) $\mathrm{E}(X)$ and $\mathrm{E}(Y)$ and let $\mathrm{E}(XY)$ exist and be finite. Then, the square of the expectation of the product of $X$ and $Y$ is less than or equal to the product of the expectation of the squares of $X$ and $Y$:

$$ \label{eq:EXY2-EX2-EY2}
\left[ \mathrm{E}(XY) \right]^2 \leq \mathrm{E}\left( X^2 \right) \mathrm{E}\left( Y^2 \right) \; .
$$


**Proof:** Note that $Y^2$ is a non-negative [random variable](/D/rvar) whose [expected value is also non-negative](/P/mean-nonneg):

$$ \label{eq:mean-Y2-nonneg}
\mathrm{E}\left( Y^2 \right) \geq 0 \; .
$$

1) First, consider the case that $\mathrm{E}\left( Y^2 \right) > 0$. Define a new random variable Z as

$$ \label{eq:Z}
Z = X - Y \, \frac{\mathrm{E}(XY)}{\mathrm{E}\left( Y^2 \right)} \; .
$$

Once again, because $Z^2$ is always non-negative, we have the expected value:

$$ \label{eq:mean-Z2-nonneg}
\mathrm{E}\left( Z^2 \right) \geq 0 \; .
$$

Thus, using the [linearity of the expected value](/P/mean-lin), we have

$$ \label{eq:mean-prodsqr-v1}
\begin{split}
0 &\leq \mathrm{E}\left( Z^2 \right) \\
&\leq \mathrm{E}\left( \left( X - Y \, \frac{\mathrm{E}(XY)}{\mathrm{E}\left( Y^2 \right)} \right)^2 \right) \\
&\leq \mathrm{E}\left( X^2 - 2 X Y \, \frac{\mathrm{E}(XY)}{\mathrm{E}\left( Y^2 \right)} + Y^2 \, \frac{\left[ \mathrm{E}(XY) \right]^2}{\left[ \mathrm{E}\left( Y^2 \right) \right]^2} \right) \\
&\leq \mathrm{E}\left( X^2 \right) - 2 \, \mathrm{E}(XY) \, \frac{\mathrm{E}(XY)}{\mathrm{E}\left( Y^2 \right)} + \mathrm{E}\left( Y^2 \right) \, \frac{\left[ \mathrm{E}(XY) \right]^2}{\left[ \mathrm{E}\left( Y^2 \right) \right]^2} \\
&\leq \mathrm{E}\left( X^2 \right) - 2 \, \frac{\left[ \mathrm{E}(XY) \right]^2}{\mathrm{E}\left( Y^2 \right)} + \frac{\left[ \mathrm{E}(XY) \right]^2}{\mathrm{E}\left( Y^2 \right)} \\
&\leq \mathrm{E}\left( X^2 \right) - \frac{\left[ \mathrm{E}(XY) \right]^2}{\mathrm{E}\left( Y^2 \right)} \; , \\
\end{split}
$$

giving

$$ \label{eq:EXY2-EX2-EY2-qed-v1}
\left[ \mathrm{E}(XY) \right]^2 \leq \mathrm{E}\left( X^2 \right) \mathrm{E}\left( Y^2 \right)
$$

as required.

2) Next, consider the case that $\mathrm{E}\left( Y^2 \right) = 0$. In this case, $Y$ [must be a constant](/D/const) with [mean](/D/mean) $\mathrm{E}(Y) = 0$ and [variance](/D/var) $\mathrm{Var}(Y) = 0$, thus we have

$$ \label{eq:Pr-Y-0}
\mathrm{Pr}(Y = 0) = 1 \; .
$$

This implies

$$ \label{eq:Pr-XY-0}
\mathrm{Pr}(XY = 0) = 1 \; ,
$$

such that

$$ \label{eq:EXY}
\mathrm{E}(XY) = 0 \; .
$$

Thus, we can write

$$ \label{eq:mean-prodsqr-v2}
0 = \left[ \mathrm{E}(XY) \right]^2 = \mathrm{E}\left( X^2 \right) \mathrm{E}\left( Y^2 \right) = 0 \; ,
$$

giving

$$ \label{eq:EXY2-EX2-EY2-qed-v2}
\left[ \mathrm{E}(XY) \right]^2 \leq \mathrm{E}\left( X^2 \right) \mathrm{E}\left( Y^2 \right)
$$

as required.