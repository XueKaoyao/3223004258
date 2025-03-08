import sys,re
import cProfile

# 用于读取文件内容的函数
def readfile(url):
    with open(url, 'r', encoding='utf-8') as file:
        return file.read()

# 将论文的每句话拆开成一个字一个字放入集合
def split(text):
    return set(re.findall(r'[\u4e00-\u9fa5]', text))

# 计算相似度
def calculate_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

# 主函数
def main():
    if len(sys.argv) != 4:
        print("请在命令行输入: python 论文查重.py [原文文件] [抄袭版论文的文件] [答案文件]")
        sys.exit(1)

    original_file_path = sys.argv[1]
    plagiarism_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    # 读取原文和抄袭版论文
    original_text = readfile(original_file_path)
    plagiarism_text = readfile(plagiarism_file_path)

    # 分词并计算相似度
    original_split = split(original_text)
    plagiarism_split = split(plagiarism_text)

    similarity = calculate_similarity(original_split, plagiarism_split)

    # 输出结果到文件，保留两位小数
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"{similarity:.2f}")

if __name__ == "__main__":
    main()

# 性能分析
cProfile.run('main()')