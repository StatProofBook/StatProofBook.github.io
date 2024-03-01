---
layout: proof
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 17:40:00

title: "Log Probability is a Strictly Proper Scoring rule"
chapter: "General Theorems"
section: "Probability theory"
topic: "Decision Theory"
definition: "Log Probability is a Strictly Proper Scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"

def_id: "P438"
shortcut: "spsr-lsr"
username: "KarahanS"
---


**Theorem:** [Log (probability) scoring rule](/D/lsr) is a [strictly proper scoring rule](/D/spsr).

We will show that all versions of the log probability scoring rule (binary/multiclass/continuous) are _strictly proper_ scoring rules.

* **Binary log probability scoring rule**

**Proof:**

$$
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] = P(Y = 1) \log q + P(Y = 0) \log (1 - q)
$$
Let $p$ be the true probability of the event $Y = 1$. Then, the expected score is:
$$
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] = p \log q + (1 - p) \log (1 - q) 
$$
To find the maxima, take the derivative with respect to $q$ and set it to zero:
$$
\begin{split}
\frac{\partial}{\partial q}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= \frac{p}{q} - \frac{1-p}{1 - q} = 0 \\
&= \frac{p  - pq - q +pq}{q (1-q)} = 0 \\
&= \frac{p - q}{q (1-q)} = 0\\
& \Rightarrow p - q = 0 \\
& \Rightarrow p = q
\end{split}
$$

Now, we need to check the second derivative to see if it is a maximum for _properness_ condition and if it is the only maximizer for _strictness_ condition:

$$
\begin{split}
\frac{\partial^2}{\partial q^2}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= -\frac{p}{q^2} - \frac{1-p}{(1 - q)^2}  \\
&= - \left( \underbrace{\frac{p}{q^2}}_\textrm{> 0} + \underbrace{\frac{1-p}{(1 - q)^2}}_\textrm{> 0} \right)  < 0
\end{split}
$$
Except for the cases $q=0$ and $q=1$, second derivative is _always_ negative, which means that the function is concave and the maximum is unique. For $q = 1$, maximum is achieved only if $p = 1$, and similarly for $q = 0$ maximum is achieved only if $p = 0$. Therefore, $p = q$ is the only maximizer and the log probability scoring rule for binary classification is _strictly proper_. 

* **Multiclass log probability scoring rule**

**Proof #1:**

$$
S(q, y) = \sum_k^K y_k \log q_k(x)
$$
Let $p_k$ be the true probability of the event $Y = k$. Since $q_k$ is the predicted probability for class $k$, we know that $\sum_i q_i = 1$. Then, the expected score is:
$$
\begin{split}
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= \sum_k P(Y = k|x) \log(q_k(x)) \\&= p_1 \log(q_1(x)) + p_2\log(q_2(x)) + ... + p_K \log(q_K(x)) \\&= p_1 \log(q_1(x)) + p_2\log(q_2(x)) + ... + p_K \log(1 - \sum_{i \neq K} q_i(x))
\end{split}
$$
Taking the derivative with respect to $q_j$ and setting it to zero:
$$
\begin{split}
\frac{\partial}{\partial q_j}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= \frac{p_j}{q_j} -\frac{p_K}{1- \sum_{i \neq K} q_i(x)} = 0 \\
&= \frac{p_j}{q_j} - \frac{p_K}{q_K} = 0 \\
& \Rightarrow \frac{p_j}{q_j} = \frac{p_K}{q_K}
\end{split}
$$
This equality holds for any $j$:
$$
\frac{p_1}{q_1} = \frac{p_2}{q_2} = ... = \frac{p_K}{q_K} = \lambda
$$
Each $q_i$ can be represented as a constant multiple of $p_i$ as follows:  $q_i = \lambda \ p_i$
$$
\begin{split}
    \sum_i q_i &= 1 \\
    \sum_i \lambda \ p_i &= 1 \\
    \lambda \sum_i p_i &= 1 \\
    \lambda = 1
 \end{split}
 $$
 Since $\lambda = 1$, we have $p_i = q_i$ for all $i$. Now, we need to check the second derivative to see if it is a maximum for _properness_ condition and if it is the only maximizer for _strictness_ condition:

