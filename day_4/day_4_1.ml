let read_file filename = 
  let ic = open_in filename in
  let rec read_lines acc = 
    match input_line ic with 
    | line -> read_lines (line :: acc)
    | exception End_of_file -> List.rev acc
  in
  let lines = read_lines [] in
  close_in ic;
  lines
;;

let () =
  let lines = read_file "day_4/day_4.in" in
  
