Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

Should be constant, it does not have to traverse list, just sets value at a key.

2. What is the space complexity of your ring buffer's `append` function?

This is also constant, as the ring buffer never grows in size after initializing.

3. What is the runtime complexity of your ring buffer's `get` method?

Linear: it has to traverse the entire storage list (removing/filtering out `None` items).

4. What is the space complexity of your ring buffer's `get` method?

Constant, for same reason as (2).

5. What is the runtime complexity of the provided code in `names.py`?

Exponential, specifically `O(n^2 + 2n)`. It has to traverse both files accumulating a list per file of length `n` (so `2n`), then traverse the first list, and for each item, also traverse the second list (`n^2`).

6. What is the space complexity of the provided code in `names.py`?

Worst case it would be `3n`: it accumulates two lists of length `n` plus a third list of duplicates (which could be up to length `n` as well).

7. What is the runtime complexity of your optimized code in `names.py`?

Linear, specifically `O(2n)`. It traverses the first file and generates a hash of names (`O(n)`), traverses the second file (`O(n)`) and looks up the name in the hash (`O(c)`).

8. What is the space complexity of your optimized code in `names.py`?

Pretty sure it's just `O(2n)`: the hash is length `n` and the list of duplicates is length `n` in the worst case.
