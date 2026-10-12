hanoi(1, Source, _, Target) :-
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Target),
    nl.

hanoi(N, Source, Auxiliary, Target) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Target, Auxiliary),
    hanoi(1, Source, Auxiliary, Target),
    hanoi(M, Auxiliary, Source, Target).