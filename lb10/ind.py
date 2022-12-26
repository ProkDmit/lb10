#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"b", "c", "h", "i", "j"}
    b = {"e", "h", "i", "s", "w"}
    c = {"a", "b", "j", "k", "l", "m"}
    d = {"a", "h", "i", "w", "x"}
    bn = u.difference(b)
    ac = a.difference(c)
    x = ac.intersection(bn)
    print(f"x={x}")
    ab = a.intersection(bn)
    cd = c.difference(d)
    y = ab.union(cd)
    print(f"y={y}")
