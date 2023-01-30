is_a(dog, mammal).
is_a(cat, mammal).
is_a(mammal, animal).
is_a(fish, animal).

descendant(X, Y) :- is_a(X, Y).
descendant(X, Y) :- is_a(X, Z), descendant(Z, Y).
