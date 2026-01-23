---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-10-24 13:48:56

title: "Mode of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Mode"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-10-24"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Mode"

proof_id: "P520"
shortcut: "beta-mode"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta distribution](/D/beta):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:beta-mode-p1}
\mathrm{mode}(X) \in \left\{
\begin{array}{rl}
\left\lbrace 0, 1 \right\rbrace \; , & \text{if} \quad \alpha < 1 \quad \text{and} \quad \beta < 1 \\
\left[       0, 1 \right]       \; , & \text{if} \quad \alpha = 1 \quad \text{and} \quad \beta = 1
\end{array}
\right.
$$

and

$$ \label{eq:beta-mode-p2}
\mathrm{mode}(X) = \left\{
\begin{array}{rl}
  0 \; \text{or} \; 1 \; ,
& \text{if} \quad \alpha < 1 \quad \text{or} \quad \beta < 1 \quad (\text{but not} \; \alpha < 1 \; \text{and} \; \beta < 1) \\
  \frac{\alpha-1}{\alpha+\beta-2} \; ,
& \text{if} \quad \alpha \geq 1 \quad \text{and} \quad \beta \geq 1 \quad (\text{but not} \; \alpha = 1 \; \text{and} \; \beta = 1) \; .
\end{array}
\right.
$$


**Proof:** The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the beta distribution](/P/beta-pdf) is:

$$ \label{eq:beta-pdf}
f_X(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1} \; .
$$

1) If $\alpha < 1$, then 0 is the mode, since

$$ \label{eq:beta-mode-p2a-s1}
\lim_{\substack{x \rightarrow 0 \\ \alpha < 1}} f_X(x) = \infty \; ,
\quad \text{because} \quad
\lim_{x \rightarrow 0} x^{\alpha-1} = \infty
\quad \text{for} \quad
\alpha < 1 \; ,
$$

and if $\beta < 1$, then 1 is the mode, since

$$ \label{eq:beta-mode-p2a-s2}
\lim_{\substack{x \rightarrow 1 \\ \beta < 1}} f_X(x) = \infty \; ,
\quad \text{because} \quad
\lim_{x \rightarrow 1} (1-x)^{\beta-1} = \infty
\quad \text{for} \quad
\beta < 1 \; .
$$

2) If both $\alpha < 1$ and $\beta < 1$, then 

$$ \label{eq:beta-mode-p1a}
\lim_{x \rightarrow 0} f_X(x) = \infty
\quad \text{and} \quad
\lim_{x \rightarrow 1} f_X(x) = \infty \; ,
$$

so any value from the set $\left\lbrace 0, 1 \right\rbrace$ may be considered the mode.

3) If both $\alpha = 1$ and $\beta = 1$, then

$$ \label{eq:beta-mode-p1b}
\begin{split}
  f_X(x)
&= \frac{1}{\mathrm{B}(1,1)} \, x^{1-1} \, (1-x)^{1-1} \\
&= \frac{\Gamma(2)}{\Gamma(1) \Gamma(1)} x^0 \, (1-x)^0 \\
&= 1 = \mathrm{const.} \; ,
\end{split}
$$

i.e. the distribution becomes equivalent to the (standard) [continuous uniform distribution](/D/cuni) with parameters $a = 0$ and $b = 1$ which has a [constant probability density function](/P/cuni-pdf). Thus, any value from the interval $\left[ 0,1 \right]$ [may be considered the mode](/P/cuni-mode).

4) For the remaining cases, we must analyze the probability density function. The first two deriatives of this function are:

$$ \label{eq:beta-pdf-der1}
\begin{split}
   f'_X(x)
 = \frac{\mathrm{d}f_X(x)}{\mathrm{d}x}
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \left[ - (\beta-1) x^{\alpha-1} (1-x)^{\beta-2} + (\alpha-1) x^{\alpha-2} (1-x)^{\beta-1} \right] \\
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \left[ (\alpha-1) x^{\alpha-2} (1-x)^{\beta-1} - (\beta-1) x^{\alpha-1} (1-x)^{\beta-2} \right]
\end{split}
$$

$$ \label{eq:beta-pdf-der2}
\begin{split}
   f''_X(x)
 = \frac{\mathrm{d}^2f_X(x)}{\mathrm{d}x^2}
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \left[
   (\alpha-1) \left( (\alpha-2) x^{\alpha-3} (1-x)^{\beta-1} - (\beta-1) x^{\alpha-2} (1-x)^{\beta-2} \right) - \right. \\
&\hphantom{=} \quad\quad\quad\quad\;
   \left. (\beta-1)  \left( (\alpha-1) x^{\alpha-2} (1-x)^{\beta-2} - (\beta-2) x^{\alpha-1} (1-x)^{\beta-3} \right)
   \right] \\
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \left[
   (\alpha-1) (\alpha-2) x^{\alpha-3} (1-x)^{\beta-1} - 2 (\alpha-1) (\beta-1) x^{\alpha-2} (1-x)^{\beta-2} + \right. \\
&\hphantom{=} \quad\quad\quad\quad\;
   \left. (\beta-1) (\beta-2) x^{\alpha-1} (1-x)^{\beta-3}
   \right] \; .
\end{split}
$$

We now calculate the root of the first derivative \eqref{eq:beta-pdf-der1}:

$$ \label{eq:beta-mode-p2b-s1}
\begin{split}
   f'_X(x)
 = 0
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \left[ (\alpha-1) x^{\alpha-2} (1-x)^{\beta-1} - (\beta-1) x^{\alpha-1} (1-x)^{\beta-2} \right] \\
&\Leftrightarrow \\
(\beta-1) x^{\alpha-1} (1-x)^{\beta-2} &= (\alpha-1) x^{\alpha-2} (1-x)^{\beta-1} \\
                           (\beta-1) x &= (\alpha-1) (1-x) \\
            x [(\beta-1) + (\alpha-1)] &= \alpha-1 \\
                                     x &= \frac{\alpha-1}{\alpha+\beta-2} \; .
