import re

path_to_file = str(input("Enter the path to file:"))
resource_file = open(path_to_file, "r")
out_cards = open(path_to_file[:-4] + "_cards" + path_to_file[-4:],"w")
out_hash = open(path_to_file[:-4] + "_hashes" + path_to_file[-4:],"w")
pattern_card_number = re.compile(r"\((\d+),")
pattern_card_mainstring = re.compile(r"\d+=\d+=\d+=\d+=\d+")
pattern_card_hash = re.compile(r"\dx\w+")
for line in resource_file:
    result_number = str(pattern_card_number.findall(line)[0])
    result_string = str(pattern_card_mainstring.findall(line)[0])
    result_hash = str(pattern_card_hash.findall(line)[0])
    txt_card = "insert into [gkArcade].[gk].[GK_CARDS](card,card_code) values ({0}, \
'{1}');".format(result_number, result_string) + "\n"
    txt_hash = "insert into [gkArcade].[gk].[GK_CARDS_EXT](card,Extra) values ({0},\
convert( binary(260),'{1}'));".format(result_number, result_hash) + "\n"
    out_hash.write(txt_hash)
    out_cards.write(txt_card)
print("Job's done")
out_hash.close()
resource_file.close()
out_cards.close()

