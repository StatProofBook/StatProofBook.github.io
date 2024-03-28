---
layout: proof
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-03-28 20:40:00

title: "Brier scoring rule is strictly proper scoring rule"
chapter: "General Theorems"
section: "Machine learning"
topic: "Scoring rules"
theorem: "Brier scoring rule is strictly proper scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"

proof_id: "P445"
shortcut: "bsr-spsr"
username: "KarahanS"
---


**Theorem:** The [brier scoring rule](/D/bsr) is a [strictly proper scoring rule](/D/spsr).

**Proof:** We will show that both versions of the brier scoring rule (binary/multiclass) are strictly proper scoring rules.
1) Binary Brier Scoring rule:

$$
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] = - P(Y = 1) (q - 1)^2 + P(Y = 0) -q^2
$$

Let $p$ be the true probability of the event $Y = 1$. Then, the expected score is:


$$
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] = - p (q - 1)^2 - (1 - p) q^2
$$

To find the maxima, take the derivative with respect to $q$ and set it to zero:

$$
\begin{split}
\frac{\partial}{\partial q}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= -2p(q - 1) - 2(1 - p)q \\
&= -2pq + 2p - 2q + 2pq \\
&= 2p - 2q \\
0 &= 2p - 2q \\
\Rightarrow p &= q
\end{split}
$$

We need to check the second derivative to see, if it is a maximum for the properness condition and if it is the only maximizer for the strictness condition:

$$
\begin{split}
\frac{\partial^2}{\partial q^2}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= -2 < 0 \\
\end{split}
$$

Second derivative is always negative, which means that the function is concave and the maximum is unique. Therefore, $p = q$ is the only maximizer and the Brier scoring rule for binary classification is strictly proper.

2) Multiclass Brier Scoring rule:

$$
\begin{split}
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= \sum_k P(Y = k) \bigg[ -\sum_i (q_i - y_i)^2 \bigg]\\
&= \sum_k P(Y = k) \bigg[  -(q_{k} - 1)^2 -\sum_{i \neq k} q_i^2 \bigg] \\
&= \sum_k P(Y = k) \bigg[  -(q_{k} - 1)^2 + q_k^2 -\sum_{i} q_i^2 \bigg] \\
&= \sum_k P(Y = k) \bigg[  -q_{k}^2 - 1 + 2q_k + q_k^2 -\sum_{i} q_i^2 \bigg] \\
&= \sum_k P(Y = k) \bigg[  2q_k - 1 -\sum_{i} q_i^2 \bigg] \\
&= \sum_k   P(Y = k)(2q_k - 1)  - \sum_k P(Y = k) \bigg(\sum_i q_i^2\bigg)  \\
&= \sum_k  P(Y = k)(2q_k - 1)  - \sum_i q_i^2 \bigg(\underbrace{\sum_k P(Y = k)}_\textrm{1}\bigg)  \\
&= \sum_k  P(Y = k)(2q_k - 1)  - \sum_i q_i^2 \\
&= \sum_k  P(Y = k)(2q_k - 1)  - q_k^2
\end{split}
$$

Similar to what we did for log probability, this expression can be expressed as follows (replacing $q_K$ with $1 - \sum_{i \neq K} q_i$):

$$
\begin{split}
\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= p_1(2q_1 - 1) - q_1^2 + p_2(2q_2 - 1) - q_2^2 + ... + p_K(2q_K - 1) - q_K^2 \\
&= p_1(2q_1 - 1) -q_1^2 + p_2(2q_2 - 1) -q_2^2 + ... + p_K(1 - 2\sum_{i \neq K} q_i)  -  (1 - \sum_{i \neq K} q_i)^2\\

\end{split}
$$


Taking the derivative with respect to $q_j$ and setting it to zero:

$$
\begin{split}
\frac{\partial}{\partial q_j}\mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] &= 2p_j - 2q_j - 2p_K + 2 (1 - \sum_{i \neq K} q_i) \\
&= 2p_j - 2q_j - 2p_K + 2 q_K \\
&= (p_j - q_j) + (q_K - p_K) \\
(p_j - q_j) &= (p_K - q_K) \\
\end{split}
$$