\end{split}
$$

Note that for this quantity, we have

$$ \label{eq:beta-mode-p2b-s2}
\begin{split}
\frac{\alpha-1}{\alpha+\beta-2} &< 0 \; ,
\quad \text{if}  \quad \alpha < 1 
\quad \text{and} \quad \beta  > 2 - \alpha \\
\frac{\alpha-1}{\alpha+\beta-2} &> 1 \; ,
\quad \text{if}  \quad \beta  < 1 
\quad \text{and} \quad \alpha > 2 - \beta \; .
\end{split}
$$

Also note that the following holds:

$$ \label{eq:beta-mode-p2b-s3}
  1 - x
= 1 - \frac{\alpha-1}{\alpha+\beta-2}
= \frac{\alpha+\beta-2}{\alpha+\beta-2} - \frac{\alpha-1}{\alpha+\beta-2}
= \frac{\beta-1}{\alpha+\beta-2} \; .
$$

By plugging $x$ and $1-x$ into the second deriative \eqref{eq:beta-pdf-der2}, we find:

$$ \label{eq:beta-mode-p2b-s4}
\begin{split}
   f''_X\left( \frac{\alpha-1}{\alpha+\beta-2} \right)
&= \frac{1}{\mathrm{B}(\alpha, \beta)} \left[
   (\alpha-1) (\alpha-2) \left( \frac{\alpha-1}{\alpha+\beta-2} \right)^{\alpha-3} \left( \frac{\beta-1}{\alpha+\beta-2} \right)^{\beta-1} - \right. \\
&\hphantom{=} \quad\quad\quad\quad
   \left. 2 (\alpha-1) (\beta-1) \left( \frac{\alpha-1}{\alpha+\beta-2} \right)^{\alpha-2} \left( \frac{\beta-1}{\alpha+\beta-2} \right)^{\beta-2} + \right. \\
&\hphantom{=} \quad\quad\quad\quad\;
   \left. (\beta-1) (\beta-2) \left( \frac{\alpha-1}{\alpha+\beta-2} \right)^{\alpha-1} \left( \frac{\beta-1}{\alpha+\beta-2} \right)^{\beta-3} \right] \; .
\end{split}
$$

Multiplying with factors which are certainly positive, we can focus on those parts of the second derivative which determine its sign:

$$ \label{eq:beta-mode-p2b-s5}
\begin{split}
   \frac{f''_X(x) \cdot \mathrm{B}(\alpha, \beta)}{\left( \frac{\alpha-1}{\alpha+\beta-2} \right)^{\alpha-3} \cdot \left( \frac{\beta-1}{\alpha+\beta-2} \right)^{\beta-3}}
&= (\alpha-1) (\alpha-2) \left( \frac{\beta-1}{\alpha+\beta-2} \right)^2 - \\
&\hphantom{=} 2 (\alpha-1) (\beta-1) \left( \frac{\alpha-1}{\alpha+\beta-2} \right) \left( \frac{\beta-1}{\alpha+\beta-2} \right) + \\
&\hphantom{=} (\beta-1) (\beta-2) \left( \frac{\alpha-1}{\alpha+\beta-2} \right)^2 \; .
\end{split}
$$

Further multiplying with or dividing by terms which are necessarily positive and thus do not change the sign of the function value, we get:

$$ \label{eq:beta-mode-p2b-s6}
\begin{split}
   \frac{f''_X(x) \cdot \mathrm{B}(\alpha, \beta)}{\left( \frac{\alpha-1}{\alpha+\beta-2} \right)^{\alpha-3} \cdot \left( \frac{\beta-1}{\alpha+\beta-2} \right)^{\beta-3}} \cdot \frac{(\alpha+\beta-2)^2}{(\alpha-1) (\beta-1)}
&= (\alpha-2) (\beta-1) - 2 (\alpha-1) (\beta-1) + (\alpha-1) (\beta-2) \\
&= (\alpha-1) [(\beta-2)-(\beta-1)] + (\beta-1) [(\alpha-1)-(\alpha-2)] \\
&= - (\alpha-1) - (\beta-1) \\
&< 0,
\quad \text{if}  \quad \alpha > 1
\quad \text{and} \quad \beta  > 1 \; .
\end{split}
$$

Thus, $f'\'\_X(x)$ is negative for $x = \frac{\alpha-1}{\alpha+\beta-2}$, demonstrating that this is a maximum. To summarize:

* If $\alpha < 1$ and $\beta < 1$, then $f_X(x)$ diverges at both ends and both values from the set $\left\lbrace 0, 1 \right\rbrace$ can be seen as the mode of $X$.

* If $\alpha < 1$ or $\beta < 1$ (but not $\alpha < 1$ and $\beta < 1$), then the mode of $X$ is 0 or 1, because $f_X(x)$ tends towards infinity at $x = 0$ or $x = 1$.

* If $\alpha = 1$ and $\beta = 1$, then $f_X(x)$ is constant and any value in the interval $\left[ 0,1 \right]$ can be seen as the mode of $X$.

* If $\alpha \geq 1$ and $\beta \geq 1$ (but not $\alpha = 1$ and $\beta = 1$), then $0 < x = \frac{\alpha-1}{\alpha+\beta-2} < 1$ and $f'_X(x) = 0$ and $f'\'\_X(x) < 0$, such that $f_X(x)$ reaches its machimum at $\frac{\alpha-1}{\alpha+\beta-2} = \mathrm{mode}(X)$.