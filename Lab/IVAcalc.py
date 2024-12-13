"""
Create a program to calculate the final sale price of a product. To do this, request through the command line (shell) the price of the product, the value of the VAT rate to be applied, and (optionally) the value of a discount to be applied to the final product price. The program should give instructions to the user on how it should be invoked. The value of the VAT and the discount should be given as a percentage. 
"""

import sys
from decimal import Decimal as dec

# if not 3 <= len(sys.argv) <= 4:
if len(sys.argv) not in (3, 4):
    print(f"Usage: {sys.argv[0]} PRICE VAT_RATE [DISCOUNT]", file=sys.stderr)
    sys.exit(2)

price = dec(sys.argv[1])
vat_rate = dec(sys.argv[2])
discount = dec(sys.argv[3] if len(sys.argv) == 4 else "0")

final_price = price * (1 + vat_rate / 100) * (1 - discount / 100)

print(f"Final price  : {final_price:.2f} €")
