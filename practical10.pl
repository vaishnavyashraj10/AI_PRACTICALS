:- use_module(library(lists)).

goal([1,2,3,4,5,6,7,8,0]).

move(S, N) :-
    nth0(I, S, 0),
    member(D, [-3,3,-1,1]),
    J is I + D,
    J >= 0,
    J < 9,
    (D =\= -1 ; I mod 3 =\= 0),
    (D =\= 1 ; I mod 3 =\= 2),
    nth0(J, S, V),
    replace(S, I, V, T),
    replace(T, J, 0, N).

replace([_|Rest], 0, V, [V|Rest]).

replace([X|Rest], I, V, [X|NewRest]) :-
    I > 0,
    I1 is I - 1,
    replace(Rest, I1, V, NewRest).

solve(Start, Path) :-
    bfs([[Start]], [Start], RevPath),
    reverse(RevPath, Path).

bfs([[S|Rest]|_], _, [S|Rest]) :-
    goal(S).

bfs([[S|Rest]|Queue], Visited, Path) :-
    findall([N,S|Rest],
        (move(S,N), \+ member(N, Visited)),
        NewPaths),
    collect_states(NewPaths, States),
    append(Visited, States, Visited1),
    append(Queue, NewPaths, Queue1),
    bfs(Queue1, Visited1, Path).

collect_states([], []).

collect_states([[S|_]|Rest], [S|States]) :-
    collect_states(Rest, States).