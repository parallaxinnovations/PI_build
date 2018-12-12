import os
import re
import sys
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

def rewrite_egg(egg_path):
    """Create an egg that works with MicroView in python3"""

    RE_PYCACHE_FILE3 = re.compile('(.*)\.cp3\d-(.*)(.pyd)$')

    cache_tag = sys.implementation.cache_tag

    with tempfile.TemporaryDirectory() as tmpdir:
        names_lst = []
        tmpdir_abs_path = os.path.abspath(tmpdir)
        with ZipFile(egg_path, 'r') as zf:
            for name in zf.namelist():

                w_name = name
                w_name = w_name.replace('__pycache_/', '')
                w_name = w_name.replace(cache_tag+'.', '')
#                m = RE_PYCACHE_FILE3.match(w_name)
#                if m:
#                    w_name = m.groups()[0] + m.groups()[2]

                w_path = os.path.join(tmpdir_abs_path, w_name)
                dir_path = os.path.dirname(w_path)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                with open(w_path, 'wb') as file_to_write:
                    with zf.open(name) as file_to_read:
                        file_to_write.write(file_to_read.read())
                names_lst.append(w_name)
        with ZipFile(egg_path, 'w', compression=ZIP_DEFLATED) as zf:
            for name in names_lst:
                r_path = os.path.join(tmpdir_abs_path, name)
                zf.write(r_path, arcname=name)
