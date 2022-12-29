#!/usr/bin/python3
"""Defines the text identation function."""

def text_indentation(text):
    """
    printing the text with 2 new lines after each of these characters: . ? and :

    Args:
        text (str): the text provided by the user
    Raises:
        TypeError: if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in ".?:":
        text = (i + "\n\n").join([line.strip(" ") for line in text.split(i)])
    print(text, end="")
