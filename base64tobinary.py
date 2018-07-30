import base64

path_to_file = str(input("Enter the path to file:"))
resource_file = open(path_to_file, "r")
out_file = open(path_to_file + "_binary","wb")
resource_file_bin = resource_file.read()
decoded_resource_file = base64.decodebytes(resource_file_bin.encode())
out_file.write(decoded_resource_file)
resource_file.close()
out_file.close()