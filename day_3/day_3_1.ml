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



let get_mul_from_start string = 
  let regex = Str.regexp "mul([0-9]+,[0-9]+)" in
  let rec find_end index =
    if index > String.length string || index > 12 then -1 
    else if Str.string_match regex (String.sub string 0 index) 0 then index
    else find_end (index + 1)
  in
  let index = find_end 0 in
  if index == -1 then ""
  else String.sub string 0 index
;;

let rec get_all_muls string acc = 
  (* Printf.printf "%s\n" string; *)
  let substring = "mul(" in
  let substring_length = String.length substring in
  match string with
  | "" -> acc
  | _ -> 
    let index = substring_index string substring in
    if index == -1 then acc
    else 
      let trimmed_string = String.sub string index (String.length string - index) in
      let mul_occurence = get_mul_from_start trimmed_string in
      if String.length mul_occurence == 0 then 
        let new_string = String.sub trimmed_string substring_length (String.length trimmed_string - substring_length) in
        get_all_muls new_string acc
      else 
        let mul_occurence_length = String.length mul_occurence in
        let final_trimmed_string = String.sub trimmed_string mul_occurence_length (String.length trimmed_string - mul_occurence_length) in
        get_all_muls final_trimmed_string (mul_occurence :: acc)
    ;;
    
let multiply string = 
  let trimmed_front = String.sub string 4 (String.length string - 4) in
  let trimmed = String.sub trimmed_front 0 (String.length trimmed_front - 1) in
  let string_nums = Str.split(Str.regexp ",") trimmed in
  let operand1 = int_of_string(List.nth string_nums 0)  in
  let operand2 = int_of_string(List.nth string_nums 1)  in
  operand1 * operand2;;



let () =
  let lines = read_file "day_3/day_3.in" in 
  let get_line_total line = List.fold_left (fun acc str -> acc + multiply str) 0 (get_all_muls line []) in
  let total = List.fold_left (fun acc line -> acc + get_line_total line) 0 lines in
  Printf.printf "%d \n" total

   
