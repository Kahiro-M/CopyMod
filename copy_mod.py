import os
import shutil
from datetime import datetime, timedelta

def copy_files(file_list, destination_dir):
    try:
        # コピー先ディレクトリが存在しない場合は作成する
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        result_list = []
        for file_path in file_list:
            # コピー元ファイルが存在するか確認する
            if not os.path.isfile(file_path):
                print(f"Error: ファイル '{file_path}' が存在しません。スキップします。")
            else:
                # ファイルをコピーする準備
                file_name = os.path.basename(file_path)
                destination_path = os.path.join(destination_dir, file_name)

                # コピー先ディレクトリに同じファイルが存在するか確認する
                if os.path.exists(destination_path):
                    print(f"ファイル '{destination_path}' はすでに存在します。スキップします。")
                else:
                    # ファイルをコピーする（更新日時などの情報を保持したまま）
                    shutil.copy2(file_path, destination_path)
                    print(f"ファイル '{file_path}' を '{destination_path}' にコピーしました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def copy_file(file_path, destination_dir, out_file_name):
    try:
        # コピー先ディレクトリが存在しない場合は作成する
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # コピー元ファイルが存在するか確認する
        if not os.path.isfile(file_path):
            print(f"Error: ファイル '{file_path}' が存在しません。スキップします。")
            return None
        else:
            # ファイルをコピーする準備
            file_name = out_file_name
            destination_path = os.path.join(destination_dir, file_name)

            # コピー先ディレクトリに同じファイルが存在するか確認する
            if os.path.exists(destination_path):
                print(f"ファイル '{destination_path}' はすでに存在します。スキップします。")
                return None
            else:
                # ファイルをコピーする（更新日時などの情報を保持したまま）
                shutil.copy2(file_path, destination_path)
                print(f"ファイル '{file_path}' を '{destination_path}' にコピーしました。")
                return destination_path
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

if __name__ == '__main__':
    main()
