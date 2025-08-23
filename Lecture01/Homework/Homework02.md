## Problem: Word Occurrences

You are given a list of words. Some words may repeat.
For each word, output the number of times it occurs.

* The **order of output** should correspond to the **order of first appearance** of each word in the input.

---

### Input Format

1. The first line contains an integer **n** — the number of words.
2. The next **n** lines each contain a single word.

---

### Output Format

The program should output:

1. The number of distinct words.
2. A list of distinct words in the order they appear.
3. A list of occurrence counts corresponding to each word.
4. A dictionary mapping words to their counts.

---

### Sample Input

```
4
bcdef
abcdefg
bcde
bcdef
```

---

### Sample Output

```
3
['bcdef', 'abcdefg', 'bcde']
2 1 1
{'bcdef': 2, 'abcdefg': 1, 'bcde': 1}
```

