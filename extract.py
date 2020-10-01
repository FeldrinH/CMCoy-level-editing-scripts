import sys
import os
from decode_image import decode_image
from decode_xml_to_ogmo import decode_xml_to_ogmo

swf_path = sys.argv[1]
project_dir_path = sys.argv[2]

os.makedirs(project_dir_path, exist_ok=True)
os.chdir(project_dir_path)

decode_xml_to_ogmo()
