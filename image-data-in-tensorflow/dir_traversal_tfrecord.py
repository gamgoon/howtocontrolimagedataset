# 참고 : http://yeephycho.github.io/2016/08/15/image-data-in-tensorflow/
import os # 시스템 경로, 파일명 처리
import tensorflow as tf

# tfrecord 파일 리스트 출력 및 리턴
def list_tfrecord_file(file_list):
    tfrecord_list = []
    for i in range(len(file_list)):
        current_file_abs_path = os.path.abspath(file_list[i])
        if current_file_abs_path.endswith(".tfrecord"):
            tfrecord_list.append(current_file_abs_path)
            print("Found %s successfully!" % file_list[i])
        else:
            pass
    return tfrecord_list

# 현재 디렉토리 순회
def tfrecord_auto_traversal():
    current_folder_filename_list = os.listdir("./")
    if current_folder_filename_list != None:
        print("%s files were found under current folder. " % len(current_folder_filename_list))
        print("Please be noted that only files end with '*.tfrecord' will be load!")
        tfrecord_list = list_tfrecord_file(current_folder_filename_list)
        if len(tfrecord_list) != 0:
            for list_index in range(len(tfrecord_list)):
                print(tfrecord_list[list_index])
        else:
            print("Cannot find any tfrecord files, please check the path.")
    return tfrecord_list

def main():
    tfrecord_list = tfrecord_auto_traversal()

if __name__ == "__main__":
    main()