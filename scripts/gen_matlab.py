# Make sure to have matlab 2014b or later
# Install MATLAB engine API for python (http://se.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)

import matlab.engine


class GenMatlab:
    def __init__(self):
        self.script = "modelname = 'my_untitled';\n" \
                 "open_system(new_system(modelname));\n"

        self.ypos = 20


    def run(self, id, operand, const1, const2, block_w, block_h):
        self.operand = operand
        self.const1 = const1
        self.const2 = const2
        self.block_w = block_w
        self.block_h = block_h
        self.id = id

        if self.operand == "add":
            self.operand = "Add"
            self.script += self.AddValues(20, self.ypos)
        elif self.operand == "subtract":
            self.operand = "Subtract"
            self.script += self.AddValues(20, self.ypos)
        elif self.operand == "product":
            self.operand = "Product"
            self.script += self.AddValues(20, self.ypos)
        elif self.operand == "Constant":
            const1name = "Const_" + str(self.id)
            self.script += "add_block('simulink/Sources/Constant','my_untitled/" + const1name + "', 'Value','" + str(self.const1) + "');\n"
        else:
            raise Exception("Block not yet implemented.")

    def push_to_matlab(self):
        self.script += "save_system(modelname);\n "
        with open("myScript.m", "w+") as f:
            f.write(self.script)

        eng = matlab.engine.start_matlab('-desktop')
        eng.myScript(nargout=0)
        print("done")
        response = raw_input()  # Pause the script, press any key to continue

    def AddValues(self, xpos, ypos):
        # num, to name all object different
        # val1, value of first constant
        # val2, value of second const
        # xpos, ypos, pos of first const block

        opname = "Operand_" + str(self.id)
        const1name = "Const_" + str(self.id)  +".1"
        const2name = "Const_" + str(self.id)  +".2"
        script = "add_block('simulink/Math Operations/" + self.operand + "','my_untitled/" + opname + "');\n" \
                 "add_block('simulink/Sources/Constant','my_untitled/" + const1name + "', 'Value','" + str(self.const1) + "');\n"\
                 "add_block('simulink/Sources/Constant','my_untitled/" + const2name + "', 'Value','" + str(self.const2) + "');\n"\
                 "set_param('my_untitled/" + const1name + "','position',[" + str(xpos) + ", " + str(ypos) + ", " + str(xpos+self.block_w) + ", " + str(ypos+self.block_h) + "]); \n" \
                 "set_param('my_untitled/" + const2name + "','position',[" + str(xpos) + ", " + str(ypos+60) + ", " + str(xpos+self.block_w) + ", " + str(ypos+60+self.block_h) + "]); \n" \
                 "set_param('my_untitled/" + opname + "','position',[" + str(xpos + 80) + ", " + str(ypos+30) + ", " + str(xpos+80+self.block_w) + ", " + str(ypos+30+self.block_h) + "]); \n" \
                 "add_line('my_untitled','" + const1name + "/1','" + opname + "/1'); \n" \
                 "add_line('my_untitled','" + const2name + "/1','" + opname + "/2');\n"
        self.ypos += 130
        return script

if __name__ == '__main__':
    mat = GenMatlab()
    mat.run(1, "add", 5, 6, 30, 30)
    mat.run(2, "product", 2, 3, 30, 30)
    mat.run(3, "subtract", 8, 9, 30, 30)
    mat.run(4, "subtract", 8, 9, 30, 30)
    mat.push_to_matlab()

