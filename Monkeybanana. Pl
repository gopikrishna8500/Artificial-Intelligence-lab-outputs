room(state(at_door, on_floor, has_not)).

% Define the rules for the monkey's actions
move(climb_box, state(at_door, on_floor, has_not), state(at_box, on_box, has_not)).
move(grasp_banana, state(at_box, on_box, has_not), state(at_box, on_box, has)).
move(climb_down, state(at_box, on_box, has), state(at_door, on_floor, has)).

% Define a rule for a valid sequence of actions
solve_problem(state(_, _, has), []).
solve_problem(State, [Move|Moves]) :-
    move(Move, State, NextState),
    solve_problem(NextState, Moves).
