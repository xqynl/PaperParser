import json
import pymupdf

# 读取配置文件
with open('config.json', 'r', encoding='utf8') as fp:
    json_data = json.load(fp)

    paper_path = json_data['paper_path']
    output_path = json_data['output_path']

    file_name = paper_path.rsplit('/', 1)[1]
    paper_name = file_name.rsplit('.', 1)[0]


paper_doc = pymupdf.open(paper_path)


# 按照章节提取paper内容
def extract_chapters(doc):

    # for page_num in doc.page_cout:
    output_file = output_path + "/" + paper_name + '.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for page_num in range(2):
            print('hello')
            page = doc.load_page(0)
            # text_dict = page.get_text('dict')
            # f.write(str(text_dict))
            text = page.get_text('text')
            f.write(str(text))


# 判断文字是否在合适的图片区域
def is_text_in_image_area(span):
    # 可以根据 span['bbox'] (文本块的边界框) 和图片的位置关系，做进一步的过滤
    pass



def main():
    extract_chapters(paper_doc)
    return


if __name__ == "__main__":
    main()
