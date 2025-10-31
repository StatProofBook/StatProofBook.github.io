---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-04-04 14:42:41

title: "Relationship between F-distribution and beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Relationship to F-distribution"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "F-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-04-04"
    url: "https://en.wikipedia.org/wiki/F-distribution#Related_distributions"
  - authors: "Wikipedia"
    year: 2025
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-04-04"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Related_distributions"

proof_id: "P497"
shortcut: "beta-f"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [F-distribution](/D/f):

$$ \label{eq:X}
X \sim F(d_1, d_2) \; .
$$

Then, the quantity

$$ \label{eq:Y}
Y = \frac{d_1 X / d_2}{1 + d_1 X / d_2} = \frac{d_1 X}{d_2 + d_1 X}
$$

follows a [beta distribution](/D/beta):

$$ \label{eq:beta-f}
Y \sim \mathrm{Bet}\left( \frac{d_1}{2}, \frac{d_2}{2} \right) \; .
$$


**Proof:** We denote $Y = g(X)$. The first derivative of the $g$ is:

$$ \label{eq:dg-dx}
\begin{split}
   \frac{\mathrm{d}g(x)}{\mathrm{d}x}
&= \frac{\mathrm{d}}{\mathrm{d}x} \left( \frac{d_1 x}{d_2 + d_1 x} \right) \\
&= \frac{d_1 d_2 + d_1^2 x - d_1^2 x}{(d_2 + d_1 x)^2} \\
&= \frac{d_1 d_2}{(d_2 + d_1 x)^2} \; .
\end{split}
$$

This derivative is positive for all $x \geq 0$, such that $Y$ is a strictly increasing function of $X$. This means we can derive the distribution of $Y$ by applying the [probability density function of a strictly increasing function of a continuous random variable](/P/pdf-sifct):

$$ \label{eq:pdf-sifct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y} \; .
\end{array}
\right.
$$

where $\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace$. Because $g: \, \mathbb{R}\_{\geq 0} \rightarrow [0,1]$, we have $\mathcal{X} = \mathbb{R}\_{\geq 0}$ and $\mathcal{Y} = [0, 1]$, such that

$$ \label{eq:Y-pdf-zero}
f_Y(y) = 0
\quad \text{for} \quad
y \notin [0,1] \; .
$$

The inverse function of $g$ is:

$$ \label{eq:g-inv}
\begin{split}
       g(x) = y &= \frac{d_1 x}{d_2 + d_1 x} \\
d_2 y + d_1 x y &= d_1 x \\
d_1 x - d_1 x y &= d_2 y \\
x (d_1 - d_1 y) &= d_2 y \\
              x &= \frac{d_2 y}{d_1 - d_1 y} = g^{-1}(y) \; .
\end{split}
$$

The derivative of $g^{-1}$ with respect to $y$ is:

$$ \label{eq:dg-inv-dy}
\begin{split}
   \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y}
&= \frac{\mathrm{d}}{\mathrm{d}y} \left( \frac{d_2 y}{d_1 - d_1 y} \right) \\
&= \frac{d_1 d_2 + d_1 d_2 y - (- d_1 d_2 y)}{(d_1 - d_1 y)^2} \\
&= \frac{d_1 d_2}{d_1^2 - 2 d_1^2 y + d_1^2 y^2} \\
&= \frac{d_2}{d_1 - 2 d_1 y + d_1 y^2} \\
&= \frac{d_2}{d_1 (1 - 2 y + y^2)} \\
&= \frac{d_2}{d_1} \cdot \frac{1}{(1-y)^2} \; .
\end{split}
$$

The [probability density function of the F-distribution](/P/f-pdf) with [degrees of freedom](/D/dof) $d_1$ and $d_2$ is:

$$ \label{eq:f-pdf}
f_X(x) = \frac{\Gamma\left( \frac{d_1+d_2}{2} \right)}{\Gamma\left( \frac{d_1}{2} \right) \cdot \Gamma\left( \frac{d_2}{2} \right)} \cdot \left( \frac{d_1}{d_2} \right)^{\frac{d_1}{2}} \cdot x^{\frac{d_1}{2}-1} \cdot \left( \frac{d_1}{d_2} x + 1 \right)^{-\frac{d_2+d_2}{2}} \; .
$$

