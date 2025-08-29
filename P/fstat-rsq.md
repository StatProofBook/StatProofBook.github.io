---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-15 12:18:18

title: "Relationship between F-statistic and R²"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "F-statistic"
theorem: "Relationship to coefficient of determination"

sources:
  - authors: "Alecos Papadopoulos"
    year: 2014
    title: "What is the distribution of R² in linear regression under the null hypothesis?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2024-03-15"
    url: "https://stats.stackexchange.com/a/130082"

proof_id: "P442"
shortcut: "fstat-rsq"
username: "JoramSoch"
---


**Theorem:** Let there be a [linear regression model](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Then, the [F-statistic](/D/fstat) for comparing this model against a null model containing only a [constant regressor](/D/mlr) $x_0 = 1_n$ can be expressed in terms of the [coefficient of determination](/D/rsq)

$$ \label{eq:F-R2}
F = \frac{R^2/(p-1)}{(1-R^2)/(n-p)}
$$

and vice versa

$$ \label{eq:R2-F}
R^2 = 1 - \frac{1}{F \cdot \frac{p-1}{n-p} + 1}
$$

where $n$ and $p$ are the dimensions of the design matrix $X \in \mathbb{R}^{n \times p}$.


**Proof:** Consider two [linear regression models](/D/mlr) for the same measured data $y$, one using design matrix $X$ from \eqref{eq:mlr} and the other with design matrix $X_0 = 1_n \in \mathbb{R}^{n \times 1}$. Then, $\mathrm{RSS}$ is the [residual sum of squares](/D/rss) of the model in \eqref{eq:mlr} and the residual sum of squares for the model using $X_0$ is equal to the [total sum of squares](/D/tss).

<br>
1) Thus, the [F-statistic](/D/fstat)

$$ \label{eq:F}
F = \frac{(\mathrm{RSS}_0-\mathrm{RSS})/(p-p_0)}{\mathrm{RSS}/(n-p)}
$$

becomes

$$ \label{eq:F-RSS-TSS}
F = \frac{(\mathrm{TSS}-\mathrm{RSS})/(p-1)}{\mathrm{RSS}/(n-p)} \; .
$$

From this, we can derive $F$ in terms of $R^2$:

$$ \label{eq:F-R2-qed}
\begin{split}
F &= \frac{(\mathrm{TSS}-\mathrm{RSS})/(p-1)}{\mathrm{RSS}/(n-p)} \\
&= \frac{\frac{\mathrm{TSS} - \mathrm{RSS}}{\mathrm{TSS}} / (p-1)}{\frac{\mathrm{RSS}}{\mathrm{TSS}} / (n-p)} \\
&= \frac{\left( 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} \right) / (p-1)}{\left( 1 - \left( 1- \frac{\mathrm{RSS}}{\mathrm{TSS}} \right)\right) / (n-p)} \\
&= \frac{\left(R^2\right)/(p-1)}{\left(1-R^2\right)/(n-p)} \; .
\end{split}
$$

<br>
2) Rearranging this equation, we can derive $R^2$ in terms of $F$:

$$ \label{eq:R2-F-qed}
\begin{split}
F &= \frac{\left(R^2\right)/(p-1)}{\left(1-R^2\right)/(n-p)} \\
F \cdot \frac{p-1}{n-p} &= \frac{R^2}{\left(1-R^2\right)} \\
F \cdot \frac{p-1}{n-p} \cdot (1-R^2) &= R^2 \\
F \cdot \frac{p-1}{n-p} - F \cdot \frac{p-1}{n-p} \cdot R^2 &= R^2 \\
F \cdot \frac{p-1}{n-p} \cdot R^2 + R^2 &= F \cdot \frac{p-1}{n-p} \\
R^2 \left( F \cdot \frac{p-1}{n-p} + 1 \right) &= F \cdot \frac{p-1}{n-p} \\
R^2 &= \frac{F \cdot \frac{p-1}{n-p}}{F \cdot \frac{p-1}{n-p} + 1} \\
R^2 &= \frac{F \cdot \frac{p-1}{n-p} + 1 - 1}{F \cdot \frac{p-1}{n-p} + 1} \\
R^2 &= \frac{F \cdot \frac{p-1}{n-p} + 1}{F \cdot \frac{p-1}{n-p} + 1} - \frac{1}{F \cdot \frac{p-1}{n-p} + 1} \\
R^2 &= 1 - \frac{1}{F \cdot \frac{p-1}{n-p} + 1} \\
\end{split}
$$

This completes the proof.