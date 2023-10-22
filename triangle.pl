% Define the predicate to check if a triangle is a right triangle.
is_right_triangle(A, B, C) :-
    % Convert degrees to radians
    RadianA is A * pi / 180,
    RadianB is B * pi / 180,
    RadianC is C * pi / 180,
    
    % Check if the sum of the squares of two smaller angles is equal to the square of the largest angle.
    (abs(sin(RadianA) * sin(RadianA) + cos(RadianA) * cos(RadianA) - (sin(RadianB) * sin(RadianB) + cos(RadianB) * cos(RadianB)) < 1e-10;
    abs(sin(RadianA) * sin(RadianA) + cos(RadianA) * cos(RadianA) - (sin(RadianC) * sin(RadianC) + cos(RadianC) * cos(RadianC)) < 1e-10;
    abs(sin(RadianB) * sin(RadianB) + cos(RadianB) * cos(RadianB) - (sin(RadianC) * sin(RadianC) + cos(RadianC) * cos(RadianC)) < 1e-10).

% Example usage:
% Check if a triangle with angles 30, 60, and 90 degrees is a right triangle.
?- is_right_triangle(30, 60, 90).


