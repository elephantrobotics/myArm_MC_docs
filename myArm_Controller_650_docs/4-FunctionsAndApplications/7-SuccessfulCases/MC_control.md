# C650控制M750程序案例

## 程序地址
> https://github.com/elephantrobotics/pymycobot/tree/main/demo/myArm_M%26C_demo_v1.1

## 安装依赖

```shell
pip install -r requirement.txt
```

## 运行程序

```shell
python main.py
```

## 程序使用说明

> 串口的打开有顺序要求：先开启 myArmM 的串口连接，再开启 myArmC 的串口连接。

<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1 -BasedOnPythonDevelopmentAndUse/6_example/app_1.png" alt="7.1.1-7" style="zoom: 50%;" />

<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.1 -BasedOnPythonDevelopmentAndUse/6_example/app_2.png" alt="7.1.1-1" style="zoom: 50%;" />

> 两个串口都开启以后就可以通过移动 myArmC 来控制 myArmM 运动。

---