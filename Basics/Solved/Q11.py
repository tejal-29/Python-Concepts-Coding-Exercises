'''
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''

n = 5

for i in range(1, n + 1):

    for j in range(1, 2 * n):

        if i == n:
            print("*", end=" ")

        elif j == n - i + 1 or j == n + i - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()


'''
Row 1 (i = 1)

Condition:

j == n - i + 1
j == n + i - 1

Substitute values:

j == 5 - 1 + 1 = 5
j == 5 + 1 - 1 = 5

Both become:

j == 5

So star only at column 5.

1 2 3 4 5 6 7 8 9
        *

Output:

        *
Row 2 (i = 2)

Left star:

j = 5 - 2 + 1
j = 4

Right star:

j = 5 + 2 - 1
j = 6

Stars at columns 4 and 6.

1 2 3 4 5 6 7 8 9
      *   *

Output:

      *   *
Row 3 (i = 3)

Left star:

j = 5 - 3 + 1 = 3

Right star:

j = 5 + 3 - 1 = 7

Stars at columns 3 and 7.

1 2 3 4 5 6 7 8 9
    *       *

Output:

    *       *
'''    