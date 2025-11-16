# 这个文件是要转换大小写的文件
import random
ls=[]
random.seed(10)
for i in range(10):
    a=random.randint(0,100)
    ls.append(a)
print(ls)
import keyword

def convert_python_file(input_file, output_file):
    # 读取输入文件内容
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有Python保留字（全小写）
    reserved_words = set(keyword.kwlist)
    converted_content = []
    i = 0
    n = len(content)
    
    while i < n:
        # 找到字母序列的起始位置
        if content[i].isalpha():
            start = i
            # 找到字母序列的结束位置
            while i < n and content[i].isalpha():
                i += 1
            word = content[start:i]
            # 检查是否为保留字（保留字都是小写）
            if word.lower() in reserved_words:
                converted_content.append(word)  # 保留原大小写
            else:
                converted_content.append(word.upper())  # 转换为大写
        else:
            # 非字母字符直接保留
            converted_content.append(content[i])
            i += 1
    
    # 将处理后的内容写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(converted_content))

if __name__ == "__main__":
    input_filename = "random_int.py"
    output_filename = "random_int_converted.py"
    convert_python_file(input_filename, output_filename)
    print(f"转换完成，结果已保存至 {output_filename}")
