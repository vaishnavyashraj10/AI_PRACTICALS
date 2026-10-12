% Distances between cities
edge(a, b, 10).
edge(a, c, 15).
edge(a, d, 20).
edge(b, c, 35).
edge(b, d, 25).
edge(c, d, 30).

distance(X, Y, D) :- edge(X, Y, D).
distance(X, Y, D) :- edge(Y, X, D).

route([X,Y], D) :-
    distance(X, Y, D).

route([X,Y|Rest], Total) :-
    distance(X, Y, D1),
    route([Y|Rest], D2),
    Total is D1 + D2.

tsp(Start, BestRoute, BestCost) :-
    findall(Cost-Route,
        (permutation([b,c,d], Others),
         Route = [Start|Others],
         append(Route, [Start], FullRoute),
         route(FullRoute, Cost)),
        Options),
    keysort(Options, [BestCost-BestRoute|_]).