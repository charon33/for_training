import re

path_to_file = str(input("Enter the path to file:"))
resource_file = open(path_to_file, "r")
out_cards = open(path_to_file[:-4] + "_old" + path_to_file[-4:],"w")
pattern_card_number = re.compile(r"\((\d+),")
pattern_card_mainstring = re.compile(r"\d+=\d+=\d+=\d+=\d+")
pattern_card_centercode = re.compile(r"790=(\d+)=")
for line in resource_file:
    result_number = str(pattern_card_number.findall(line)[0])
    result_string = str(pattern_card_mainstring.findall(line)[0])
    print(pattern_card_centercode.findall(line)[0])
    #result_centercode = str(pattern_card_hash.findall(line)[0])
    txt_card = "({0}, '{1}', {2});".format(result_number, result_string, result_centercode) + "\n"
    out_cards.write(txt_card)
print("Job's done")
resource_file.close()
out_cards.close()

