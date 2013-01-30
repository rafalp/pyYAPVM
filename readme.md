YAPVM - Yet Another Pseudo Virtual Machine (in Python)
======================================================

WTF?!
-----

YAPVM is result of tiny experiment in field of writing virtual machines. It supports few basic basic commands and works exclusively on INTegers.

YAPVM comes with example program "program.txt" that asks user to enter two integeres bigger than 0, sums them and outputs result.

To run that program fire vm.py in your command prompt and enter program.txt as first argument.

Commands
--------

1. **VAR** *arg* - Put read/write cursor at *arg* position in "memory".
2. **INT** *arg* - Set current memory block value to *arg*.
2. **SUM** *arg* - Add *arg* memory block's value to current memory block.
2. **SUB** *arg* - Remove *arg* memory block's value from current memory block.
2. **ASK** *arg* - Ask user *arg* question and await input.
2. **PRT** *arg* - Print *arg* to standard output. You can use "$" as token to be replaced with current memory block's value.
2. **STP** *arg* - Define jump point with *arg* ID.
2. **JMP** *arg* - Jump to *arg* point.
2. **END** - Stop program execution.
2. **GT** *arg* - If current memory block is greater than memory block *arg*, set current memory block to bool True
2. **LT** *arg* - If current memory block is lower than memory block *arg*, set current memory block to bool True
2. **GTE** *arg* - If current memory block is greater than or equal to memory block *arg*, set current memory block to bool True
2. **LTE** *arg* - If current memory block is lower than or equal to memory block *arg*, set current memory block to bool True
2. **EQ** *arg* - If current memory block is equal to memory block *arg*, set current memory block to bool True

In addition, you can write comments by beginning lines with "#".

Authors
-------

**Rafał Pitoń**

+ http://rpiton.com
+ http://github.com/ralfp
+ https://twitter.com/RafalPiton


Copyright and license
---------------------

pyYAPVM is released as public domain.