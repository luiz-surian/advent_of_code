#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

# from pprint import pprint

tree = {}
value = 0


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.read().split(" ")
    return [int(x.strip()) for x in content]


def part_1():
    def gen_tree(items, i_node, n_father="root"):
        global tree
        n_child = items[i_node]
        n_meta = items[i_node + 1]
        i_next = i_node + 2
        ret = 0
        tree[i_node] = {
            "n_father": n_father,
            "n_child": n_child,
            "n_meta": n_meta,
            "metadata": []
        }
        for _ in range(n_child):
            i_next, tmp = gen_tree(items, i_next, i_node)
            ret += tmp
        meta = items[i_next:i_next + n_meta]
        tree[i_node]["metadata"] = meta
        return i_next + n_meta, ret + sum(meta)

    serial = load_import()
    return gen_tree(serial, 0)[1]


def part_2():
    def get_children(node):
        global tree
        if tree[node]["n_child"] == 0:
            return sum(tree[node]["metadata"])
        else:
            children = []
            for n_id, n in tree.items():
                if n["n_father"] == node:
                    children.append(n_id)
            return children

    def travel(node):
        global tree, value
        # print(f"travel({node})")
        children = get_children(node)
        # print(children)
        if type(children) is int:
            value += children
        else:
            # print(self.tree[node]["metadata"])
            for n in tree[node]["metadata"]:
                try:
                    travel(children[n - 1])
                except IndexError:
                    # print("Node", n, "Not found, ignoring")
                    pass

    travel(0)
    return value


if __name__ == '__main__':
    print("Day 8 - Part 1 - What is the sum of all metadata entries?:", part_1())
    # Result: -- 37262

    print("Day 8 - Part 2 - What is the value of the root node?:",  part_2())
    # Result: -- 20839
