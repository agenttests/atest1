import sys
try:
    import py2exe
except:
    raw_input('Please install py2exe first...')
    sys.exit(-1)

from distutils.core import setup
import shutil

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {'bundle_files': 1, 'compressed': True}
    },
    console=[
        {'script': "MBRprotect_tester.py"}
    ],
    zipfile=None,
)

shutil.move('dist\\MBRprotect_tester.exe', '.\\MBRprotect_tester.exe')
shutil.rmtree('build')
shutil.rmtree('dist')