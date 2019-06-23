#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import treetaggerwrapper as ttw
import os


TTWDIR=os.environ['HOME']+'/tree-tagger-install/'
tagger=ttw.TreeTagger(TAGLANG='en', TAGDIR=TTWDIR)


def cos_sim(a, b):
	dic2 = {}
	tags2 = tagger.TagText(a.decode("utf-8"))
	for tag2 in tags2:
		tag2 = tag2.split('\t')
		if tag2[2] not in dic2:
			dic2[tag2[2]] = 1
		else:
			dic2[tag2[2]] += 1

	dic = {}
	tags = tagger.TagText(b.decode("utf-8"))
	for tag in tags:
		tag = tag.split('\t')
		if tag[2] not in dic:
			dic[tag[2]] = 1
		else:
			dic[tag[2]] += 1

	length_d = 0.0
	for d in dic:
		length_d += dic[d]
	length_d = math.sqrt(length_d)

	length_d2 = 0.0
	for d2 in dic2:
		length_d2 += dic2[d2]
	length_d2 = math.sqrt(length_d2)

	score = 0.0
        cos = 0.0
	for d in dic:
		if d in dic2:
			score += dic[d] * dic2[d]
	if score != 0.0:
		cos = score / (length_d * length_d2)
	return cos