With that, we have everything that we need to derive the distribution of $Y$ for $y \in \mathcal{Y}$. Combining \eqref{eq:pdf-sifct}, \eqref{eq:f-pdf}, \eqref{eq:g-inv} and \eqref{eq:dg-inv-dy}, $f_Y(y)$ for $y \in [0,1]$ becomes:

$$ \label{eq:Y-pdf-nonzero}
\begin{split}
   f_Y(y)
&= f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \\
&= \frac{\Gamma\left( \frac{d_1+d_2}{2} \right)}{\Gamma\left( \frac{d_1}{2} \right) \cdot \Gamma\left( \frac{d_2}{2} \right)} \cdot \left( \frac{d_1}{d_2} \right)^{\frac{d_1}{2}} \cdot \left( \frac{d_2 y}{d_1 - d_1 y} \right)^{\frac{d_1}{2}-1} \cdot \left( \frac{d_1}{d_2} \left( \frac{d_2 y}{d_1 - d_1 y} \right) + 1 \right)^{-\frac{d_1+d_2}{2}} \cdot \\
&\hphantom{=} \left( \frac{d_2}{d_1} \cdot \frac{1}{(1-y)^2} \right) \\
&= \frac{1}{\mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot \left( \frac{d_1}{d_2} \right)^{\frac{d_1}{2}} \cdot d_2^{\frac{d_1}{2}-1} \cdot y^{\frac{d_1}{2}-1} \cdot d_1^{-\left(\frac{d_1}{2}-1\right)} \cdot (1-y)^{-\left(\frac{d_1}{2}-1\right)} \cdot \\
&\hphantom{=} \left( \frac{d_1}{d_2} \left( \frac{d_2 y}{d_1 - d_1 y} \right) + 1 \right)^{-\frac{d_1+d_2}{2}} \cdot \left( \frac{d_2}{d_1} \cdot \frac{1}{(1-y)^2} \right) \\
&= \frac{1}{\mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot \left( \frac{d_1}{d_2} \right) \cdot \left( \frac{d_2}{d_1} \right) \cdot y^{\frac{d_1}{2}-1} \cdot (1-y)^{-\frac{d_1}{2}+1} \cdot (1-y)^{-2} \cdot \\
&\hphantom{=} \left( \frac{d_1 d_2 y}{d_2 (d_1 - d_1 y)} + \frac{d_2 (d_1 - d_1 y)}{d_2 (d_1 - d_1 y)} \right)^{-\frac{d_1+d_2}{2}} \\
&= \frac{1}{\mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot y^{\frac{d_1}{2}-1} \cdot (1-y)^{-\frac{d_1}{2}-1} \cdot \left( \frac{d_1 d_2}{d_2 (d_1 - d_1 y)} \right)^{-\frac{d_1+d_2}{2}} \\
&= \frac{1}{\mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot y^{\frac{d_1}{2}-1} \cdot (1-y)^{-\frac{d_1}{2}-1} \cdot \left( \frac{1}{1 - y} \right)^{-\frac{d_1+d_2}{2}} \\
&= \frac{1}{\mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot y^{\frac{d_1}{2}-1} \cdot (1-y)^{-\frac{d_1}{2}-1} \cdot (1-y)^{\frac{d_1+d_2}{2}} \\
&= \frac{1}{\mathrm{B}\left( \frac{d_1}{2}, \frac{d_2}{2} \right)} \cdot y^{\frac{d_1}{2}-1} \cdot (1-y)^{\frac{d_2}{2}-1} \; .
\end{split}
$$

This is the [probability density function of the beta distribution](/P/beta-pdf) with parameters

$$ \label{eq:beta-f-para}
\alpha = \frac{d_1}{2}
\quad \mathrm{and} \quad
\beta = \frac{d_2}{2} \; ,
$$

such that

$$ \label{eq:beta-f-qed}
Y \sim \mathrm{Bet}\left( \frac{d_1}{2}, \frac{d_2}{2} \right) \; .
$$