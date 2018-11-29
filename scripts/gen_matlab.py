# Make sure to have matlab 2014b or later
# Install MATLAB engine API for python (http://se.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

import matlab.engine


class GenMatlab:
    def __init__(self, operand, block_w, block_h):
        self.operand = operand
        self.block_w = block_w
        self.block_h = block_h

        self.run()

    def run(self):
        script = "modelname = 'my_untitled';\n" \
                 "open_system(new_system(modelname));\n" \
                 "set_param(modelname,'ScreenColor','green');\n"

        if self.operand == "Add":

        elif self.operand == "Subtract":

        elif self.operand == "Product":

        elif self.operand == "Constant":

        else:
            raise Exception("Block not yet implemented.")

    def AddValues(self, num, val1, val2, xpos, ypos):
        # num, to name all object different
        # val1, value of first constant
        # val2, value of second const
        # xpos, ypos, pos of first const block

        opname = "Add_" + str(num)
        const1name = "Const_" + str(num)  +".1"
        const2name = "Const_" + str(num)  +".2"
        script = "add_block('simulink/Math Operations/Add','my_untitled/" + opname + "');\n " \
                 "add_block('simulink/Sources/Constant','my_untitled/" + const1name + "', 'Value','" + str(val1) + "');\n "\
                 "add_block('simulink/Sources/Constant','my_untitled/" + const2name + "', 'Value','" + str(val2) + "');\n "\
                 "set_param('my_untitled/" + const1name + "','position',[" + str(xpos) + ", " + str(ypos) + ", " + str(xpos+self.block_w) + ", " + str(ypos+self.block_h) + "]); \n" \
                 "set_param('my_untitled/" + const2name + "','position',[" + str(xpos) + ", " + str(ypos+60) + ", " + str(xpos+self.block_w) + ", " + str(ypos+60+self.block_h) + "]); \n" \
                 "set_param('my_untitled/" + opname + "','position',[" + str(xpos + 80) + ", " + str(ypos+30) + ", " + str(xpos+80+self.block_w) + ", " + str(ypos+30+self.block_h) + "]); \n" \
                 "add_line('my_untitled','" + const1name + "/1','" + opname + "/1'); \n" \
                 "add_line('my_untitled','" + const2name + "/1','" + opname + "/2');\n "
        return script


    def SubtractValues(self, num, val1, val2, xpos, ypos):
        # num, to name all object different
        # val1, value of first constant
        # val2, value of second const
        # xpos, ypos, pos of first const block

        opname = "Sub_" + str(num)
        const1name = "Const_" + str(num)  +".1"
        const2name = "Const_" + str(num)  +".2"
        script = "add_block('simulink/Math Operations/Subtract','my_untitled/" + opname + "');\n " \
                 "add_block('simulink/Sources/Constant','my_untitled/" + const1name + "', 'Value','" + str(val1) + "');\n " \
                 "add_block('simulink/Sources/Constant','my_untitled/" + const2name + "', 'Value','" + str(val2) + "');\n " \
                 "set_param('my_untitled/" + const1name + "','position',[" + str(xpos) + ", " + str(ypos) + ", " + str(xpos+self.block_w) + ", " + str(ypos+self.block_h) + "]); \n" \
                 "set_param('my_untitled/" + const2name + "','position',[" + str(xpos) + ", " + str(ypos+60) + ", " + str(xpos+self.block_w) + ", " + str(ypos+60+self.block_h) + "]); \n" \
                 "set_param('my_untitled/" + opname + "','position',[" + str(xpos + 80) + ", " + str(ypos+30) + ", " + str(xpos+80+self.block_w) + ", " + str(ypos+30+self.block_h) + "]); \n" \
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

