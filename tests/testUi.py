import easygui as box1
import sys
while 1:
    ## 初始界面
    msg = "请输入明文"
    title = "Elgamal机制演示"
    fieldNames = ["明文数据："]
    fieldValues = []
    fieldValues = box1.enterbox(msg, title, fieldNames)
    print(fieldValues)
    box1.msgbox("Hello,Elgamal机制演示","203某小组")
    ## 选择界面
    msg = "请问你想选择哪组数据展示演示过程？"
    title = "Elgamal机制演示"
    choices = ["数据一","数据二","数据三","数据四","数据五"]
    choice = box1.choicebox(msg,title,choices)

    box1.msgbox("你的选择是：" +str(choice),"结果")

    ## 展示界面
    box1.msgbox("现在展示：" +str(choice)+ "的流程", str(choice) + "流程展示")

    ## 循环选择
    msg = "你希望重新选择一组数据吗？"
    title = "请选择！"

    if box1.ccbox(msg,title):
            pass
    else:
            sys.exit(0)







