auto(); // 自动打开无障碍服务，注意平板屏幕要横着放置，因为脚本代码是根据平板横置写的。

/*判断屏幕锁定，解锁屏幕  小米平板的滑动解锁用auto.js 不能模拟 所以直接在“开发者选项中” 开启“直接进入系统”功能*/
if (!device.isScreenOn()) {//息屏状态将屏幕唤醒
        device.wakeUp();//唤醒设备
        sleep(1000); // 等待屏幕亮起

        //miui10 向上锁屏滑动不论是swipe函数还是gtesure函数都不行，miui9之前是可以的
        // 直接进入开发者模式，启动“点亮屏幕直接进入桌面” 
    }

// 启动 Termux
var appName = "Termux"
launchApp(appName);
sleep(2000); // 等待2s

// 在平板界面弹出的键盘输入“crond start”并回车
click(766,1047);
click(668,803);
click(1620,807);
click(1346,1048);
click(572,922);
click(954,1151);
click(385,932);
click(861,809);
click(193,933);
click(679,807);
click(862,806);
click(1750,1154);


sleep(600000); //等待10min

// 输入“exit”退出Termux 
click(478,809);
click(578,1048);
click(1434,794);
click(859,800);
click(1750,1154);

/* 返回桌面
back(); // 模拟按下返回键。
back();*/
