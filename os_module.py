import os

print(os.getcwd())

# chck_dir = os.path.exists("OS_MODULE_SAMPLE")
if not os.path.exists("OS_MODULE_SAMPLE"):
    os.makedirs('OS_MODULE_SAMPLE')
else:
    print("Meron ng OS_MODULE_SAMPLE")


hold_cwd = os.path.abspath("OS_MODULE_SAMPLE")
print("hold cwd>", hold_cwd)
if not os.path.exists("" + hold_cwd + "\\INSIDE_OS_MODULE_SAMPLE"):
    os.makedirs("" + hold_cwd + "\\INSIDE_OS_MODULE_SAMPLE")