$$
\begin{split}

\frac{\partial^2}{\partial q_j^2}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= -\frac{p_j}{q_j^2} - \frac{p_K}{(1- \sum_{i \neq K} q_i(x))^2}  \\
&= - \left( \underbrace{\frac{p_j}{q_j^2}}_\textrm{> 0} + \underbrace{\frac{p_K}{(1- \sum_{i \neq K} q_i(x))^2}}_\textrm{> 0} \right)  < 0
\end{split}
$$

Except for the cases $q_j=0$ and $q_j=1$, second derivative is _always_ negative, which means that the function is concave and the maximum is unique. For $q_j = 1$, maximum is achieved only if $p_j = 1$, and similarly for $q_j = 0$ maximum is achieved only if $p_j = 0$. Therefore, $p_j = q_j$ is the only maximizer and the log probability scoring rule for multiclass classification is _strictly proper_.

**Proof #2:**

Alternatively, we can solve the optimization problem with Lagrange Multipliers. The Lagrangian is:
$$
\mathcal{L}(q, \lambda) = \sum_k P(Y = k|x) \log(q_k(x)) + \lambda \left(1 - \sum_k q_k(x)\right)
$$
Taking the derivative with respect to $q_j$ and setting it to zero:
$$
\begin{split}
\frac{\partial}{\partial q_j}\mathcal{L}(q, \lambda) &= \frac{p_j}{q_j} - \lambda = 0 \\
& \Rightarrow \frac{p_j}{q_j} = \lambda
\end{split}
$$

Rest of the proof is the same as the first proof.


* **Continuous log probability scoring rule**

**Proof:**
$$
S(q, y) = \log q(y)
$$

Let $p(y)$ be the true probability density function of the event $Y = y$. Then, the expected score is:

$$
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] = \int p(y) \log q(y) dy
$$

Let $X = \frac{q(y)}{p(y)}$ and $\phi = \log(\cdot)$ (a concave function). By Jensen's inequality we know that $f(\mathbb{E}[X]) \leq \mathbb{E}[f(X)]$ if **$f$ is concave**. Therefore, we have:
$$
\begin{split}
\int p(y) \log \frac{q(y)}{p(y)} dy &\leq \log \int p(y)\frac{q(y)}{p(y)} dy\\ \int p(y) \log \frac{q(y)}{p(y)} dy &\leq \log \int q(y) dy \\ \int p(y) \log \frac{q(y)}{p(y)} dy &\leq \log(1) \\
\int p(y) \log \frac{q(y)}{p(y)} dy &\leq 0 \\

\end{split}
$$

The same result can be achieved by using the [Kullback-Leibler divergence](/D/kl). [The Kullback-Leibler divergence is always non-negative](/P/kl-nonneg2.md), therefore $\text{E} - \text{CE} = \text{KL} \geq 0$. Resulting expression is $-\text{KL}$, which is always non-positive. It is maximized **only when** $q(y) = p(y)$, which means that the log probability scoring rule for continuous classification is _strictly proper_.

An alternative argument for _uniqueness_ of the maximum point can be proposed as follows: $\int p(y) \log \frac{q(y)}{p(y)} dy $ can be equal to $0$ in two cases: Either $\frac{q(y)}{p(y)}$ is equal to $1$ for each value - or the expression $\log ( \frac{q(y)}{p(y)})$ takes positive and negative values - summing up to $0$ at the end. Second case cannot occur because it means that there exists $y_0$ such that  $q(y_0) > p(y_0)$.  imply that Jensen’s inequality is violated. Therefore the maximum is achieved if and only if $q = p$.


