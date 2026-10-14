% Facts
male(ram).
male(amit).
male(raj).

female(sita).
female(gita).
female(neha).

parent(ram, amit).
parent(sita, amit).
parent(ram, gita).
parent(sita, gita).
parent(amit, raj).
parent(neha, raj).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y)