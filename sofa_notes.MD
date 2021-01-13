# Soft Manipulator

1. *Installation:* The latest version of SOFA is available from https://www.sofa-framework.org. However, it does no allow .pyscn files, which are essential for the Sofapython environment and required some packages to be built from source. A modified version of 19.06 available at https://github.com/SofaDefrost/SoftRobots/tree/v19.06.1 contains working binaries of all required packages and allows .pyscn files.<br>

2. *Opening the simulator:* In MacOS, SOFA uses a specific version of Python2 that does not allow external libarires such as pandas and matplotlib. Fortunately, there is a workaround if Linux is used. Instead of double clicking on the executable file, open SOFA by executing the command ./runSofa from the  the 'SOFA_v19.06.99_custom_Linux_v5.1/bin' folder.<br>

3. *Mouse Interaction:* To check the response to external forces, press <code>Shift</code> and click+Drag on the part of the robot where you want the force to be applied.<br>

4. *Wrong key mapping:* In the documentation for Cablegripper / Pneunetgripper tutorials, it's mentioned that the robot can be actuated by pressing the <code>Ctrl + (+/-)</code> keys. However, a slight modification is required in the pythonController file. The line if <code>(c == "-"):</code> in the onKeyPressed function should be changed to <code>(c == "=")</code>.

