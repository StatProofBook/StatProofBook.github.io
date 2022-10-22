---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 08:09:00

title: "Beta-binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Beta-binomial distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Beta-binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-10-20"
    url: "https://en.wikipedia.org/wiki/Beta-binomial_distribution#Motivation_and_derivation"

def_id: "D177"
shortcut: "betabin"
username: "JoramSoch"
---


**Definition:** Let $p$ be a [random variable](/D/rvar) following a [beta distribution](/D/beta)

$$ \label{eq:beta}
p \sim \mathrm{Bet}(\alpha, \beta)
$$

and let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin) conditional on $p$

$$ \label{eq:bin}
X \mid p \sim \mathrm{Bin}(n, p) \; .
$$

Then, the [marginal distribution](/D/dist-marg) of $X$ is called a beta-binomial distribution

$$ \label{eq:betabin}
X \sim \mathrm{BetBin}(n, \alpha, \beta)
$$

with [number of trials](/D/bin) $n$ and [shape parameters](/D/beta) $\alpha$ and $\beta$.