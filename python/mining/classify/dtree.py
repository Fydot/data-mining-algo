#!/usr/bin/env python
# coding: utf8
import sys
from math import log
from collections import Counter


def entropy(data):
    """
    :param data: [{"title1": elem1, "title2": elem2, ..., "group": group}, ...]
    :return: The Entropy of data

    calculate entropy of data
    """

    group_counter = Counter()
    for items in data:
        group_counter[items["group"]] += 1

    entropy_score = 0
    for group in group_counter:
        group_p = len(group_counter[group]) / len(data)
        entropy_score += group_p * log(group_p, 2)

    return entropy_score * -1.0


def gain(data, attribute):
    attr_groups = {}
    for items in data:
        if items[attribute] not in attr_groups:
            attr_groups[items[attribute]] = []
        attr_groups[items[attribute]].append(items)

    entropy_weight_score = 0.0
    for attr in attr_groups:
        entropy_weight_score += len(attr_groups[attr]) * entropy(attr_groups[attr])

    return entropy(data) - entropy_weight_score / len(data)


def select_attribute_gain(data):
    if len(data) == 0:
        return None
    attributes = data[0].keys().remove("group")

    max_gain = -sys.maxint
    max_gain_attr = ""

    for attribute in attributes:
        attr_gain = gain(data, attribute)
        if attr_gain > max_gain:
            max_gain = attr_gain
            max_gain_attr = attribute

    return max_gain_attr, max_gain


def build_d_tree(data):
    pass
