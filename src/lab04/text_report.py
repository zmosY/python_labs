from src.lab04.io_txt_csv import read_text,write_csv
from other.utils import get_project_root
from src.lab03.text_stats import text_stats
from src.lib.text import *

def text_rep(input, output,encoding = 'utf-8'):
    """
    input: Относительный путь к входному файлу (от корня проекта), например "data/lab04/input.txt"
    output: Относительный путь к выходному CSV-файлу, например "data/lab04/report.csv"
    """

    project_root = get_project_root()

    input_path = project_root / input
    output_path = project_root / output

    txt = read_text(input_path,encoding=encoding)
    # print(txt)
    text_stats(txt)
    txt = top_n(count_freq(tokenize(normalize(txt))))
    # print(txt)
    txt = [('word','count')] + txt
    write_csv(txt, output_path)



#test_A
# text_rep("data/lab04/test_A/input.txt","data/lab04/test_A/result.csv")

#test_B
# text_rep("data/lab04/test_B/input.txt","data/lab04/test_B/result.csv")

#test_C
# text_rep("data/lab04/test_C/input.txt","data/lab04/test_C/result.csv",encoding='cp1251')

def text_rep_multi(input : list, output,encoding = 'utf-8'):
    """
    input: Спиксок из Относительных путей к входным файлам (от корня проекта), например ["data/lab04/a.txt, data/lab04/b.txt"]"
    output: Относительный путь к выходной папке в которой будет лежать report_per_file.csv и report_per_file.csv, например "data/lab04"
    """
    project_root = get_project_root()

    output_path = project_root / output / 'report_per_file.csv'
    txt_per_file = []
    txt_total = ''
    for i in range(len(input)):
        input_path = project_root / input[i]
        txt = read_text(input_path, encoding=encoding)
        txt_total += ' ' + txt
        txt = top_n(count_freq(tokenize(normalize(txt))))
        txt = [(input_path.name,) + i for i in txt]
        txt_per_file += txt
    txt_per_file = [('file','world','count')] + txt_per_file
    write_csv(txt_per_file, output_path)

    output_path = project_root / output / 'report_total.csv'
    txt_total = top_n(count_freq(tokenize(normalize(txt_total))))
    txt_total = [('word','count')] + txt_total
    write_csv(txt_total, output_path)

#test_D
text_rep_multi(['data/lab04/test_D/a.txt','data/lab04/test_D/b.txt'],"data/lab04/test_D")
