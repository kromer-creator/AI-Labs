
include "globals.mzn";
include "alldifferent.mzn";
include "among.mzn";

int: Evaluation;  % If 0, use utilitarian utility, if 1, use egalitarian utility
int: nTables;     % Number of tables available
int: nSeats;      % Number of seats at each table
int: nGuests;     % Number of guests in need of seating
int: nGroups;     % Number of groups that wish to be seated together
int: PrefWeight;  % Weight of seating preference
array[1..nGroups] of set of int: Groups;  % Array of the sets of groups that want to be seated together
array[1..nGuests] of set of int: Pref;    % Array of preference weights
set of int: Trouble;      % Set of "troublemakers" who shouldn't be seated together
array [1..nTables] of var set of 1..nGuests: Assignments;  % Stores the seating assignments
array [1..nGuests] of var 1..nTables: Seating;    % Stores the guests that will be seated at each table
var int: utility;    % Variable of calculated utility from seating arrangement


% CONSTRAINTS: 
% Symmetry breaking
constraint int_set_channel(Seating, Assignments);
constraint decreasing(Assignments);

% No table has more people than seats available (nSeats)
constraint forall(table in 1..nTables)(
count(assignment in Seating)(table=assignment) <= nSeats  
);

% Every table must have at least Floor(nSeats/2) people at it
constraint forall(table in 1..nTables)(
count(assignment in Seating)(table=assignment) > floor(nSeats/2)
);

% Every person must be seated with their group
constraint forall(group in 1..nGroups)(
all_equal([Seating[person] | person in Groups[group]])
); 

% Everyone in the set Trouble must be seated at different tables
constraint alldifferent(t in Trouble)(Seating[t]);

% Calculate rest of seating based on pref weights
% Utilitarian calculation
var int: utilitarian = sum(guest in 1..nGuests)(
card (Assignments[Seating[guest]] intersect Pref[guest])*PrefWeight
);
% Egalitarian calculation
var int: egalitarian = min(guest in 1..nGuests)(
card (Assignments[Seating[guest]] intersect Pref[guest])*PrefWeight
);
% Calculate the utility depending on the desired evaluation function
constraint if Evaluation == 0 then utility = utilitarian else utility = egalitarian endif;
% if Evaluation == 0 -> call utilitarian  
% if Evaluation == 1 -> call egalitarian

% Solve for utility
solve maximize utility;

% Output results
        
output ["Table: Guests:\n"] ++ 
  [show(i) ++ ":" ++ show(Seating[i]) ++ "\n" | i in 1..nTables] ++ 
  ["Utilitarian Utility: " ++ show(utilitarian) ++ "\n"] ++
  ["Egalitarian Utility: " ++ show(egalitarian) ++ "\n"]        
