##load "str.cma";;

let read_file filename = 
  let ic = open_in filename in 
  let rec read_lines accumulator =
    match input_line ic with
    | line -> read_lines (line :: accumulator)
    | exception End_of_file -> List.rev accumulator
  in
  let lines = read_lines [] in
  close_in ic;
  lines
;;

let substring_index string substring = 
  let string_len = String.length string in
  let substring_len = String.length substring in 
  let rec find_index index = 
    if index + substring_len > string_len then -1
    else if String.sub string index substring_len = substring then index
    else find_index (index + 1)
  in 
  find_index 0
;;

let rec do_all func lst = 
  match lst with 
  | [] -> ()
  | head::tail -> func head; do_all func tail
;;

(* let rec get_mul_from_start string = 
  let rec find_end = 
     *)
  


let () =
  (* let lines = read_file "day_3/day_3.in" in 
  let substring = "mul(" in
  let index = substring_index (List.nth lines 0) substring in
  
   *)
   let regex = Str.regexp "mul([0-9]{1,3},[0-9]{1,3})" in
   let matched = Str.string_match regex "mul(10,32)" 0 in
   Printf.printf "%b" matched
