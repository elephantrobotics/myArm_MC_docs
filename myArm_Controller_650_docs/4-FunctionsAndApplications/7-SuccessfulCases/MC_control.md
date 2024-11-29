# C650 control M750 program example

## Program address
> https://github.com/elephantrobotics/pymycobot/tree/main/demo/myArm_M%26C_demo_v1.1

## Installation dependency

```shell
pip install -r requirement.txt
```

## Run the program

```shell
python main.py
```

## Program instructions

> There is a sequence requirement for opening the serial port: open the serial port connection of myArmM first, and then open the serial port connection of myArmC.

<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1 -BasedOnPythonDevelopmentAndUse/6_example/app_1.png" alt="7.1.1-7" style="zoom: 50%;" />

<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1 -BasedOnPythonDevelopmentAndUse/6_example/app_2.png" alt="7.1.1-1" style="zoom: 50%;" />

> After both serial ports are enabled, you can control the movement of myArmM by moving myArmC.

---