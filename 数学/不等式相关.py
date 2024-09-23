"""
ax ≤ b  =>  x ≤ ⌊b/a⌋    ax < b  =>  x < ⌈b/a⌉
ax > b  =>  x > ⌊b/a⌋    ax ≥ b  =>  x ≥ ⌈b/a⌉

x<<i ≤ s  =>  x ≤ s>>i    x<<i < s  =>  x ≤ (s-1)>>i
x<<i > s  =>  x > s>>i    x<<i ≥ s  =>  x > (s-1)>>i

1<<x ≤ v  =>  x ≤ v.bit_length()-1    1<<x < v  =>  x ≤ (v-1).bit_length()-1
1<<x > v  =>  x ≥ v.bit_length()      1<<x ≥ v  =>  x ≥ (v-1).bit_length()
"""
