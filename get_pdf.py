from pdfrw import PdfFileReader,PdfWriter
import os
text = """
******************************************************************
 工具名称:PDF图纸包制作工具
 使用说明:
         1.文件夹内必须有"图纸PDF"文件夹和"要打印的图纸.txt"文件
           所有PDF图纸存放在里面
         2.复制流程卡里整理好的图号粘贴到"要打印的图纸.txt"内保存
         3.运行"get_pdf.exe"按照提示操作,如有未找到的图纸
           把找到的图纸加入进"图纸PDF"内重新运行
******************************************************************
"""
def all_pdf():
    y = PdfWriter()
    lost = []
    if os.path.exists('未找到的图纸.txt'):
        os.remove('未找到的图纸.txt')
    with open('要打印的图纸.txt','r') as f:
        for i in f.readlines():
            tuzhi = '图纸PDF\\'+i.strip().strip('\n')+'.pdf'
            if os.path.exists(tuzhi):
                x = PdfFileReader(tuzhi)
                y.addpage(x.pages[0])
            else:
                lost.append(i)
    with open('未找到的图纸.txt','a') as f:
        f.write('没有找到的图纸:\n')
        for i in lost:
            f.write(i)
            print('没有找到的图纸:%s'%i.strip('\n'))
    return  y.write('pdf包.pdf')
def main():
    print(text)
    input('按回车键开始制作PDF包:')
    all_pdf()
    input('PDF包已制作完成,请按回车键结束程序:')
if __name__ == '__main__':
    main()