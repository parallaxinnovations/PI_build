import os
import re
import tempfile
from zipfile import ZipFile, ZIP_DEFLATED

def rewrite_egg(egg_path):
    """Create an egg that works with MicroView in python3"""

    RE_PYCACHE_FILE = re.compile('(.*/)(.+)\.cpython-3\d(.*)(.pyc|.pyo)$')
    RE_PYCACHE_FILE2 = re.compile('(.*)\.cpython-3\d(.*)(.pyc|.pyo)$')

    with tempfile.TemporaryDirectory() as tmpdir:
        names_lst = []
        tmpdir_abs_path = os.path.abspath(tmpdir)
        with ZipFile(egg_path, 'r') as zf:
            for name in zf.namelist():

#                if '__pycache__' in name:
#                    import pdb
#                    pdb.set_trace()

                if 'cpython-3' in name:
                    if name.startswith('__pycache__'):
                        m = RE_PYCACHE_FILE2.match(name)
                        w_name = m.group(1) + m.group(3)
                    else:
                        m = RE_PYCACHE_FILE.match(name)
                        if m:
                            w_name = m.group(1) + m.group(2) + m.group(4)
                        else:
                            w_name = name
                else:
                    w_name = name

                w_name = w_name.replace('__pycache__/', '')

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
