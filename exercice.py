#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num_letters = []
	for chr in text:
		if chr.isalnum():
			num_letters += chr
	return len(num_letters)

def get_word_length_histogram(text):

	histo = [0]
	for word in text.split():
		length = get_num_letters(word)
		if length >= len(histo):
			histo += [0] * (length - len(histo) + 1)
		histo[length] += (length != 0)


	return (histo)

def format_histogram(histogram):
	ROW_CHAR = "*"

	return "\n".join([f"{i : >2} {ROW_CHAR*elem}" for i, elem in enumerate(histogram) if i != 0])

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	hauteur = max(histogram)
	resultat = ""
	for i in range(hauteur - 1, -1, -1):
		resultat += "".join([BLOCK_CHAR if elem >= i + 1 else " " for elem in histogram[1:]]) + "\n"

	resultat += LINE_CHAR * len(histogram)
	return resultat


if __name__ == "__main__":
	print(get_num_letters("tree$%^&"))
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
