# Make sure to have matlab 2014b or later
# Install MATLAB engine API for python (http://se.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

import matlab.engine
w = 30
h = 30

# num, to name all object different
# val1, value of first constant
# val2, value of second const
# xpos, ypos, pos of first const block
def AddValues(num, val1, val2, xpos, ypos):
    opname = "Add_" + str(num)
    const1name = "Const_" + str(num)  +".1"
    const2name = "Const_" + str(num)  +".2"
    script = "add_block('simulink/Math Operations/Add','my_untitled/" + opname + "');\n " \
             "add_block('simulink/Sources/Constant','my_untitled/" + const1name + "', 'Value','" + str(val1) + "');\n " \
             "add_block('simulink/Sources/Constant','my_untitled/" + const2name + "', 'Value','" + str(val2) + "');\n " \
            "set_param('my_untitled/" + const1name + "','position',[" + str(xpos) + ", " + str(ypos) + ", " + str(xpos+w) + ", " + str(ypos+h) + "]); \n" \
            "set_param('my_untitled/" + const2name + "','position',[" + str(xpos) + ", " + str(ypos+60) + ", " + str(xpos+w) + ", " + str(ypos+60+h) + "]); \n" \
            "set_param('my_untitled/" + opname + "','position',[" + str(xpos + 80) + ", " + str(ypos+30) + ", " + str(xpos+80+w) + ", " + str(ypos+30+h) + "]); \n" \
            "add_line('my_untitled','" + const1name + "/1','" + opname + "/1'); \n" \
             "add_line('my_untitled','" + const2name + "/1','" + opname + "/2');\n "
    return script

# num, to name all object different
# val1, value of first constant
# val2, value of second const
# xpos, ypos, pos of first const block
def SubtractValues(num, val1, val2, xpos, ypos):
    opname = "Sub_" + str(num)
    const1name = "Const_" + str(num)  +".1"
    const2name = "Const_" + str(num)  +".2"
    script = "add_block('simulink/Math Operations/Subtract','my_untitled/" + opname + "');\n " \
             "add_block('simulink/Sources/Constant','my_untitled/" + const1name + "', 'Value','" + str(val1) + "');\n " \
             "add_block('simulink/Sources/Constant','my_untitled/" + const2name + "', 'Value','" + str(val2) + "');\n " \
            "set_param('my_untitled/" + const1name + "','position',[" + str(xpos) + ", " + str(ypos) + ", " + str(xpos+w) + ", " + str(ypos+h) + "]); \n" \
            "set_param('my_untitled/" + const2name + "','position',[" + str(xpos) + ", " + str(ypos+60) + ", " + str(xpos+w) + ", " + str(ypos+60+h) + "]); \n" \
            "set_param('my_untitled/" + opname + "','position',[" + str(xpos + 80) + ", " + str(ypos+30) + ", " + str(xpos+80+w) + ", " + str(ypos+30+h) + "]); \n" \
            "add_line('my_untitled','" + const1name + "/1','" + opname + "/1'); \n" \
             "add_line('my_untitled','" + const2name + "/1','" + opname + "/2');\n "
    return script

if __name__ == '__main__':
    script = "modelname = 'my_untitled';\n" \
             "open_system(new_system(modelname));\n" \
             "set_param(modelname,'ScreenColor','green');\n"

    script += AddValues(1, 5, 7, 10, 10)
    script += SubtractValues(2, 1, 2, 100, 100)
    script +="save_system(modelname);\n "

    with open("myScript.m", "w+") as f:
        f.write(script)

    eng = matlab.engine.start_matlab('-desktop')
    eng.myScript(nargout=0)
    print("done")
    response = raw_input() # Pause the script, press any key to continue

