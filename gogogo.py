from office.ppt.ppt2txt import extract_text_from_ppt


def go_ppt2txt():
    ppt_file_path = '/Users/chengpeng/Documents/下载文献/管理文档/以结果为导向的执行力PPT-太阳美公司.pptx'
    output_text_file = '/Users/chengpeng/Downloads/text.txt'
    extract_text_from_ppt(ppt_file_path, output_text_file)

go_ppt2txt()