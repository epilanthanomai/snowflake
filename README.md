# snowflakes

algorithmic snowflake generation for a laser cutter

[![Build Status](https://travis-ci.org/epilanthanomai/snowflake.svg?branch=develop)](https://travis-ci.org/epilanthanomai/snowflake)

## Motivation

The authors have access to a [Glowforge](https://glowforge.com/) laser
cutter. What if we could algorithmically generate some interesting shape
like snowflakes, and then just cut them out? That sounds pretty neat.

## Approach

[Reiter (2004)](http://www.patarnott.com/pdf/SnowCrystalGrowth.pdf)
describes a method for applying hexagonal cellular automata to generate
snowflake shapes. We implement that algorithm, and then we translate the
resultant snowflake cell structure to svg. Glowforge accepts that svg for
printing.

## Development

You can run the tests! You'll need
[tox](https://tox.readthedocs.io/en/latest/index.html).

```shell
$ tox
```
