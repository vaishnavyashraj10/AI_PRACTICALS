:- use_module(library(lists)).

queens(N, Solution) :-
    numlist(1, N, Columns),
    permutation(Columns, Solution),
    safe(Solution).

safe([]).

safe([Q|Rest]) :-
    safe(Rest, Q, 1),
    safe(Rest).

safe([], _, _).

safe([Q|Rest], Previous, Distance) :-
    abs(Q - Previous) =\= Distance,
    D1 is Distance + 1,
    safe(Rest, Q, D1).