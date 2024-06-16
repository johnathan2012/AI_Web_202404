ary = 15, 30    # tuple
one, two = ary  # Unpacking

print('Before swap:{}, {}'.format(one, two))

one, two = two, one
print('After swap:{}, {}'.format(one ,two))
