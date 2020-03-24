#! /usr/bin/env python3
# _*_ coding: utf-8 _*_


def compare_list(list1, list2):
    same_items = []
    diff_items_list1_only = []
    diff_items_list2_only = []

    for item in list1:
        if list2.count(item):
            same_items.append(item)
        else:
            diff_items_list1_only.append(item)
    for item in list2:
        if list1.count(item):
            pass
        else:
            diff_items_list2_only.append(item)

    if len(list1) != len(list2):
        print('The two lists are in different size, list1=%s, list2=%s' % (len(list1), len(list2)))
        print('Same elements are: %s' % same_items)
        print('Elements only in list1 are: %s' % diff_items_list1_only)
        print('Elements only in list2 are %s' % diff_items_list2_only)

    else:
        print('The two lists are in same size, list1=%s, list2=%s' % (len(list1), len(list2)))
        print('Same elements are: %s' % same_items)
        print('Elements only in list1 are: %s' % diff_items_list1_only)
        print('Elements only in list2 are %s' % diff_items_list2_only)

if __name__ == '__main__':
    compare_list([1, 1, 2, 3], [1, 2, 3, 4])
