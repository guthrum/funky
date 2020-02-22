#!/usr/bin/env python3

print("Can flip case of char with (int value) ^ (1<<5)")
c = ord('c')
capital_c = chr(c ^ (1 << 5))
print("c -> " + capital_c)


