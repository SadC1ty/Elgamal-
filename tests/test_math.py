import unittest
import elgamal
import easygui as box1
import sys


class GreatestCommonDivisorTests(unittest.TestCase):
    while 1:
        ## 初始界面
        box1.msgbox("Hello,Elgamal机制演示", "203某小组")
        ## 选择界面
        msg = "请问你想选择哪组数据展示演示过程？"
        title = "Elgamal机制演示"
        choices = ["数据一", "数据二", "数据三", "数据四", "数据五"]
        choice = box1.choicebox(msg, title, choices)

        box1.msgbox("你的选择是：" + str(choice), "结果")

        ## 展示界面
        box1.msgbox("现在展示：" + str(choice) + "的流程", str(choice) + "流程展示")

        ## 循环选择
        msg = "你希望重新选择一组数据吗？"
        title = "请选择！"

        if box1.ccbox(msg, title):
            pass
        else:
            sys.exit(0)
    def test_zero(self):
        self.assertEqual(elgamal.gcd(0, 0), 0)

    def test_any_number_and__one_returns_one(self):
        self.assertEqual(elgamal.gcd(1, 1), 1)
        self.assertEqual(elgamal.gcd(2, 1), 1)
        self.assertEqual(elgamal.gcd(3, 1), 1)

    def test_primes_are_divided_by_one(self):
        self.assertEqual(elgamal.gcd(3, 2), 1)
        self.assertEqual(elgamal.gcd(5, 3), 1)
        self.assertEqual(elgamal.gcd(7, 3), 1)
        self.assertEqual(elgamal.gcd(11, 7), 1)
        self.assertEqual(elgamal.gcd(13, 5), 1)
        self.assertEqual(elgamal.gcd(17, 2), 1)

    def test_coprimes_are_divided_by_one(self):
        self.assertEqual(elgamal.gcd(9, 8), 1)

    def test_not_coprime(self):
        self.assertNotEqual(elgamal.gcd(10, 20), 1)

if __name__ == '__main__':
    unittest.main()

