import sys
import os

code_path = os.path.normpath(os.getcwd()+"/../")
utilities_path = os.path.normpath(code_path+"/utilities")
sys.path.insert(1,code_path)
sys.path.insert(1,utilities_path)
import post_process
import utilities.logger
import utilities.abaqus.inp_reader_v2
import utilities.abaqus.inp_tree_processor_v2

# from utilities.logger import main_log

def get_desired_part(parts_list,ap):
	part_name_requested = ap['part_name']
	for part in parts_list:
		if part.label == part_name_requested:
			return part
	# This is reached if the requested part was never found.
	raise Exception("Could not find the part: " + part_name_requested +
				" as requested in the input file.")


if __name__ == '__main__':
    main_log = utilities.logger.main_log
    main_log.info("Post-processing starts.")

    # para_path = os.getcwd()+'/../Cases/Impeller/'
    # para_path = os.getcwd()+'/../Cant3D/'
    para_path = code_path + '/../Cant3D/'
    sys.path.insert(1, para_path)
    import parameters
    ap = parameters.ap
    parsed_inp_file = utilities.abaqus.inp_reader_v2.parse_inp_file(ap['inp_path'])
    parts_list = utilities.abaqus.inp_tree_processor_v2.process_tree(parsed_inp_file)
    part = post_process.get_desired_part(parts_list,ap)
    ## delete parsed parts to release memory
    del parsed_inp_file
    del parts_list
    print(part)