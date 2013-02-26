Debugging
=========

### Floating points numbers

#### Binary numbers

Our usual numbers are base ten. So an example would be  
`302 = 3*100 + 0*10 + 2*1`.

Binary is just `0` and `1`. Again a similar exampe, but in base two  
`(binary) 101 = (base 10) 1*2**2 + 0*2**1 + 1*2**0 = (base 10) 5`

Binary numbers take a lot more diggits to represent them than base 10. So to represent `n` digits, you will need `2**n` binary numbers.

Floating point numbers cause problems because we think in `base 10` and the pc in `base 2`. Computers work in `base 2`, because it is to build switches with two states.

Whole numbers - binary or decimal numbers don't have any difference, it's only float numbers that have issues.

A decimal point - `0.125 = 1/8 = 1*10**-1 + 2*10**-2 + 5*10**-3`

A binary point - `0.125 = 1/8 = 2**-3 = 1 * 10**-3 = (binary) 0.001`

*I found this tutorial on the IEEE standardized floating point storage formats*  
![IEEE floating point](http://kipirvine.com/asm/workbook/floating_tut.htm)

Decimal - `0.1 = 1*10**-1` and there is no finite way to display this decimal in binary.

```Python
print(0.1)
# 0.1
