from rembg import remove
import os


input_path = r'D:\Hendry\rmbg\input'
output_path =  r'D:\Hendry\rmbg\output'


for root, dirs, files in os.walk(input_path):
    for filename in files:
        with open(os.path.join(root, filename), 'rb') as i:
            output_path_ = os.path.join(output_path, filename)
            with open(output_path_, 'wb') as o:
                input_data = i.read()
                
                output_data = remove(input_data)
                
                o.write(output_data) 