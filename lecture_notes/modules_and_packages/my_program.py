# import from a single module
from my_module import my_func

my_func()

# import from a package (directory)
from my_main_package import some_main_script

# import from a subpackage (subdirectory)
from my_main_package.my_subpackage import my_sub_script

some_main_script.report_main()
my_sub_script.sub_report()


