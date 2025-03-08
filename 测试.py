import unittest
from 论文查重 import calculate_similarity, split

class TestPlagiarismCheck(unittest.TestCase):

    def test_calculate_similarity(self):
        # 测试相似度计算
        set1 = {"今", "天", "是", "星", "期", "天", "天", "气", "晴"}
        set2 = {"今", "天", "是", "周", "天", "天", "气", "晴", "朗"}
        result = calculate_similarity(set1, set2)
        self.assertAlmostEqual(result, 0.8, places=2)

        set3 = {"今", "天", "天", "气", "晴"}
        set4 = {"天", "气", "晴", "不", "错"}
        result2 = calculate_similarity(set3, set4)
        self.assertAlmostEqual(result2, 0.5, places=2)

    def test_split(self):
        # 测试文本分割函数
        text = "今天是星期天"
        result = split(text)
        expected_result = {"今", "天", "是", "星", "期", "天"}
        self.assertEqual(result, expected_result)

        text2 = "天气晴"
        result2 = split(text2)
        expected_result2 = {"天", "气", "晴"}
        self.assertEqual(result2, expected_result2)

        text3 = "abc123"
        result3 = split(text3)
        expected_result3 = {"abc123"}
        self.assertEqual(result3, expected_result3)


if __name__ == '__main__':
    unittest.main()
