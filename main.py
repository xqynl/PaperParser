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
        for page_num in range(1):
            print('hello')
            page = doc.load_page(0)
            text_dict = page.get_text('dict')
            f.write(str(text_dict))
            # for block in text_dict['blocks']:
            #     if block['type'] == 0:
            #         for line in block['lines']:
            #             for span in line['spans']:
            #                 # 判断文本是否在合理的区域
            # print(text_dict)


    # text = ""
    # for block in text_dict["blocks"]:
    #     if block['type'] == 0:  # 只有文本块类型是0的才是文本
    #         for line in block["lines"]:
    #             for span in line["spans"]:
    #                 # 判断文本是否在合理的区域
    #                 if not is_text_in_image_area(span):  # 自定义判断逻辑
    #                     text += span['text'] + " "
    #
    # print(text)


def is_text_in_image_area(span):
    # 可以根据 span['bbox'] (文本块的边界框) 和图片的位置关系，做进一步的过滤
    # bbox: [x0, y0, x1, y1]，可以通过对比坐标来判断文本是否在图片区域
    pass


if __name__ == "__main__":
    extract_chapters(paper_doc)
