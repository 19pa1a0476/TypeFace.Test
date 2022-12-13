The following algorithm is followed by most SQL languages (excluding PostgreSQL[example needed]):

Save the first letter. Map all occurrences of a, e, i, o, u, y, h, w. to zero(0)
Replace all consonants (include the first letter) with digits as in [2.] above.
Replace all adjacent same digits with one digit, and then remove all the zero (0) digits
If the saved letter's digit is the same as the resulting first digit, remove the digit (keep the letter).
Append 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it